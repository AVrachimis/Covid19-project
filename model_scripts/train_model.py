"""trains facemask detection model using MobileNetV2 as a base model"""

import os
import sys
import argparse
from glob import glob
import numpy as np  # pylint: disable=W0611

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from sklearn.model_selection import train_test_split

BATCH_SIZE = 5  # Num of Pics to Train each time
EPOCHS = 5  # Training Loop
INPUT_SHAPE = 224  # [96, 128, 160, 192, 224]
TYPE_DATASET = ['withMask', 'withoutMask', 'incorrectMask']


def preproc(filename, label):
    """preprocess image for training"""

    image_byte = tf.io.read_file(filename)
    image = tf.io.decode_image(image_byte, channels=3)
    image_resize = tf.image.resize_with_pad(image, INPUT_SHAPE, INPUT_SHAPE)
    image_norm = tf.cast(image_resize, tf.float32) / 255.0
    label_onehot = tf.one_hot(label, len(
        TYPE_DATASET), on_value=None, off_value=None)
    return image_norm, label_onehot


def make_dataset(images, labels):
    """make training dataset"""
    num = len(images)
    dataset = tf.data.Dataset.from_tensor_slices((images, labels))
    dataset = dataset.shuffle(num).repeat()
    # , num_parallel_calls=tf.data.experimental.AUTOTUNE)
    dataset = dataset.map(preproc)
    # .prefetch(tf.data.experimental.AUTOTUNE)
    dataset = dataset.batch(BATCH_SIZE)
    return dataset


def prepare_dataset(dir_dataset: str, type_dataset: list, img_ext="*.jpg"):
    """prepare dataset for training"""
    images = []
    labels = []
    for index, value in enumerate(type_dataset):
        this_type_dataset = value

        dir_mask = os.path.join(dir_dataset, this_type_dataset)
        f_mask = glob(os.path.join(dir_mask, img_ext))
        num_mask = len(f_mask)
        label_mask = [index]*num_mask

        images += f_mask
        labels += label_mask
    return images, labels


def train(dir_dataset, model_path):
    """training the model using MobileNetV2"""

    images, labels = prepare_dataset(dir_dataset=dir_dataset,
                                     type_dataset=TYPE_DATASET)

    (training_images, testing_images, training_labels, testing_labels) = train_test_split(
        images, labels, test_size=0.20, random_state=42)

    dataset_train = make_dataset(training_images, training_labels)
    dataset_vali = make_dataset(testing_images, testing_labels)

    # Create base model using MobileNetV2
    base_model = keras.applications.MobileNetV2(
        input_shape=(INPUT_SHAPE, INPUT_SHAPE, 3), include_top=False)
    model_output = Dense(len(TYPE_DATASET), activation='softmax')(
        Dense(1024, activation='relu')(
            GlobalAveragePooling2D()(base_model.output)
        )
    )
    model = keras.Model(inputs=base_model.input, outputs=model_output)

    # Freeze convolution
    for layer in base_model.layers:
        layer.trainable = False

    model.compile(loss='categorical_crossentropy',
                  optimizer='sgd',
                  metrics=['accuracy'])

    model.fit(dataset_train,
              steps_per_epoch=len(training_images)//BATCH_SIZE,
              epochs=EPOCHS,
              validation_data=dataset_vali,
              validation_steps=len(testing_images)//BATCH_SIZE,
              verbose=1)

    model.evaluate(dataset_vali, steps=len(
        testing_images)//BATCH_SIZE, verbose=1)

    model.save(model_path)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()  # pylint: disable=C0103
    ap.add_argument("-d", "--dataset", required=True,
                    help="path to input dataset")
    ap.add_argument("-m", "--model", type=str,
                    default="mask_detector.model",
                    help="path to output face mask detector model")
    args = vars(ap.parse_args())  # pylint: disable=C0103

    current_dir = os.path.dirname(os.path.realpath(__file__))  # pylint: disable=C0103
    parent_dir = os.path.dirname(current_dir)  # pylint: disable=C0103

    if args["dataset"] not in os.listdir(parent_dir):
        print("Invalid dataset folder name\nPlease try again")
        sys.exit(0)

    dataset_dir = os.path.join(parent_dir, args["dataset"])  # pylint: disable=C0103

    train(dataset_dir, args["model"])
