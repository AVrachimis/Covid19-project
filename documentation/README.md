# Documentation

## Overview

This directory contains the relevant documentation on how to use and troubleshoot the software, as well as make any changes to the model.  

## Manual

#### Dataset

This section details how to add more images to the existing dataset and how to use the scripts to normalize the new images.  To view the documentation on how the dataset was collated or how an overview of how the scripts function, see *Development Documentation*.

- [Adding more images to the dataset](manual/dataset/adding_more_images_to_dataset.md)
- [Using the dataset scripts](manual/dataset/using_dataset_scripts.md)

#### Running the Software and Training the Model

This section discusses how to train the model and how to execute the facemask detector.  NOTE: as this is a prototype, it is not fully optimised against all conditions, so please use the *User Guide* to use the system to its full effectiveness.

- [Training the model](manual/running_software_and_training_model/training_the_model.md)
- [Running the facemask detector](manual/running_software_and_training_model/running_facemask_detector.md)
- [User guide](manual/running_software_and_training_model/user_guide.md)

#### Environment Setup

- [Setting up the Jetson Nano environment](manual/environment_setup/jetson_nano_env_setup.md)
- [Using the Jetson Nano environment](manual/environment_setup/using_jetson_nano_env.md)
- [Setting up local environment (Ubuntu or Windows machines)](manual/environment_setup/local_env_setup.md)

## Troubleshooting

This directory details the possible errors that could occur when using the system and how to fix them.  We tried to be as comprehensive as possible when covering these, so if any other issues arise, then please contact us.

- [Errors while installing NumPy](troubleshooting/errors_installing_numpy.md)
- [Errors while training the model](troubleshooting/errors_training_model.md)
- [Errors while using pre-setup Python environment](troubleshooting/errors_using_python_env.md)
- [Errors with camera configuration](troubleshooting/errors_with_camera_config.md)

## Development Documentation

This section contains information on the various scripts that the software depends on as well as how the dataset was compiled, the chosen computer vision model, and possible further optimisation techniques.

- [Dataset](development_documentation/dataset.md)
- [Best model type for Jetson Nano](development_documentation/best_model_type.md)
- [Further optimisation](development_documentation/further_optimisation.md)
