#!/bin/sh
set -x
set -e

git clone https://github.com/AlexeyAB/darknet darknet
(cd darknet && git checkout -b "a298" "a298f94255a20a3198d80ea512755d9e5dddbf02")

# for training with GPU. Comment out if you dont have CUDA.
(cd darknet && \
 sed -i 's/OPENCV=0/OPENCV=1/' Makefile && \
 sed -i 's/GPU=0/GPU=1/' Makefile && \
 sed -i 's/CUDNN=0/CUDNN=1/' Makefile && \
 sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile \
)

(cd darknet && ./build.sh)

( \
  mkdir -p data && \
  mkdir -p cfg && \
  cd data && \
  wget --timestamping https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights && \
  cd .. && \
  ls \
)
