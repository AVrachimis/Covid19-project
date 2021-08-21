# Local Environment Setup Guide

## Overview

Below is a guide detailing how to install the packages required to run this repository and how to setup a local environment on both Ubuntu and Windows.  Unfortunately, we could not provide information on MacOS installation.

## Prerequisites

First ensure that you have installed Python (version 3.8) and Git on your machine.  Additionally, if you are using Windows, install Anaconda so that you can setup this environment within your system.

## Windows (10)

#### 1.) Cloning the Repository

Firstly, clone the repository by running the following command in your terminal:

```$ git clone https://stgit.dcs.gla.ac.uk/tp3-2020-CS31/cs31-main.git```

This will download the repository to your current directory.  Alternatively, if you have downloaded this repository, then you can simply move it to the folder which you wish to run the software from.

#### 2.) Creating the Environment

Firstly, run the Anaconda Prompt - you can do this by pressing the Windows key and typing "Anaconda Prompt (anaconda3)".  Once you have done this, check that conda is up-to-date:

```$ conda update conda```

Update any necessary packages by typing `y` to proceed.

In the prompt, enter the following, replacing `env_name` with the name you wish to use, and x.x with the version of Python you wish to use.  We recommend 3.8 but this is compatible with versions >= 3.6.

```$ conda create -n env_name python=x.x```

If it asks you to install other dependent packages, type `y` to proceed.

Now, in the terminal, navigate to the directory which contains the repository.  You can do this by using `cd`:

```$ cd /path/to/repository```

#### 3.) Activation and Install

To activate your virtual environment, run:

```$ conda activate env_name```

Before you install the relevant packages, ensure that you have installed `pip` within your anaconda environment:

```$ conda install pip```

Then, run the following command to install the packages from the `requirements.txt` file:

```$ pip install -r requirements.txt```

#### 4.) Running the Software and Closing

You have now fully installed and set up your local environment on your Windows system.  To run the software see "Running the Facemask Detector" [(click here)](documentation/manual/running_software_andtraining_model/running_facemask_detector.md).

Once you are finished with your environment and you wish to close it, run the following:

```
$ conda deactivate
$ exit
```

## Ubuntu (18.04, 20.04)

#### 1.) Updating Ubuntu

Before installation, make sure your system is updated:

```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt auto-remove
```

Additionally, ensure that you have the correct version of Python installed.  Check this by using the following command in a terminal:

```$ python --version```

#### 2.) Cloning the Repository

Similar to the Windows guide, either install the repository or clone it directly from the GitLab, and move it into the directory you wish to work from.  Do this by running the following command in a terminal:

```$ git clone https://stgit.dcs.gla.ac.uk/tp3-2020-CS31/cs31-main.git```

#### 3.) Installation

In a terminal, navigate to where you downloaded the repository.  Do this by running the following:

```$ cd /path/to/repository```

Then, install the packages from the `requirements.txt` file by executing:

```$ pip install -r requirements.txt```

#### 4.) Running the Software

You have now fully installed and set up your local environment on your Linux/Ubuntu system.  To run the software see "Running the Facemask Detector" [(click here)](documentation/manual/running_software_andtraining_model/running_facemask_detector.md).