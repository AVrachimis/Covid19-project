"""tests model accuracy using the original dataset"""

import os
import argparse

import numpy as np  # pylint: disable=W0611

import tensorflow as tf
from tensorflow.keras.models import load_model

if __package__:  # when this script imported by parent scripts
    from .train_model import TYPE_DATASET, prepare_dataset  # pylint: disable=E0402
    from .face_predict_dnn import predict  # pylint: disable=E0402
else:           # when this script run directly
    from train_model import TYPE_DATASET, prepare_dataset
    from face_predict_dnn import predict

if __name__ == "__main__":
    ap = argparse.ArgumentParser()  # pylint: disable=C0103
    ap.add_argument("-d", "--dataset", required=True,
                    help="path to input dataset")
    ap.add_argument("-m", "--model", type=str,
                    default="mask_detector.model",
                    help="path to output face mask detector model")
    args = vars(ap.parse_args())  # pylint: disable=C0103

    DIR_DATASET = args["dataset"]
    DIR_MODEL = args["model"]
    FILENAME_RESULT = f"test_result_{os.path.split(DIR_MODEL)[-1]}.txt"
    if os.path.exists(FILENAME_RESULT):
        os.remove(FILENAME_RESULT)

    images, labels = prepare_dataset(DIR_DATASET, TYPE_DATASET)  # pylint: disable=C0103
    MODEL = load_model(DIR_MODEL)
    MODEL.summary()

    for img in images:
        image_byte = tf.io.read_file(img)
        image = tf.io.decode_image(image_byte, channels=3)

        prediction, _ = predict(image, MODEL)
        print("", img, TYPE_DATASET[prediction], end=". ")

    with open(FILENAME_RESULT, "a") as FILE_RESULT:
        print("Model: %s" % DIR_MODEL, file=FILE_RESULT)
        MODEL.summary(print_fn=lambda x: FILE_RESULT.write(x + '\n'))
