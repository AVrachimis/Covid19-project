# Setting up Jetson Nano Environment

## Overview

This guide is designed for the NVIDIA's Jetson Nano 4GB Developer Kit.  Other devices or future updates may differ slightly.

## Prerequisites 

To get started, you will require:

- MicroSD card (minimum recommended is 32GB UHS-1 card).
- Micro-USB power supply.
- Jeston Nano 4GB Developer Kit.
- Keyboard and mouse
- WiFi dongle or available ethernet connection.
- USB webcam.
- PureThermal mini/2 USB breakout board.
- Lepton 3.5 thermal camera.

## 1.) Format and Write Image to the MicroSD Card

Follow the instructions on the [NVIDIA Developer](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write) website to format and write the image to your microSD card.  This can be done on Windows, MacOS, and Linux platforms.

## 2.) Setup and Initial Boot

- First, plug in your keyboard, mouse, WiFi dongle or ethernet cable, and display cable.
- Then, insert the microSD card (which has the system image already written on it), into the slot on the underside of the Jetson Nano module (opposite the USB ports).
- Plug in the power supply and power on the Jetson Nano.
- On boot, you will be asked to complete a setup guide.
  - You will be asked to select `APP` partition size; please select the maximum size suggested.
- Once the setup is complete, you should be taken to the desktop.

If you would like more information on setting up and boothing the Jetson Nano, please click [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#setup).

## 3.) Updating the Jeston Nano and Removing Unecessary Programs

First, set the power capacity of the Nano to maximum:

```
$ sudo nvpmodel -m 0
$ sudo jetson_clocks
```

Then, remove LibreOffice - unless you expect that you will require it later, as it takes up a lot of uncessary space.

```
$ sudo apt-get purge libreoffice*
$ sudo apt-get clean
```

Now, you can go ahead and update system-level packages:

```
$ sudo apt-get update && sudo apt-get upgrade
```

## 4.) Installing System-level Dependencies and Updating `CMake`

First, we need to install a collection of development tools:

```
$ sudo apt-get install git cmake
$ sudo apt-get install libatlas-base-dev gfortran
$ sudo apt-get install libhdf5-serial-dev hdf5-tools
$ sudo apt-get install libhd5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev
$ sudo apt-get install python3-dev
$ sudo apt-get install nano locate
```

You will also need to install SciPy prerequisites and and a system-level Cython library:

```
$ sudo apt-get install libfreetype6-dev python3-setuptools
$ sudo apt-get install protobuf-compiler libprotobuf-dev openssl
$ sudo apt-get install libssl-dev libcurl4-openssl-dev
$ sudo apt-get install cython3
```

Then, update the CMake precompiler tool.  This will be needed to compile OpenCV later.  To do this, download and extract the CMake update:

```
$ wget http://www.cmake.org/files/v3.13/cmake-3.13.0.tar.gz
$ tar xpvf cmake-3.13.0.tar.gz cmake-3.13.0/
```

Next, compile CMake:

```
$ cd cmake-3.13.0/
$ ./bootstrap --system-curl
$ make -j4
```

Afterwards, update your bash profile.  Make sure that you do not delete the `cmake-3.13.0/`:

```
$ echo 'export PATH=/home/nvidia/cmake-3.13.0/bin/:$PATH' >> ~/.bashrc
$ source ~/.bashrc
```

## 5.) Installing OpenCV System-level Dependencies and other Development Packages

First, install the following tools.  These will allow you to build and compile OpenCV with parallelism to speed up installation:

```
$ sudo apt-get install build-essential pkg-config
$ sudo apt-get install libtbb2 libtbb-dev
```

Next, install the following codecs and image libraries:

```
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt-get install libxvidcore-dev libavresample-dev
$ sudo apt-get install libtiff-dev libjpeg-dev libpng-dev
```

Afterwards, install Video4Linux so that we can use the USB camera:

```
$ sudo apt-get install libv4l-dev libdc1394-22-dev
```

## 6.) Setting up a Virtual Environment

First, install the Python package `pip`:

```
$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py
$ rm get-pip.py
```

Next, install the following tools which are used to manage the virtual environment:

```
$ sudo pip install virtualenv
```

#### **(Optional but recommended) Install `virtualenvwrapper`**

Install `virtualenvwrapper` using `pip`:

```
$ sudo pip install virtualenvwrapper
```

Next, add the information to your bash profile.  Open `~/.bashrc` with the `nano` editor:

```
$ nano ~/.bashrc
```

Insert the following details at the bottom of the file.  Once this is complete, save and exit using `CTRL+X` and `Y`:

```
# virtualenv and virtualenvwrapper
export WORKON_HOM=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

Then, load the bash profile to finish installation:

```
$ source ~/.bashrc
```

For a more in depth guide on installing `virtualenvwrapper`, click [here](https://virtualenvwrapper.readthedocs.io/en/latest/command-ref.html)

## 7.) Creating the Virtual Environment

To create the virtual environment with `virtualenvwrapper`, we can use `mkvirtualenv`:

```
$ mkvirtualenv nano-env -p python3
$ workon nano-env
```

## 8.) Installing TensorFlow, Keras, NumPy, and SciPy

You will be required to install these packages in the virtual environment.  Make sure that you are currently working in the virtual environment which you created in the previous step.

First, install NumPy and Cython:

```
$ pip install numpy cython
```

If you encounter the error message below during installation, follow the troubleshooting guide [click here](documentation/troubleshooting/errors_installing_numpy.md).

```
ERROR: Could not build wheels for numpy which use PEP 517 and cannot be installed directly.
```

Check if NumPy has been installed correctly by running the following command.  Note, if no import error occurs, then NumPy has been installed correctly.

```
$ python -c 'import numpy as np; print(np.__version__)'
```

Next, you will need to install additional Python packages which Tensorflow requires:

```
$ pip install future==0.18.2 mock==3.0.5 h5py==2.10.0 keras_preprocessing==1.1.1 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11
```

You can now install TensorFlow from the NVIDIA website.  This version is specifically optimised for the Jeston Nano:

```
$ sudo pip install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow
```

Finally, install the Keras library and check that both Keras and TensorFlow have neen installed correctly - there should be no input errors after running the following:

```
# Install Keras
$ pip install keras

# Test Tensorflow and Keras
$ python
>>> import tensorflow
>>> import keras
>>> exit()
```

## 9.) Install OpenCV 4.5.0 on Jetson Nano

This section details how to install OpenCV with CUDA support - NVIDIA's CUDA set of libraries for working on the GPU.  Building the OpenCV 4.5.0 package requires more than 4GB of RAM, so you must configure a temporary swapfile on the microSD card.  To do this, run the following:

```
$ sudo apt-get update
$ sudo apt-get upgrade

# install nano  
$ sudo apt-get install nano

# install dphys-swapfile  
$ sudo apt-get install dphys-swapfile
# give the required memory size
$ sudo nano /etc/dphys-swapfile
```

Then, reboot your system:

```
$ sudo reboot
```

After the reboot, you will need to work on your virtual environment again and install the dependencies for OpenCV.  Note that, some of these dependencies may have alrady been installed.

```
# workon virtual environment
$ workon nano-env

# reveal the CUDA location  
$ sudo sh -c "echo '/usr/local/cuda/lib64' >> /etc/ld.so.conf.d/nvidia-tegra.conf"
$ sudo ldconfig

# third-party libraries  
$ sudo apt-get install build-essential cmake git unzip pkg-config  
$ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt-get install libgtk2.0-dev libcanberra-gtk*
$ sudo apt-get install python3-dev python3-numpy python3-pip
$ sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev
$ sudo apt-get install libtbb2 libtbb-dev libdc1394-22-dev
$ sudo apt-get install libv4l-dev v4l-utils
$ sudo apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
$ sudo apt-get install libavresample-dev libvorbis-dev libxine2-dev
$ sudo apt-get install libfaac-dev libmp3lame-dev libtheora-dev
$ sudo apt-get install libopencore-amrnb-dev libopencore-amrwb-dev
$ sudo apt-get install libopenblas-dev libatlas-base-dev libblas-dev
$ sudo apt-get install liblapack-dev libeigen3-dev gfortran
$ sudo apt-get install libhdf5-dev protobuf-compiler
$ sudo apt-get install libprotobuf-dev libgoogle-glog-dev libgflags-dev
```

You can now download OpenCV.  There are two packages which you will need, the basic release, and the additional contributions.

```
$ cd ~  
$ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.0.zip
$ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.0.zip
```

Next, unpack your downloaded files:


```
$ unzip opencv.zip
$ unzip opencv_contrib.zip
```

You can now rename your directories with more conventient names like `/opencv` and `opencv_contrib`.

```
$ mv opencv-4.5.0  opencv  
$ mv opencv_contrib-4.5.0  opencv_contrib
```

Make sure that you remove the downloaded zip files:

```
$ rm opencv.zip
$ rm opencv_contrib.zip
```

Before you build the library on the Jetson Nano, make a directory which will hold the build files:

```
$ cd ~/opencv  
$ mkdir build
$ cd build
```

Now, build the OpenCV libraries:

```
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr  \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
-D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
-D WITH_CUDA=ON \
-D CUDA_ARCH_BIN=5.3 \
-D CUDA_ARCH_PTX="" \
-D WITH_CUDNN=ON \
-D WITH_CUBLAS=ON \
-D ENABLE_FAST_MATH=ON \
-D CUDA_FAST_MATH=ON \
-D OPENCV_DNN_CUDA=ON \
-D ENABLE_NEON=ON \
-D WITH_QT=OFF  \
-D WITH_OPENMP=ON \  
-D WITH_OPENGL=ON \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=ON \
-D WITH_GSTREAMER=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D BUILD_TESTS=OFF \
-D WITH_EIGEN=ON \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D BUILD_opencv_python3=TRUE \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D BUILD_EXAMPLES=OFF ..
```

After this is complete, start the build with the following command.  Note that this takes a considerable amount of time (two hours in our experience).

```
$ make -j4
```

After successful compilation, you can remove old packages, and install new generated packages on your system's database.

```
$ sudo rm -r /usr/include/opencv4/opencv2
$ sudo make install  
$ sudo ldconfig

# cleaning (frees 300 KB)
$ make clean
$ sudo apt-get update
```

Also, make sure that you delete the swap file which you configured earlier:

```
# remove the swapfile 
$ sudo /etc/init.d/dphys-swapfile stop
$ sudo apt-get remove --purge dphys-swapfile
```

Next, you need to create a symbolic link from OpenCV's installation directory to the virtual environment:

```
# You should cd into the directory of your virtual environment.
# In this case, we have called it nano-env
$ cd ~/.virtualenvs/nano-env/lib/python3.6/site-packages/
$ ln -s /usr/local/lib/python3.6/site-packages/cv2/python3.6/cv2.cpython-36m-aarch64-linux-gnu.so cv2.so
```

Verify that OpenCV has been installed correctly.  If no import error occurs, and version '4.5.0' is outputted, then OpenCV has been installed correctly:

```
$ python -c 'import cv2; print(cv2.__version__)'
'4.5.0'
```

## 10.) Install Other Dependencies via `pip`

First, make sure that you are working on your virtual environment:

```
$ workon nano-dev
```

You can now install other required libraries:

```
$ pip install matplotlib
$ pip install pillow imutils
$ pip install dlib
$ pip install lxml progressbar2
```

## 11.) Installing `flirpy`

To install `flirpy`, clone the following repository.  For easy access, we recommend cloning the package into the `/home` directory:


```
$ git clone https://github.com/LJMUAstroecology/flirpy.git
```

To install the library, run the following:

```
$ cd flirpy
$ pip install .
```

If an error occurs during this stage, use the troubleshooting guide on the `flirpy` repository [(click here)](https://github.com/LJMUAstroEcology/flirpy).

## 12.) Setting up a Swapfile

To improve performence when running the facemask detector, you can create a swapfile:

```
$ sudo fallocate -l 8G /mnt/8GB.swap
$ sudo mkswap /mnt/8GB.swap
$ sudo swapon /mnt/8GB.swap
```

Add the following line to `/etc/fstab` and reboot to make sure that the swap space is mounted automatically:

```
/mnt/8GB.swap  none  swap  sw 0  0
```

Follow [using Jeston Nano environment](documentation/manual/environment_setup/using_jetson_nano_env.md) for a guide on using the Jetson Nano.

## References
- NVIDIA Developer. 2021. _Getting Started With Jetson Nano Developer Kit_. [online] Available at: <https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit> [Accessed 28 October 2020].
- Rosebrock, A., 2021. How to configure your NVIDIA Jetson Nano for Computer Vision and Deep Learning - PyImageSearch. [online] PyImageSearch. Available at: <https://www.pyimagesearch.com/2020/03/25/how-to-configure-your-nvidia-jetson-nano-for-computer-vision-and-deep-learning/> [Accessed 10 October 2020].
- Docs.nvidia.com. 2021. _Installing TensorFlow For Jetson Platform :: NVIDIA Deep Learning Frameworks Documentation_. [online] Available at: <https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html> [Accessed 1 November 2020].
- Qengineering.eu. 2021. _Install OpenCV 4.5 on Jetson Nano - Q-engineering_. [online] Available at: <https://qengineering.eu/install-opencv-4.5-on-jetson-nano.html> [Accessed 15 January 2021].
- Jkjung-avt.github.io. 2021. _Setting up Jetson Nano: The Basics_. [online] Available at: <https://jkjung-avt.github.io/setting-up-nano/> [Accessed 20 January 2021].