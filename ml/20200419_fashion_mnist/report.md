# Report

##Software
Code of the experiments can be found here: 
https://github.com/serge-m/code-training/tree/master/ml/20200419_fashion_mnist

or here: 

https://drive.google.com/open?id=1JIFSNX_tRze4LH4pF1N8YWGNa4FEuyxq 

I use pytorch and pytorch-lightning libraries as a framework for my experiments.
Each experiment is implemented in a separate python file. Model and the training parameters are set up using standard pytorch-lightning conventions. Each experiment script defines a model and optimization loop, trains a model and runs the evaluation on the test set. The results are written to stdout and dumped to lightning_logs directory in tensorboard format.

Validation and tests are performed on the same data set. That may lead to sub-optimal hyperparameters selection and worse generalization, but I assume it is good enough for this training task.

Fashion MNIST data set is downloaded automatically using standard pytorch functions.


Some notes about code structure:
- data - default location for downloaded FashinMNIST dataset (downloaded automatically by scripts if missing)
- models - trained models
- lightning_logs - logs for tensorboard

Developed on Ubuntu 18 with python3.6.

## How to run

    # install python3-venv if missing
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -U pip
    pip install -r requirements.txt
    # then run a command for experiment (see below)


## Experiments
### Experiment 1. VGG-like network
I start with a model that is similar to VGG backbone: several blocks of convolutional layers followed by a fully connected layer. 

Command:

    python 2020041907_port3_fashion_mnist_with_test.py --gpus 1 --epochs 15


The network contains roughly 6 million parameters which is significantly lower than resnet-101 mentioned in the task description with 44,5 M parameters.

### Experiment 2. Normalizing inputs

The range of the input data in the previous experiment was not normalized. In this experiment I subtract the mean and set variance to 0.5. 

Command:
    
    python 2020041907_port5_fashion_mnist_norm.py --gpus 1 --epochs 15

The change didn’t bring an improvement. The accuracy stays approximately the same.
The validation loss increases in the end for both experiments, while training loss decreases (overfitting)



### Experiment 3. Augmentation with random crop
Random crop is applied to the training set.

Command:

    python 202004191231_fashion_mnist_crop_norm_no_tfms_on_val.py --gpus 1 --epochs 15

There is no gain in accuracy - it’s approximately the same as before: 0.92



With lower learning rate it achieves accuracy  0.932.

Command:
    python 202004191231_fashion_mnist_crop_norm_no_tfms_on_val.py --gpus 1 --epochs 15 --learning_rate 0.001


### Experiment 4. One cycle LR

Applying “one cycle” LR schedule

Command:
    
    python 202004191306_fashion_mnist_lr2.py --gpus 1 --epochs 15 --learning_rate 0.01

Result: A bit better accuracy: 0.937


    python 202004191306_fashion_mnist_lr2.py --gpus 1 --epochs 15 --learning_rate 0.001

Result: Approximately same accuracy: 0.938


### Experiment 5. Longer training

If we train a bit longer (40 epochs) we can achieve accuracy of 0.946, which is approximately equal to our target.

Command:
    
    python 202004191306_fashion_mnist_lr2.py --gpus 1 --epochs 40 --learning_rate 0.001




### Experiment 6. more augmentation

I added small random rotations to the training set. That didn’t bring much benefits: accuracy is approximately the same: 0.9467

Command:
    
    python 202004191500_fashion_mnist_augm_crop_rot.py --gpus 1 --epochs 40 --learning_rate 0.001


### Experiment 7. Resnet

Modified resnet18 with less layers and input convolutional layer with 1 channel as input.


    python 202004192100_fashion_mnist_resnet2.py --gpus 1 --epochs 60 --learning_rate 0.001 --batch_size_train=128

Best results I got is 0.934 with 2M parameters


### Experiment 7. Resnet

Modified resnet18 with less layers and input convolutional layer with 1 channel as input.


    python 202004192100_fashion_mnist_resnet2.py --gpus 1 --epochs 60 --learning_rate 0.001 --batch_size_train=128

Best results I got is 0.934 with 2M parameters


### Experiment 8. Resnet and MobileNetV2 

I switched from Adam+OneCycle to Stochastic gradient descent with gradually decreasing learning rate. Also I tested an adapted version of MobileNetV2. MobileNet is a well known choice for limited systems. It has about 4 M parameters. For my case I reduced that number further to 0.68 M parameters. 

In both cases I achieved only accuracy of 0.931.

Commands
    
    python 202004192200_fashion_mnist_resnet_sgd.py --gpus 1 --epochs 200 --learning_rate 0.01 --batch_size_train=128
    python 202004192300_fashion_mnist_mobilenetv2_1.py --gpus 1 --epochs 200 --learning_rate 0.01 --batch_size_train=128


### Experiment 9. Resnet with smaller kernel for intro layer 

It was unclear why resnet performs worse than VGG-like. I looked at the differences between those two networks and realized that there is a much bigger kernel for standard resnet: 7 pixels.

I ran another experiment with a smaller intro kernel and achieved much better results.

Probably the input image is much smaller for fashion mnist than for imagenet and bigger kernels don’t make any sense.

Accuracy: 0.9426

Commands:

    python 2020042701_fashion_mnist_resnet_redo_w_smaller_intro_kernel_report_grads.py --gpus 1 --epochs 40 --learning_rate 0.001 --batch_size_train=128


### Experiment 10. Resnet-like matching the performance of VGG-like
After some experiments with the resnet-like model I was able to achieve the same performance as VGG-like.

The resnet-like model has less parameters: about 2 million.

Accuracy: 0.9467

Command:

    python 2020042523_Resnetish9_1intro_layer_L1_64_2_s2_L2_128_2_s2_L3_256_s2_avg_pool.py



## Results

So the best results so far I got for the VGG-like model. It is not a very small model, but it’s significantly smaller than Resnet101 mentioned in the task description. 

For the specification look at the source code of the model: 202004191500_fashion_mnist_augm_crop_rot.py
    
    Approximate number of parameters: 6 Millions
    Accuracy on test set: 0.9467
    Inference speed on CPU with batch size 1: ~250 FPS
    Inference speed on CPU with batch size 32: ~2000 FPS
    Inference speed on GPU with batch size 32: ~10000 FPS

Trained model can be downloaded here: https://drive.google.com/open?id=1crXV3Iw50FimGcQGYTlNXf2QHdnqUBqN


**UPD: smaller Resnet-like model was trained with the same accuracy and only 2 M parameters.**


 

