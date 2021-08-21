# Adding more Images to the Dataset

## Overview

This is a step-by-step guide on how to add more images to the existing dataset.  Firstly, ensure that:
- all three folders have exactly the same number of images, i.e., when adding images to a specific folder, you should also add the same number of images to the other folders.
- images should have the same extension as the images already in the dataset (JPEG).
- the resoultion of the images should be at least 800x800.
- avoid adding images that are already in the dataset.

## 1.) Choose the number of images you want to add to the dataset

Currently, the dataset already has 1,200 images of each type.  Adding too many images may cause overfitting, which occurs when a machine learning model learns the details and noise in the training to the extent that it negatively impacts the performance of the model on fresh data.  Choose a small number of images (100-200 maximum) to avoid this.

## 2.) Collect the images you want to add

Detailed below are possible suggestions of datasets in which you can collect images from.  These are the datasets that we also used so try to avoid adding images which are already in the dataset.  You can also add images from your own dataset as long as they obey the conditions above (see *Overview*).

**Images of individuals without a mask**

Dataset with 70,000 images of individuals not wearing a mask.  The chosen images from this dataset are from the `/00000` and `/01000` folders, so avoid using these folders to prevent clone images.  Note that, the images from this dataset use the PNG extension, so ensure that you convert them to JPG.

**Images of individuals correctly wearing a mask**

Dataset with 70,000 images of individuals wearing a mask correctly.  The chosen images from this dataset are from the `/00000` and `/01000` folders, so avoid using these folders to prevent clone images.  The images from this dataset use the JPG extension, so no conversion is needed.

**Images of individuals incorrectly wearing a mask**

Dataset with 70,000 images of individuals wearing a mask incorrectly.  There are three different incorrect placements of facemasks:

- `mask_nose_mouth`: the mask only covers the nose and mouth.
- `mask_mouth_chin`: the mask only covers the mouth and chin.
- `mask_chin`: the mask only covers the chin.

Avoid adding images from the `mask_nose_mouth` category as they are almost identical to the images within the `mask_chin` folder.  The chosen images from this dataset are from the `/00000` and `/01000` foders, so avoid using these folders to prevent clone images.  Furthermore, this dataset only consists of images with light blue masks.  Note that, the the images from this dataset use the JPG extension, so no conversion is needed.

**Alternative: artificial facemask script**

An alternative approach is to use the `artificial_facemask.py` script which artificially places the mask on an individual's face.  This is sometimes more preferable over the datasets detailed above since it provides a larger variety of facemask colours (5 colors), which will create a more generalized model.

You should only choose images which show individuals with no facemask.  More information on how to use this script can be found [here](documentation/manual/dataset/using_dataset_scripts.md).

## 3.) Apply the scripts to the newly collected dataset

Once the images are collected and placed into their respective folders, two more scripts must be run to apply data normalization, ensuring that the entire dataset is consistent.

Firstly, apply the `resize.py` script to the whole dataset folder to ensure every image has the same resolution.  A width of 800 must be specified during execution.  More information on this script can be found [here](documentation/manual/dataset/using_dataset_scripts.md).

Then, apply the `rename_images.py` script to the whole dataset to verify that all images follow our specified naming convention.  More information on this script can be found [here](documentation/manual/dataset/using_dataset_scripts.md).

## 4.) Train the model

Once the dataset has been collected and normalized, the model must be retrained to accomodate the new changes.  To do this follow the guide [here](documentation/manual/running_software_and_training_model/training_the_model.md)
