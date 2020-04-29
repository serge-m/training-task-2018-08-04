#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
from torchvision.models.resnet import conv1x1, conv3x3, resnet18
from torchsummary import summary

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


# In[ ]:





# In[2]:


class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, inplanes, planes, stride=1, downsample=None, groups=1,
                 base_width=64, dilation=1, norm_layer=None):
        super(BasicBlock, self).__init__()
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        if groups != 1 or base_width != 64:
            raise ValueError('BasicBlock only supports groups=1 and base_width=64')
        if dilation > 1:
            raise NotImplementedError("Dilation > 1 not supported in BasicBlock")
        # Both self.conv1 and self.downsample layers downsample the input when stride != 1
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = norm_layer(planes)
        self.relu = nn.ReLU(inplace=True)
        self.conv2 = conv3x3(planes, planes)
        self.bn2 = norm_layer(planes)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity
        out = self.relu(out)

        return out


# In[3]:


class ResNetPart(nn.Module):

    def __init__(self, zero_init_residual=False):
        super(ResNetPart, self).__init__()
        
        self._norm_layer = nn.BatchNorm2d

        self.inplanes = 64
        self.dilation = 1
        self.groups = 1
        self.base_width = 64

        self.layer1 = self._make_layer(BasicBlock, 64, 2, stride=2)
        self.layer2 = self._make_layer(BasicBlock, 128, 2, stride=2)
        self.layer3 = self._make_layer(BasicBlock, 256, 2, stride=2)
        
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
            print("downsample")
            downsample = nn.Sequential(
                conv1x1(self.inplanes, planes * block.expansion, stride),
                norm_layer(planes * block.expansion),
            )

        layers = []
        layers.append(block(self.inplanes, planes, stride, downsample, 1, 
                            64, previous_dilation, norm_layer))
        self.inplanes = planes * block.expansion
        for _ in range(1, blocks):
            layers.append(block(self.inplanes, planes, groups=self.groups,
                                base_width=self.base_width, dilation=self.dilation,
                                norm_layer=norm_layer))

        return nn.Sequential(*layers)

    def _forward_impl(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = self.layer3(x)
        return x

    def forward(self, x):
        return self._forward_impl(x)


# In[ ]:





# In[4]:


class Model(pl.LightningModule):

    def __init__(self, hparams: Params):
        super().__init__()

        self.hparams = hparams
        self.model = nn.Sequential(
            nn.Conv2d(1, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
           
            ResNetPart(),
            
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(1),
            nn.Linear(256, 10),
        )
        self.loss = F.cross_entropy
        self.train_dataset = None
        self.val_dataset = None
        
        self.tfms_common = [
            transforms.ToTensor(),
            transforms.Normalize((0.285,), (.3523*2,))
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
        
        if batch_idx % 100 == 0:
            tqdm_dict['lr'] = np.array(self.trainer.lr_schedulers[0]['scheduler'].get_lr())
            
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
        return DataLoader(self.train_dataset, batch_size=self.hparams.batch_size_train, num_workers=0)

    def val_dataloader(self):
        if self.val_dataset is None:
            self.prepare_data()
        return DataLoader(self.val_dataset, batch_size=self.hparams.batch_size_val, num_workers=0)

    def test_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=self.hparams.batch_size_val, num_workers=0)

    def configure_optimizers(self):
        """
        Return whatever optimizers and learning rate schedulers you want here.
        At least one optimizer is required.
        """
        optimizer = optim.Adam(self.parameters(), lr=self.hparams.learning_rate)
        scheduler = optim.lr_scheduler.OneCycleLR(optimizer, max_lr=self.hparams.learning_rate, 
                                                  steps_per_epoch=1, 
                                                  epochs=self.trainer.max_epochs
                                                  )
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


# In[5]:


model = Model({})
summary(model, (1, 28, 28), device='cpu')
# model(torch.randn(10,1,28,28)).size()


# In[6]:


def main(hparams):
    model = Model(hparams)
    

    name = "Resnetish9_1intro_layer_L1_64_2_s2_L2_128_2_s2_L3_256_s2_avg_pool"
    logger = TensorBoardLogger("lightning_logs", name=name)

    checkpoint_callback = ModelCheckpoint(
        filepath=os.path.join('models', name, name+'_{epoch:02d}-{val_acc:.4f}-{val_loss:.4f}'),
        save_top_k=1,
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


# In[ ]:





# In[7]:


if __name__ == '__main__':
    parent_parser = ArgumentParser(add_help=False)

    # gpu args
    parent_parser.add_argument(
        '--gpus',
        type=int,
        default=1,
        help='how many gpus'
    )

    parser = Model.add_model_specific_args(parent_parser)
    hyperparams = parser.parse_args([
        "--learning_rate", "0.001",
        "--epochs", "40"])
    main(hyperparams)


# In[ ]:




