# Best Model Type for Jetson Nano

Since we are using an NVIDIA Jetson Nano, the most appropriate object detection algorithms are single shot methods.  The main differences between other types of methods (RCNN) is speed.  This is the main reason why single shot methods are preferred when smaller, low-cost hardware is used (Jetson Nano, in our case).

Out of the Single shot methods, two of them fit more to our project needs:

- `SSD` (Single Shot Detector).
- `YOLO` (You Only Look Once).

In both object detection models, GPU is recommended for model training, however a CPU can be used as well with much slower results.

## SSD

#### **How It Works:**

The SSD approach discretises the output space of bounding boxes into a set of default boxes over different aspect ratios.  After discretising, the method scales per feature map location.  The Single Shot Detector network combines predictions from multiple feature maps with different resolutions to naturally handle objects of various sizes [Reference](https://analyticsindiamag.com/top-8-algorithms-for-object-detection/).

An example of SSD model is [MobileNetV2](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV2).

## YOLO

Although slower that the SSD, it is still one of the fastest model types and this is due its simple architecture.

#### **How It Works:**

Split the image into grid and within each grid a number of bounding boxes is taken (always produce the same number of bounding boxes) with each bounding box having its own probability class.  Once all the probabilities have been calculated, those above a certain threshold value are used to locate the object within the image.

#### **Potential Drawbacks:**

Due to its architecture, detecting smaller objects within the image, can be not as accurate as other model types.  In our project this is not something to concern us.