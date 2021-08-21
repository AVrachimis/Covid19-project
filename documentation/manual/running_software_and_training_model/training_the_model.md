# Training the Model

## Overview

This is a guide on how to train the model.  If you have added more images to the dataset, you must ensure that they are consistent with the pre-existing datasets.  To do this, follow the guide [here](documentation/manual/dataset/using_dataset_scripts.md)

## Things to Know

The following section details our recommended conditions for training the model:

- We are **not recommending** using the Jetson Nano to train the model.
  - This could be done, but given the our restrained time period, we did not attempt to do so.
- Our model is based on **MobileNetV2** which is a feature extractor within Keras.
- The time taken to train the model is **not** certain and depends on various factors, such as:
  - The more epochs to train, the more time it takes to train.  However, this results in a more accurate model.
  - The more datasets to train, the more time it takes to train.  However, this results in a more accurate model, although, there are limitations, such as overfitting (more details can be found [here](documentation/manual/adding_more_images_to_dataset.md)).
  - The higher batch size to train, the less time it takes to train overall, but this requires more GPU memory.
  - the larger input shape, the more time it takes to train.  However, this results in a more accurate model (may take longer to make predictions).
- The images within the dataset should have the same resolution as higher resolution images will require more memory, and therefore, more time to train (more details can be found [here](documentation/manual/adding_more_images_to_dataset.md)).
- The dataset should have the same amount of images in each folder to ensure that the trained model is as general as possible (more details can be found [here](documentation/manual/adding_more_images_to_dataset.md)).

## Step-by-step Guide to Train the Model

#### **1.) Clone the Repository**

Clone the repository using `git clone` or download directly:

```
$ git clone https://stgit.dcs.gla.ac.uk/tp3-2020-CS31/cs31-main
```

Unzip the downloaded file (skip this if you used `git clone`).

#### **2.) Configure Environment**

To configure your environment, you can follow the guide [here](documentation/manual/environment_setup/local_env_setup.md)

If you have an NVIDIA GPU, you can install the GPU accelerator library, found [here](https://www.tensorflow.org/install/gpu).

##### **(Optional) Modifying Parameters** 

You can modify the following parameters based on your requirements:

- `BATCH_SIZE`
- `EPOCHS`
- `INPUT_SHAPE`

#### **4.) Prepare the Dataset**

For this, please refer to the guide [here](documentation/manual/dataset/adding_more_images_to_dataset.md).

#### **5.) Run `train_model.py`**

You can change the following parameters prior to execution:

- `-d`: path to dataset.
- `-m`: name of the outputted model.

##### **Usage Example (Windows):**

```
$ conda activate
$ python .\model_scripts\train_model.py -d dataset -m mask_detector.model
```

##### **Usage Example (Linux):**

```
$ source activate
$ python3 ./model_scripts/train_model.py -d dataset -m mask_detetor.model
```

#### Troubleshooting

If any errors occur during this process, follow the troubleshooting guide [here](documentation/troubleshooting/errors_training_model.md)