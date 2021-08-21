# Errors while Training the Model

## Overview

If you encounter the error below, follow this troubleshooting guide to fix the issue.

## Potential Issues

If you are offline or under LAN and require a proxy to connect, you can prepare the MobileNetV2 model before you begin training:

First, download MobileNetV2 model from [here](https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5) or follow the steps for your OS below.

#### **Linux:**

Run the following command in a terminal:

```
$ wget https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5
$ mv *.h5 ~/.keras/models/
```

#### **Windows:**

Download the pre-trained model [here](https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5).

Then, move the downloaded file into your `/home` directory. Your path should be `/home/.keras/models`.