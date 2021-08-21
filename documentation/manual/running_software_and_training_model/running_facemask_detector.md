# Running the Facemask Detector

## Overview

This is a guide on how to run the facemask detector for a video or an image.

## Script Arguments

The following arguments must be passed prior to execution:

- `-t TYPE`: (required - has to be a option between (`video`, `image`))
  - You can either run the facemask detector on a single image or a live video feed.
- `-m MODEL`: (optional - will default to mask_detector.model) directory of trained model will be saved in the following format: mask_detector.model
- `-i IMAGEPATH`: Only required when running the facemask detection algorithm on a single image.
  - An example format is: `dataset/incorrectMask/incorrect-mask-0001.jpg`.

## Step by Step to run the detector:

You must ensure that you have installed the required environment to run the detector, to do this refer to the guide [here](documentation/manual/running_software_and_training_model/training_the_model.md)

Then, you can run the detector:

#### **Usage Example (for a video):**

```
$ conda activate
$ cd cs31-main
$ python mask_detection.py -m mask_detector.model -t video
```
#### **Usage Example (for an image):**

```
$ conda activate
$ cd cs31-main
$ python mask_detection.py -m mask_detector.model -t image -i image.jpg
```