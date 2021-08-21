"""opens image and detects mask in the image"""

import numpy as np  # pylint: disable=W0611
import cv2
import imutils

from tensorflow.keras.models import load_model
from .face_predict_dnn import detect_face  # pylint: disable=E0402

def image_detect(model_dir, image_path, label_function=detect_face):
    """
    Detects mask in a image and displays results

    @param: label_function: Function to label the frame read from webcam,
            return 3d(height,width,depth) nparray frame.
    """

    image = cv2.imread(image_path)

    # Load the model
    model = load_model(model_dir)

    labelled_frame = label_function(model, image)

    resized_frame = imutils.resize(labelled_frame, width=500)

    cv2.imshow('Facemask Prediction', resized_frame)

    # add wait key. window waits till user press any key
    cv2.waitKey(0)

    # destroy all windows
    cv2.destroyAllWindows()
