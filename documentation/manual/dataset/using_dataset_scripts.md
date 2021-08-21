# Using the Dataset Scripts

## Overview

This is a guide on how to use the dataset scripts to normalize the dataset.

## `artificial_facemask.py`

Due to the lack of 'incorrect mask' images, an artificial facemask script has been created in order to artificially create more images which show individuals wearing their mask on the chin and below the nose.

Based on the dataset's requirements, mask colour and type can be specified accordingly, allowing five different facemask colours and three different types of images:

**Mask Colours:**
- Black.
- Dark blue.
- Grey.
- Red.
- White.

**Image Types:**
- Correct facemask placement.
- Incorrect facemask placement below the nose.
- Incorrect facemask placement only covering the chin.

#### **Script Arguments:**

The program requires either `--image` or `--folder` for the input image(s).

- `--image`: allows the program to artificially place a mask on a single image, with the argument's value equalling the path to the image.
- `--folder`: allows the program to artificially place a mask on images within a directory, with the argument's value equalling the path of the folder of images.  All files in this folder must be an image and must be normalized according to the guide found [here](documentation/manual/dataset/adding_more_images_to_dataset.md).
- `--mask`: required argument specifying the path to the input mask image file.  Available paths:
  - `dataset_scripts/resources/black_mask/mask.png`
  - `dataset_scripts/resources/dark_blue_mask/mask.png`
  - `dataset_scripts/resources/grey_mask/mask.png`
  - `dataset_scripts/resources/red_mask/mask.png`
  - `dataset_scripts/resources/white_mask/mask.png`
- `--dataset`: required argument specifying the path of the output image file.  If the path does not exist already, the script will create the directory automatically.

#### **Usage Example:**

```
$ python dataset_scripts/artificial_facemask.py --image faces/image.jpg --type nose --mask dataset_scripts/resources/black_mask/mask.png --labels dataset_scripts/resources/black_mask/facemask_labels.csv --dataset face_dataset
```

## `rename.py`

This scripts renames images within a given directory to follow the naming convention required by the `train_model.py` script.  Note that, you should run the script in the `cs31-main/dataset_scripts` directory.

#### **Script Arguments:**

The script takes two required arguments, the *dataset folder*, and the *folder name* of the images which you want to rename.

For the second argument, you must specify the type of image.  The options are:

- `withMask` which renames all the images within the `withMask` folder to the following format: `mask-0001.jpg`, `mask-0002.jpg`, `mask-003.jpg`, ...
- `withoutMask` which renames all the images within the `withoutMask` folder to the following format: `no-mask-0001.jpg`, `no-mask-0002.jpg`, `no-mask-003.jpg`, ...
- `incorrectMask` which renames all the images within the `incorrectMask` folder to the following format: `incorrect-mask-0001.jpg`, `incorrect-mask-0002.jpg`, `incorrect-mask-0003.jpg`, ...

#### **Usage Example:**

```
$ python rename_images.py sampleDataset withMask
```

## `resize_images.py`

This script is used to ensure that all dataset images have the same resolution (800x800) by resizing the images based on a given width.  The aspect ratio of the resized images are kept the same.  Note that, you should run the script in the `cs31-main` directory.  This will output the resized image into a new folder called `resized_images` with path `cs31-main/resized_images`.

#### **Usage Example:**

```
$ python .\dataset_scripts\resize.py --folder .\faces\ --width 800
```