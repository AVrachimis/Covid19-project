# CS31 Main
## Project Summary

#### Computer vision solution to mitigate COVID-19 risks and enhance the workplace and public safety

The project goal is to develop an application which could be used to help workplaces or public safety as a response to covid 19. This will be done through a range of technologies including :

1. Face mask detection on a person.
2. Measurement of a person temperature before accessing a building or office.
3. Facial recognition before a person can access a building. 
	- This is not a required requirement however we would like to look at this if we have enough time.

## Running the scripts
### ``resize.py``
The resize script resizes an image while keeping the aspect ratio of the image the same.

Run the script in the ``cs31-main`` folder. This will output the resized image into a new folder called ``resized_images`` with the path ``cs31-main/resized_images``.

The resize script takes various arguments including ``--image``, 	``--folder`` and ``--width`` .

#### The program requires either ``--image`` or ``--folder`` for the input images.
#### ``--image``
Allows the program to resize a single image, with the argument value equaling the path of the image. This will only work for a single image file such as jpg, png, jpeg etc..

#### ``--folder``
Allows the program to resize a batch of images, with the argument's value equaling the path of a folder of images. All files in this folder must be an image.

#### The program also requires ``--width`` for the new width of the resized image
#### ``--width``
The argument value equals the new width size. This is a required argument and the program will not run without it.

An example execution starting in the cs31-main directory:
``python .\dataset_scripts\resize.py --folder  .\faces\ --width 500``

#

### ``artifical_facemask.py``
The artificial facemask script artificially places a mask on an image. This will be used while creating our artificial dataset.

Run the script in the ``cs31-main`` folder. This will output the new image into a new folder either called  ``correct_mask`` or ``incorrect_mask``. This depends on the type of image which the artificial facemask is producing. All of these folders would be in the ``cs31-main`` folder.

The script takes various arguments including ``--image``, ``--folder``, ``--type``, ``--mask``, ``--label`` and ``--dataset``.

#### The program requires either ``--image`` or ``--folder`` for the input images.
This works the same way as the ``resize.py`` script.

#### The program requires ``--type`` for the type of image the program will produce
The argument value equals a choice between three values. The options are.

 - ``correct``: This will artificially place a face mask in the correct position. The output image will be added to the ``correct_mask`` folder.
 - ``nose``: This will artificially place a face mask below the nose. The output image will be added to the ``incorrect_mask`` folder.
 - ``chin``: This will artificially place a face mask on the chin. The output image will be added to the ``incorrect_mask`` folder.

This is a required argument and the program will not run without it.

#### The program requires ``--mask`` for the input mask which you would like to overlay on the face
The path to the input mask image file.

This is a required argument and the program will not run without it.

#### The program requires ``--label`` for the input mask label points
The path to a csv file with the label points for the mask. You can use tools such as https://www.makesense.ai/ to generate this file.

This is a required argument and the program will not run without it.

#### The program requires ``--dataset`` for the output location of the artifical mask image
The path to the output image file. If path doesn't exist already, the script will create the directory for you.

This is a required argument and the program will not run without it.


An example execution starting in the cs31-main directory:
``python dataset_scripts/artifical_facemask.py --image faces/image.jpg --type nose --mask dataset_scripts/resources/black_mask/mask.png --labels dataset_scripts/resources/black_mask/facemask_labels.csv --dataset face_dataset``

### ``rename_images.py``
The rename images script renames the images names of the given folder. 

Run the script in the ``cs31-main/dataset_scripts`` folder. 

#### The script takes 2 required arguments, the dataset folder and the folder name of the images you want to rename 
For the second argument, you have to type one of the three images categories. The options are: 

- ``withMask``      : It renames all the images withing the withMask folder in the following format:     ``mask-0001.jpg``           
- ``withoutMask``   : It renames all the images within the withoutMask folder in the following format:   ``no-mask-0001.jpg``        
- ``incorrectMask`` : It renames all the images within the incorrectMask folder in the following format: ``incorrect-mask-0001.jpg`` 

An example execution in the cs31-main/dataset_scripts directory:  ``python rename_images.py dataset withMask``

### ``train_model.py``
The script to train mask detection model.
- ``-m MODEL``		: directory of trained model will be saved in the following format:	``mask_detector.model``
- ``-d DATASET``	: directory of dataset with mask in the following format:			``dataset``

An example execution in the cs31-main directory:  ``python ./model_scripts/train_model.py -d dataset``

### ``test_model.py``
The script to test mask detection model.
- ``-m MODEL``		: directory of trained model to load in the following format:	``mask_detector.model``
- ``-d DATASET``	: directory of dataset with mask in the following format:			``dataset``

An example execution in the cs31-main directory:  ``python ./model_scripts/test_model.py -d dataset -m mask_detector.model``

### ``mask_detection.py``
The script to run entire face mask detection.

Run the script in the ``cs31-main`` folder. 

#### The script requires at least one argument however there are other optional arguments available.

- ``-m MODEL``		: (optional - will default to mask_detector.model) directory of trained model will be saved in the following format:	``mask_detector.model``
- ``-t TYPE``	: (required - has to be a option between (``video``,``image``)) You have a choice to run the facemask detection algorithm on a single image or a live video feed. 
- ``-i IMAGEPATH`` : Only required when running the facemask detection algorithm on a single image. An example format is: 	``dataset/incorrectMask/incorrect-mask-0001.jpg``

An example execution for a video in the cs31-main directory: ``python mask_detection.py -t video``
An example execution for a image in the cs31-main directory: ``python mask_detection.py -t image -i dataset/withMask/mask-0955.jpg``

