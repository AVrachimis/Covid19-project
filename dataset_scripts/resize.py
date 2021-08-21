"""
Resize image or a folder of images
"""
import argparse
import os
import cv2


def resize_image(image, new_width):
    """Resizes image with the width new_width keeping the aspect ratio"""
    (height, width, dim) = image.shape
    del dim
    ratio = new_width / width
    dim = (new_width, int(height * ratio))
    return cv2.resize(image, dim)


def ensure_dir(image_path):
    """Checks if dir exists at path, if not it create a new directory with the path vairable"""

    if not os.path.exists(image_path):
        os.mkdir(image_path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()  # pylint: disable=C0103

    parser.add_argument('--image')

    parser.add_argument('--folder')

    parser.add_argument('--width', required=True)

    args = parser.parse_args()  # pylint: disable=C0103

    # Checks if user has given either a image or folder
    if (args.folder is None and args.image is None):
        raise Exception(
            "Please specify the image or folder with --image or --folder")

    path = f"{os.getcwd()}/resized_images"  # pylint: disable=C0103

    # Checks if dir exists if not creates the dir
    ensure_dir(path)

    if args.folder:
        # runs the program for a folder of images
        for filename in os.listdir(f"{os.getcwd()}/{args.folder}"):
            print(filename)
            input_image = cv2.imread(f"{args.folder}/{filename}")
            output_image = resize_image(input_image, int(args.width))
            cv2.imwrite(f"{path}/{filename}", output_image)
    else:
        # runs the program for a single image
        input_image = cv2.imread(args.image)  # pylint: disable=C0103

        output_image = resize_image(input_image, int(args.width))  # pylint: disable=C0103

        filename = (args.image).split("/")[-1]  # pylint: disable=C0103

        print(f"{path}/{filename}")
        cv2.imwrite(f"{path}/{filename}", output_image)
