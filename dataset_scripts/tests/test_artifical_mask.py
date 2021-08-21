"""
tests artificial facemask script
"""
import os
import pytest
import cv2
#import numpy as np

from dataset_scripts.resize import resize_image
import dataset_scripts.artificial_facemask as artificial_facemask

@pytest.fixture
def input_face_image():
    """Open test_image.png file using cv2"""
    image = cv2.imread("dataset_scripts/tests/testImages/test_face1.jpg")
    image = resize_image(image, 500)

    return image


@pytest.fixture
def face_landmarks(input_face_image):  # pylint: disable=W0621
    """Converts image to gray and returns the face landmarks for that image"""
    gray_img = cv2.cvtColor(src=input_face_image, code=cv2.COLOR_BGR2GRAY)
    landmarks = artificial_facemask.face_detector(gray_img)

    return landmarks


@pytest.fixture
def src_pnts():
    """Open facemask src points and returns them"""
    _src_pnts = artificial_facemask.open_csv_file("dataset_scripts/tests/testResources/facemask_labels.csv")  # pylint: disable=C0301
    return _src_pnts


@pytest.fixture
def dest_pnts(face_landmarks):  # pylint: disable=W0621
    """Returns facemask dest_pnts"""
    wear_mask_landmarks = [29, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 2]

    _dest_pnts = artificial_facemask.mask_landmarks(face_landmarks, wear_mask_landmarks)

    return _dest_pnts


def test_ensure_dir():
    """Checks if ensure_dir checks that dir exists"""
    path = f"{os.getcwd()}/test_dir"
    artificial_facemask.ensure_dir(path)

    if os.path.exists(path):
        os.rmdir(path)
        assert True
    else:
        assert False


def test_open_csv_file(src_pnts):  # pylint: disable=W0621
    """Checks that the open_csv_file opens and returns the correct number of scr_pnts"""
    assert src_pnts.shape == (12, 2)


def test_mask_landmarks(dest_pnts):  # pylint: disable=W0621
    """Checks that the mask_landmarks returns the correct number of dest_pnts"""
    assert dest_pnts.shape == (12, 2)


def test_overlay(dest_pnts, src_pnts, input_face_image):  # pylint: disable=W0621
    """Checks that the mask is overlayed correctly on face"""

    output_image = artificial_facemask.overlay_mask(src_pnts, dest_pnts, input_face_image,
                                                    "dataset_scripts/tests/testImages/mask.png")
    result_image = cv2.imread("dataset_scripts/tests/testImages/test_face1_correct.jpg")

    result = output_image.all() == result_image.all()

    assert result


def test_setup_mask_image():
    """Check if setup_mask_image opens image correctly"""

    image = artificial_facemask.setup_mask_image("dataset_scripts/tests/testImages/mask.png")

    assert image.shape == (347, 500, 4)


def test_setup_face_image():
    """Check if setup_face_image opens image correctly"""

    image, _ = artificial_facemask.setup_face_image("dataset_scripts/tests/testImages/test_face1.jpg")  # pylint: disable=C0301

    assert image.shape == (330, 500, 3)
