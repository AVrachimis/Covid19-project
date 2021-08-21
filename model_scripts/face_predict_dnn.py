""" Detects face in frame and then predicts if users face is wearing
    a facemask correctly, incorrectly or not at all """

import numpy as np
import cv2
import os  # pylint: disable=C0411

import tensorflow as tf

if __package__:
    from .train_model import INPUT_SHAPE  # pylint: disable=E0402
else:
    from train_model import INPUT_SHAPE

# pre-load face net
MODELFILE = os.path.join(os.path.dirname(
    __file__), "resources/res10_300x300_ssd_iter_140000.caffemodel")
CONFIGFILE = os.path.join(os.path.dirname(
    __file__), "resources/deploy.prototxt")
NET = cv2.dnn.readNetFromCaffe(CONFIGFILE, MODELFILE)


def predict(face, model):
    """Predicts if face is wearing a face mask corrctly, incorrectly, not at all"""

    image_resize = tf.image.resize_with_pad(face, INPUT_SHAPE, INPUT_SHAPE)
    image_norm = tf.cast(image_resize, tf.float32) / 255.0
    image_norm = np.expand_dims(image_norm, axis=0)

    prediction = model.predict(image_norm)

    i = prediction.argmax(axis=1)[0]

    return i, prediction[0][i]


def detect_face(model, frame, lepton_frame_c, cascade=NET):  # pylint: disable=R0914
    """Detect face in image and runs mask prediction algorithm on face.
       Returns frame with with a box of the face and mask prediction results"""

    # the height and width of the frame
    height, width = frame.shape[:2]

    # save a copy for prediction
    frame_raw = frame.copy()

    blob = cv2.dnn.blobFromImage(cv2.resize(
        frame, (300, 300)), 1.0, (300, 300), (104.0, 117.0, 123.0))
    cascade.setInput(blob)
    faces = cascade.forward()

    # to predict mask on face bounding box
    for i in range(faces.shape[2]):
        # get the confidence of the prediction
        confidence = faces[0, 0, i, 2]

        # if confidence is greater that 50%
        if confidence > 0.5:

            # computes the coordinates of the bounding box
            box = faces[0, 0, i, 3:7] * \
                np.array([width, height, width, height])
            (x_coord, y_coord, x1_, y1_) = box.astype("int")

            # checks that the bounding boxes fall in the frame
            x_coord, y_coord = (max(0, x_coord), max(0, y_coord))
            x1_, y1_ = (min(width - 1, x1_), min(height - 1, y1_))

            face_frame = frame_raw[y_coord: (
                y_coord+y1_), x_coord: (x_coord + x1_)]

            # checks face frame shape is valid
            if face_frame.shape == (0, 0, 3):
                continue
            try:
                prediction, accuracy = predict(face_frame, model)
            except ValueError:
                # if a error occurs with input frame, skip to the next frame
                continue

            accuracy = "{:.2f}%".format(accuracy*100)

            if prediction == 0:  # with mask
                colour = (0, 255, 0)

                text = "Wearing mask    {}".format(accuracy)
            elif prediction == 1:  # without mask
                colour = (255, 0, 0)
                text = "Not wearing mask    {}".format(accuracy)
            elif prediction == 2:  # incorrect mask
                colour = (0, 0, 255)
                text = "Wearing mask incorrectly    {}".format(accuracy)

            # Gets maximum temp from face bounding box
            if lepton_frame_c is not None:
                lepton_frame_resized_box = lepton_frame_c[x_coord:x1_, y_coord:y1_]

                max_temp = lepton_frame_resized_box.max()

                if max_temp >= 38:
                    temp_text = "\n High temp    {:.1f}% degree Celsius".format(
                        max_temp)
                else:
                    temp_text = "\n{:.1f} degree Celsius".format(max_temp)
            else:
                temp_text = ""

            # Adds temp text to prediction text

            text += temp_text

            # Draw a rectangle around face
            frame = cv2.rectangle(
                frame, (x_coord, y_coord), (x1_, y1_), colour, 2)
            # Prediction text
            for i, txt in enumerate(text.split('\n')):  # pylint: disable=W0621
                cv2.putText(img=frame,
                            text=txt,
                            org=(x_coord, (i-2)*28+(y_coord+10)),
                            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                            fontScale=1,
                            color=colour,
                            thickness=2
                            )

    return frame
