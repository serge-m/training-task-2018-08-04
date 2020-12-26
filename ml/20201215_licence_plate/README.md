# Licence plate detection

Two stage licence plate detection. On the first stage we detect vehicles. On the second stage we detect  licence
plates inside the detected vehicle images.

Both detectors are yolo v4. The licence plate detector is trained according to the 
[tutorial](https://github.com/theAIGuysCode/YOLOv4-Cloud-Tutorial)



## Training YoloV4

Training procedure for licence plates closely follows the process described in the 
[tutorial by TheAIGuy](https://github.com/theAIGuysCode/YOLOv4-Cloud-Tutorial).

`prepare_data_for_training.sh` - data set preparation

`train_yolo4_lp.ipynb` - google colab notebook for training. 
In case you are training a different problem the configs must be adjusted as described in the aforementioned  tutorial.

The training for LP takes about 5h.



## Predictions

`pip3 install -r requirements.txt` to install dependencies.

`install.sh` - to download and compile darknet.

trained weight link - todo.

`detect_lp.py` - run the detections on a list of jpg images from a directory and save results to jsons.

`draw_lp.py` - visualize the predictions from jsons as jpg images with bounding boxes.



