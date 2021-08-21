# Further Optimisation

## Overview

This document outlines our experience with optimising our facemask detection algorithm.  Given the time constraints, our final solution is not the most robust against all environments or conditions, however, we actively tried to optimise our model throughout the development process, to ensure that we develop a suitable algorithm.

## Optimising the Algorithm

We were hoping to optimise the facemask detector into a TensorRT accelerated engine.

#### **Expected Procedure**

1. Training the model through our dataset and model structure by Tensorflow
2. Convert Keras model *(.h5)* into TensorRT accelerated engine *(.trt)*
3. Deploy engine *(.trt)* by Python and do the live prediction.

## Current Problems

This section details the current issues with potential optimisations as well as outline potential solutions which could be employed, if this project is to be developed for commercial purposes.

#### **Lack of Guidlines**

There is a distinct lack of documentation from NVIDIA and Tensorflow, and other third-party blogs (e.g., StackOverflow).  More research would need to be conducted to find suitable APIs from TensorFlow and TensorRT (other other packages) in order to develop the algorithm.  Obviously, given the time constraints of the project, this is not possible.

#### **Differing TensorFlow Versions**

The version of TensorFlow that we use is `2.4.0`, which was the latest release when we began development.  This has since been updated to `2.4.1` and incorporates significant changes, meaning that we would have to make considerable alterations if we were to update the package.

For instance, we would need to use the `keras2onnx` Python package to convert the Keras model into an Onnx model.  However, this currently only supports version `2.3.1` of TensorFlow.  This is not made clear during installation, and resulted in several warnings and errors during execution.  Furthermore, this is not mentioned in NVIDIA's official guidelines (at the time of writing this).

In conjunction, online documentation also does not mention which version of TensorFlow they use, so it is very difficult to explicitly follow their guides.  There are, however, a lot of guidelines relating to TensorRT acceleration, which could be used to optimise the algorithm.

#### **System Support:**

TensorFlow is not extensively supported on Windows when using Python.  Linux, however, is the best choice, specifically Ubuntu versions `16.04` to `18.04`.

#### **Driver Combination:**

According to the NVIDIA website and TensorFlow official, to install the GPU accelerator version of TensorFlow, we must install the CUDA Toolkit.  This depends on the NVIDIA GPU Drivers and the cuDNN library, which is used alongside TensorRT.  However, the given Docker image is not compatible as it would need CUDA and Graphic Drivers to be installed.

Different versions of TensorFlow would also require specific versions of CUDA, cuDNN, and Graphic Drivers.  This means that each time we installed another version of TensorFlow, we needed to reinstall past versions of drivers.  The simplest way to do this is to directly reinstall the OS.  The drivers are also currently quite unstable, forcing us to restart our systems very frequently.

TensorFlow also appears to have some dependencies with CUDA as sometimes it will indicate that it cannot find a specific CUDA library, which means the GPU accelerator will not be used.

#### **TensorRT:**

The optimal way of using TensorRT to accelerate the prediction is to reduce the precision of the model and solidification (such as, reduce from FP32 to FP16/8), and pre-calculate the variables.

As we have tested so far, if the precision of the input shape is reduced - (224,244,3) to (96,96,3) - the accuracy will not be adequate.

The latest version of TensorRT is `7.2.2` which is not a `GA` release, meaning it is quite unstable.  Unfortunately, as of writing this, this is the only version supporting CUDA 11.2.

Finally, the TensorRT accelerated engine is more suitable for predicting large batches of data.  For the purposes of this system, this is very unlikely to occur, so increasing the batch size would be unecessary.
