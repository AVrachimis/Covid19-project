"""
Runs mask detection
"""

import os
import argparse
import sys

from model_scripts.detect_video import capture
from model_scripts.detect_image import image_detect

if __name__ == "__main__":
    ap = argparse.ArgumentParser()  # pylint: disable=C0103
    ap.add_argument("-m", "--model", type=str,
                    default="mask_detector.model",
                    help="path to face mask detector model")
    ap.add_argument("-t", "--type", required=True, choices=["video", "image"],
                    help="video or image detection")
    ap.add_argument("-i", "--imagepath", default=None,
                    help="path of image to detect")

    args = vars(ap.parse_args())  # pylint: disable=C0103

    current_dir = os.path.dirname(os.path.realpath(__file__))  # pylint: disable=C0103

    if args["model"] not in os.listdir(current_dir):
        print("Invalid model path\nPlease try again")
        sys.exit(0)

    model_dir = os.path.join(current_dir, args["model"])  # pylint: disable=C0103

    if args["type"] == "video":
        capture(model_dir)
        sys.exit(0)

    image_path = os.path.join(current_dir, args["imagepath"])  # pylint: disable=C0103

    if not os.path.exists(image_path):
        print("Invalid image path\nPlease try again")
        sys.exit(0)

    image_detect(model_dir, image_path)
