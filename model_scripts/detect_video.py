"""gets frame and detects mask in the frame"""

import numpy as np  # pylint: disable=W0611
import cv2

from flirpy.camera.lepton import Lepton
from tensorflow.keras.models import load_model
from .face_predict_dnn import detect_face  # pylint: disable=E0402


def ktoc(val):
    """Converts numpy array from kelvin to celsius"""
    return val * 0.03376883363105676 + -242.32713221114128


def capture(model_dir, label_function=detect_face, quit_key="q"):
    """
    Detects mask in a live video feed

    @param: label_function: Function to label the frame read from webcam,
            return 3d(height,width,depth) nparray frame.

    @param: quit_key: Press 'q' to stop capture.
    """

    video_capture = cv2.VideoCapture(0)
    camera = Lepton()

    window_name = "Facemask Prediction"

    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(
        window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Load the model
    model = load_model(model_dir)

    error_message = True

    while True:

        frame = video_capture.read()[-1]

        # Gets camera frame from Lepton
        lepton_frame_c_resized = None

        # Grabs camera if lepton is connected, else a error message is printed to console

        try:
            lepton_frame = camera.grab()
            lepton_frame_c = ktoc(lepton_frame)

            if lepton_frame_c is not None:
                lepton_frame_c_resized = cv2.resize(
                    lepton_frame_c, frame.shape[:2])

            error_message = True
        except ValueError:
            if error_message:
                print("No lepton camera connected")
                print("Continuing without lepton")
                error_message = False

        key = cv2.waitKey(1)
        labelled_frame = label_function(model, frame, lepton_frame_c_resized)

        cv2.imshow(window_name, labelled_frame)

        if key == ord(quit_key) or key == 27:  # press Q or Esc for exit
            break

    video_capture.release()
    camera.close()
    cv2.destroyAllWindows()
