"""tests resize script"""
import pytest
import cv2
from dataset_scripts.resize import resize_image

@pytest.fixture
def input_image():
    """Open test_image.png file using cv2"""
    image = cv2.imread("dataset_scripts/tests/testImages/test_image.png")
    return image


def test_resized_image_width(input_image):  # pylint: disable=W0621
    """Checks if image has been resized with a width of 1000"""
    resized_image = resize_image(input_image, 1000)
    assert resized_image.shape[1] == 1000


def test_resized_image_height(input_image):  # pylint: disable=W0621
    """Checks if image has been resized with correct aspect ratio"""
    resized_image = resize_image(input_image, 150)
    assert resized_image.shape[0] == 80
