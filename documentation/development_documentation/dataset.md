# Dataset Documentation

## Overview

Our dataset was collated through various sources to ensure that our model was robust.  We accomplished this by including images with varying light exposure, mask styles and colours, and face angles.  We also had to ensure that all images were of the same quality and file format; we decided that JPG would be the best option as it performs better for photorealistic images, whereas PNG is more suitable for drawings with sharp lines and solid colours.  The dataset has been constantly improved during the development process due to issues with our detection algorithm.

We are using the dataset to i.) detect individuals wearing - or not wearing - a face mask, ii.) detect correct or incorrect face mask placement.  It was also essential that we include people from all age groups, ethnicities, and genders, to reflect the entire population.

In total, our dataset consists of 3,600 images, with 1,200 images of each type:
* Correct mask.
* Incorrect mask.
* Without mask

## Sources

To develop an effective model, the dataset must be created, in such a way, so that it accurately represents the whole population.  We decided to collect images from various open-source datasets which are used for similar purposes.  This guarantees that our images are of sufficient quality and format to train and test our model.  Details of each are given below.

* MaskedFace-Net:
  * MaskedFace-Net -- A Dataset of Correctly/Incorrectly Masked Face Images in the Context of COVID-19: [link](https://arxiv.org/abs/2008.08016).
  * Dataset source: [link](https://github.com/cabani/MaskedFace-Net).
* Flickr-Faces-HQ:
  * Dataset source: [link](https://github.com/NVlabs/ffhq-dataset).
* Face-Mask-Detector:
  * Dataset source: [link](https://github.com/chandrikadeb7/Face-Mask-Detection).

#### **MaskedFace-Net**

This dataset comprises of over 130,000 (1024x1024) images of human faces with correctly and incorrectly worn face masks (artificially placed).  This distinction is split into four categories of face mask placement:
* Correctly masked.
* Incorrectly masked: uncovered chin.
* Incorrectly masked: uncovered nose.
* Incorrectly masked: uncovered nose and mouth.

We have incorporated similar image classifications to ensure that we have an even spread of face mask placements.

This dataset is based on the Flickr-Faces-HQ collection which we also utilised for our solution.

#### **Flickr-Faces-HQ**

This dataset was used in conjunction with MaskedFace-Net to include images of individuals not wearing any face mask.  It consists of 70,000 images which are of the same quality as dataset mentioned above (1024x1024).  However, the dataset has images in PNG format, so we had to convert them to JPG before we could use them in our solution.

#### Face-Mask-Detection

This repository contains a total of 4,095 images; 2,165 with a face mask;  and 1,930 without a face mask.  Unlike the previously mentioned MaskedFace-Net collection, this dataset contains real face masks instead of being artificially placed.

The source of this dataset states that the images were collected using:
* A Bing web scraper created using Python.
* Kaggle datasets.
* RMFD dataset.

This repository also states that this dataset was used to develop a face mask detector using MobileNetV2 architecture for deployment on low-cost embedded systems (Raspberry Pi, Google Coral, etc.).

This dataset was introduced later in development to resolve issues with our detection algorithm, where it could not detect correct mask placement for individuals wearing darker face masks.  The inclusion of this dataset fixed this issue and additionally increased the overall confidence level of the algorithm.

## Dataset Folder Structure

Dataset folder structure has been kept as simple as possible with three folders named with_mask, incorrect_mask, and without_mask.  The images inside the folder are named appropriately, using a rename script created.  This rename script converts all image names to adhere to the following naming convention: "mask-001", "mask-002", ..., "mask-nnn".

#### **Data Gathering Process and Data Normalization**

Initially, around 300 images for each type have been added to the dataset constructing the foundations of it. Due to the lack of resources when it comes to the incorrect mask images, an artificial face mask script has been created which places a mask artificially either on the chin, below nose or correctly. Half of the images on the incorrect mask folder are created from the artificial face mask script, while the other half are found through the resources aforementioned. 

Focusing on the quality of our dataset, we wanted to make sure that all the images are carefully selected, maximizing the accuracy of our model. That is where the resize script has been created, resizing all the images of the dataset keeping their aspect ration the same, while making sure that all the images are at least 800x800. Bad quality images not satisfying our standards, have been discarded and replaced with higher quality images. At this point more images have been added to the dataset, having approximately 800 images for each type. A bigger variety of face masks have been added into the dataset, also including peoples wearing glasses, hats, and helmets.  

Finalizing the dataset, exactly 1200 images have been collected into each type of image. With the number of images collected, we managed to achieve a generalization of our model and therefore avoiding any type of over learning. 

## Licenses and References

Full details of each dataset's licenses can be found by navigating to the source links (see Sources).

#### **MaskedFace-Net**

This dataset is made available under Creative Commons BY-NC-SA 4.0 license by NVIDIA Corporation, which allows free use, redistribution, and adaptation for non-commercial purposes as long as appropriate credit is given to each author, details of which are given below.

Cabani, A., Hammoudi, K., Behnabiles, H., and Melkemi, M.  (2020).  *MaskedFace-Net - A dataset of correctly/incorrectly masked face images in the context of COVID-19*.  Smart Health.  ISSN 2352-6482.  Found [here](https://doi.org/10.1016/j.smhl.2020.100144).

Hammoudi, K., Cabani, A., Benhabiles, H., and Melkemi, M.  (2020).  *Validating the correct wearing of protection mask by taking a selfie: design of a mobile application "CheckYourMask" to limit the spread of COVID-19*.  CMES-Computer Modelling in Engineering & Sciences.  Vol 124, No. 3.  pp 1049-1059.  Found [here](DOI:10.32604/cmes.2020.011663).

#### **Flickr-Faces-HQ**

The individual licenses were published in Flickr by their respective authors under either Creative Commons BY 2.0, Creative Commons BY-NC, Public Domain Mark 1.0, Public Domain CC0 1.0, or U.S. Government Works license.  All of which allow free use, redistribution, and adaptation for non-commercial purposes.

Details of the author's work can be found below:

Karras, T., Laine, S., Aila, T. (2019). *A Style-Based Generator Architecture for Generative Adversarial Networks*.  Cornel University.  Found [here](https://arxiv.org/abs/1812.04948).

#### **Face-Mask-Detection**

This dataset is made available through the MIT License, allowing us to reuse the model and dataset without restriction, including without limiting the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

Deb, C. (2020).  *Face-Mask-Detection - Face Mask Detection system built with OpenCV, Keras/TensorFlow using Deep Learning and Computer Vision concepts in order to detect face masks in static images as well as in real-time video streams*.  Found [here](https://github.com/chandrikadeb7/Face-Mask-Detection).
