#!/usr/bin/env python
# coding: utf-8

import os

import torch
from pytorch_lightning.callbacks import ModelCheckpoint
from torch import nn
from torch.nn import functional as F
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST, FashionMNIST

from argparse import ArgumentParser

import pytorch_lightning as pl
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_lightning import Trainer
from collections import OrderedDict
from torch import optim
import numpy as np
from dataclasses import dataclass
from torchvision.models.resnet import Bottleneck, BasicBlock, conv1x1


def reduce_mean_dicts(list_dicts, key):
    if not list_dicts:
        return 0.

    s = sum([d[key] for d in list_dicts], 0.)
    return s / len(list_dicts)


@dataclass
class Params:
    batch_size_train: int
    batch_size_val: int
    path_data: str
    learning_rate: float


# from pytorch
class ResNet(nn.Module):

    def __init__(self, block, layers, num_classes=1000, zero_init_residual=False,
                 groups=1, width_per_group=64, replace_stride_with_dilation=None,
                 norm_layer=None):
        super(ResNet, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        self._norm_layer = norm_layer

        self.inplanes = 64
        self.dilation = 1
        if replace_stride_with_dilation is None:
            # each element in the tuple indicates if we should replace
            # the 2x2 stride with a dilated convolution instead
            replace_stride_with_dilation = [False, False, False]
        if len(replace_stride_with_dilation) != 3:
            raise ValueError("replace_stride_with_dilation should be None "
                             "or a 3-element tuple, got {}".format(replace_stride_with_dilation))
        self.groups = groups
        self.base_width = width_per_group
        self.conv1 = nn.Conv2d(1, self.inplanes, kernel_size=7, stride=2, padding=3,
                               bias=False)
        self.bn1 = norm_layer(self.inplanes)
        self.relu = nn.ReLU(inplace=True)
        self.maxpool = nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        self.layer1 = self._make_layer(block, 64, layers[0])
        self.layer2 = self._make_layer(block, 128, layers[1], stride=2,
                                       dilate=replace_stride_with_dilation[0])
        self.layer3 = self._make_layer(block, 256, layers[2], stride=2,
                                       dilate=replace_stride_with_dilation[1])

        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        self.fc = nn.Linear(256 * block.expansion, num_classes)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, (nn.BatchNorm2d, nn.GroupNorm)):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

        # Zero-initialize the last BN in each residual branch,
        # so that the residual branch starts with zeros, and each residual block behaves like an identity.
        # This improves the model by 0.2~0.3% according to https://arxiv.org/abs/1706.02677
        if zero_init_residual:
            for m in self.modules():
                if isinstance(m, Bottleneck):
                    nn.init.constant_(m.bn3.weight, 0)
                elif isinstance(m, BasicBlock):
                    nn.init.constant_(m.bn2.weight, 0)

    def _make_layer(self, block, planes, blocks, stride=1, dilate=False):
        norm_layer = self._norm_layer
        downsample = None
        previous_dilation = self.dilation
        if dilate:
            self.dilation *= stride
            stride = 1
        if stride != 1 or self.inplanes != planes * block.expansion:
            downsample = nn.Sequential(
                conv1x1(self.inplanes, planes * block.expansion, stride),
                norm_layer(planes * block.expansion),
            )

        layers = []
        layers.append(block(self.inplanes, planes, stride, downsample, self.groups,
                            self.base_width, previous_dilation, norm_layer))
        self.inplanes = planes * block.expansion
        for _ in range(1, blocks):
            layers.append(block(self.inplanes, planes, groups=self.groups,
                                base_width=self.base_width, dilation=self.dilation,
                                norm_layer=norm_layer))

        return nn.Sequential(*layers)

    def _forward_impl(self, x):
        # See note [TorchScript super()]
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.maxpool(x)

        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)

        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)

        return x

    def forward(self, x):
        return self._forward_impl(x)

class ResnetV2SGD(pl.LightningModule):

    def __init__(self, hparams: Params):
        super().__init__()

        self.hparams = hparams
        self.model = ResNet(BasicBlock, [2, 2, 2, 1], num_classes=10)
        self.loss = F.cross_entropy
        self.train_dataset = None
        self.val_dataset = None
        
        self.tfms_common = [
            transforms.ToTensor(),
            transforms.Normalize((0.285,), (.3523,))
        ]
        self.tfms_train = [
            transforms.RandomRotation(7., fill=(0,)),
            transforms.RandomCrop(28, padding=3),
        ]
        

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
         
        loss_val = self.loss(y_hat, y, )

        
        tqdm_dict = {'train_loss': loss_val,
                    }
        
        # if batch_idx % 100 == 0:
        #     tqdm_dict['lr'] = np.array(self.trainer.lr_schedulers[0]['scheduler'].get_lr())
            
        return OrderedDict({
            'loss': loss_val,
            'log': tqdm_dict
        })

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)

        loss_val = self.loss(y_hat, y, )

        # acc
        labels_hat = torch.argmax(y_hat, dim=1)
        val_acc = torch.sum(y == labels_hat).item() / (len(y) * 1.0)
        val_acc = torch.tensor(val_acc)

        if self.on_gpu:
            val_acc = val_acc.cuda(loss_val.device.index)

        output = OrderedDict({
            'val_loss': loss_val,
            'val_acc': val_acc,
        })

        return output

    def validation_epoch_end(self, outputs):
        loss_mean = reduce_mean_dicts(outputs, 'val_loss')
        acc_mean = reduce_mean_dicts(outputs, 'val_acc')
        tqdm_dict = {
            'val_loss': loss_mean,
            'val_acc': acc_mean
        }
        result = {'progress_bar': tqdm_dict, 'log': tqdm_dict, 'val_loss': loss_mean}
        return result

    def prepare_data(self):

        mnist_train = FashionMNIST(self.hparams.path_data, train=True, download=True,
                                   transform=transforms.Compose(self.tfms_train + self.tfms_common)
                                  )
        mnist_test = FashionMNIST(self.hparams.path_data, train=False, download=True,
                                  transform=transforms.Compose(self.tfms_common)
                                  )

        #         mnist_train, mnist_val = random_split(mnist_train, [55000, 5000])

        self.train_dataset = mnist_train
        self.val_dataset = mnist_test

    def train_dataloader(self):
        if self.train_dataset is None:
            self.prepare_data()
        return DataLoader(self.train_dataset, batch_size=self.hparams.batch_size_train, num_workers=12, shuffle=True)

    def val_dataloader(self):
        if self.val_dataset is None:
            self.prepare_data()
        return DataLoader(self.val_dataset, batch_size=self.hparams.batch_size_val, num_workers=8)

    def test_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.hparams.batch_size_val, num_workers=0)

    def configure_optimizers(self):
        """
        Return whatever optimizers and learning rate schedulers you want here.
        At least one optimizer is required.
        """
        optimizer = optim.SGD(self.parameters(), lr=self.hparams.learning_rate, momentum=0.9)
        scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min')
        # optimizer = optim.Adam(self.parameters(), lr=self.hparams.learning_rate)
        # scheduler = optim.lr_scheduler.OneCycleLR(optimizer, max_lr=self.hparams.learning_rate,
        #                                           steps_per_epoch=1,
        #                                           epochs=self.trainer.max_epochs
        #                                           )
        return [optimizer], [scheduler]

    @staticmethod
    def add_model_specific_args(parent_parser):  # pragma: no-cover
        parser = ArgumentParser(parents=[parent_parser])

        parser.add_argument('--learning_rate', default=0.01, type=float)
        parser.add_argument('--batch_size_train', default=64, type=int)
        parser.add_argument('--batch_size_val', default=32, type=int)
        parser.add_argument('--path_data', default="./data", type=str)

        # training params (opt)
        parser.add_argument('--epochs', default=20, type=int)
        return parser

    def test_step(self, batch, batch_idx):
        """
        Lightning calls this during testing, similar to `validation_step`,
        with the data from the test dataloader passed in as `batch`.
        """
        output = self.validation_step(batch, batch_idx)
        # Rename output keys
        output['test_loss'] = output.pop('val_loss')
        output['test_acc'] = output.pop('val_acc')
        return output

    def test_epoch_end(self, outputs):
        loss_mean = reduce_mean_dicts(outputs, 'test_loss')
        acc_mean = reduce_mean_dicts(outputs, 'test_acc')
        tqdm_dict = {
            'test_loss': loss_mean,
            'test_acc': acc_mean
        }
        result = {'progress_bar': tqdm_dict, 'log': tqdm_dict, 'test_loss': loss_mean}
        return result


def main(hparams):
    model = ResnetV2SGD(hparams)
    name = type(model).__name__
    logger = TensorBoardLogger("lightning_logs", name=name)

    checkpoint_callback = ModelCheckpoint(
        filepath=os.path.join('models', name, name+'_{epoch:02d}-{val_acc:.4f}-{val_loss:.4f}'),
        save_top_k=2,
        verbose=True,
        monitor='val_acc',
        mode='max',
        prefix=''
    )

    trainer = pl.Trainer(
        max_epochs=hparams.epochs,
        gpus=hparams.gpus,
        logger=logger,
        checkpoint_callback=checkpoint_callback,
        # precision=16 if hparams.use_16bit else 32,
        progress_bar_refresh_rate=50,
    )

    trainer.fit(model)

    trainer.test(model)


if __name__ == '__main__':
    root_dir = os.path.dirname(os.path.realpath(__file__))
    parent_parser = ArgumentParser(add_help=False)

    # gpu args
    parent_parser.add_argument(
        '--gpus',
        type=int,
        default=1,
        help='how many gpus'
    )

    parser = ResnetV2SGD.add_model_specific_args(parent_parser)
    hyperparams = parser.parse_args()
    main(hyperparams)
