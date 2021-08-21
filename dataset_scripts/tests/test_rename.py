"""tests rename script"""
import os
import pytest
from dataset_scripts.rename_images import rename_image

@pytest.fixture
def get_test_images_dir():
    """Gets the path of the test_image_dir"""
    test_images_dir = "dataset_scripts/tests/testDataset"
    return test_images_dir


def test_incorrect_mask(get_test_images_dir):  # pylint: disable=W0621
    """Renames images in the test_image_dir to incorrect mask naming scheme"""
    rename_image(get_test_images_dir, "incorrect-mask-")

    result = os.listdir(get_test_images_dir)
    assert result[0] == "incorrect-mask-0001.jpg"
    assert result[1] == "incorrect-mask-0002.jpg"


def test_with_mask(get_test_images_dir):  # pylint: disable=W0621
    """Renames images in the test_image_dir to with mask naming scheme"""
    rename_image(get_test_images_dir, "mask-")

    result = os.listdir(get_test_images_dir)
    assert result[0] == "mask-0001.jpg"
    assert result[1] == "mask-0002.jpg"


def test_without_mask(get_test_images_dir):  # pylint: disable=W0621
    """Renames images in the test_image_dir to no mask naming scheme"""
    rename_image(get_test_images_dir, "no-mask-")

    result = os.listdir(get_test_images_dir)
    assert result[0] == "no-mask-0001.jpg"
    assert result[1] == "no-mask-0002.jpg"
