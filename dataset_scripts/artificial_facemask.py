"""
Artificially placing a face mask on a face
"""
import csv
import os
import sys
import argparse
import dlib
import numpy as np
import cv2

if __package__ is None or __package__ == '':
    # uses current directory visibility
    from resize import resize_image
else:
    # uses current package visibility
    from .resize import resize_image


def setup_face_image(face_image_path):
    """Opens the face image and resizes the image to a width of 500.
       Returns a gray and BGR version of the image"""
    img = cv2.imread(face_image_path)

    img = resize_image(img, 500)

    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    img = img.astype(np.float32) / 255.0

    return img, gray


def setup_mask_image(mask_dir):
    """Reads in mask image"""
    mask_img = cv2.imread(mask_dir, cv2.IMREAD_UNCHANGED)

    mask_img = mask_img.astype(np.float32) / 255.0

    return mask_img


def overlay_mask(src_pnts, dest_pnts, output_img, mask_dir):
    """Overlays the mask onto a face. The mask image will be transformed
       to fit the face. Output image is returned."""

    # load mask image
    mask_image = setup_mask_image(mask_dir)

    # get the perspective transformation matrix
    transformation_matrix, _ = cv2.findHomography(src_pnts, dest_pnts)

    # transformed masked image to required size
    transformed_mask = cv2.warpPerspective(mask_image,
                                           transformation_matrix,
                                           (output_img.shape[1], output_img.shape[0]),
                                           None,
                                           cv2.INTER_LINEAR,
                                           cv2.BORDER_CONSTANT,
                                           )

    # overlay mask on face
    alpha_mask = transformed_mask[:, :, 3]
    alpha_image = 1.0 - alpha_mask

    for i in range(0, 3):
        output_img[:, :, i] = (
            alpha_mask * transformed_mask[:, :, i]
            + alpha_image * output_img[:, :, i]
        )
    return output_img


def mask_landmarks(face_landmarks, wear_mask_landmarks):
    """Returns the position of the mask landmarks on the face as a numpy array"""

    dest_pnts = []

    for landmark in wear_mask_landmarks:
        dest_pnts.append(np.asarray([face_landmarks.part(
            landmark).x, face_landmarks.part(landmark).y]),)

    dest_pnts = np.array(dest_pnts, dtype="float32")

    return dest_pnts


def open_csv_file(label_dir):
    """Opens the mask landmarks file and returns them as a numpy array"""

    with open(label_dir) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        src_pnts = []
        for row in csv_reader:
            # skip head or empty line if it's there
            try:
                src_pnts.append(np.array([float(row[1]), float(row[2])]))
            except ValueError:
                continue
    src_pnts = np.array(src_pnts, dtype="float32")
    return src_pnts


def face_detector(gray):
    """Detects face landmarks and returns them"""
    detector = dlib.get_frontal_face_detector()

    predictor = dlib.shape_predictor(
        "dataset_scripts/resources/shape_predictor_68_face_landmarks.dat")

    faces = detector(gray)

    for face in faces:
        # Look for landmarks
        landmarks = predictor(image=gray, box=face)
        # Return landmarks for first face found only
        return landmarks


def artifical_facemask(wear_mask, face_image, gray, mask_dir, label_dir):
    """Helper function to call required functions"""

    face_landmarks = face_detector(gray)

    # No face has been detected
    if face_landmarks is not None:

        dest_pnts = mask_landmarks(face_landmarks, wear_mask)
        src_pnts = open_csv_file(label_dir)

        return overlay_mask(src_pnts, dest_pnts, face_image, mask_dir)
    return "None"


def correct_face_mask(image_to_process, mask_dir, label_dir):
    """main function for adding a mask correctly to a image"""

    wear_mask_landmarks = [29, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 2]
    face_img, gray = setup_face_image(image_to_process)
    return artifical_facemask(wear_mask_landmarks, face_img, gray, mask_dir, label_dir) * 255


def incorrect_face_mask_nose(image_to_process, mask_dir, label_dir):
    """main function for adding a mask incorrectly - not on the nose - to a image"""

    wear_mask_landmarks = [66, 14, 12, 11, 10, 9, 8, 7, 6, 5, 4, 2]
    face_img, gray = setup_face_image(image_to_process)
    return artifical_facemask(wear_mask_landmarks, face_img, gray, mask_dir, label_dir) * 255


def incorrect_face_mask_underchin(image_to_process, mask_dir, label_dir):
    """main function for adding a mask incorrectly - under the chin - to a image"""
    wear_mask_landmarks = [57, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3]
    face_img, gray = setup_face_image(image_to_process)
    return artifical_facemask(wear_mask_landmarks, face_img, gray, mask_dir, label_dir) * 255


def ensure_dir(dir_path):
    """Checks if dir exists at path, if not it create a new directory with the path vairable"""

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)


def check_path(path_dir):
    """Checks if path exists. If path doesn't exit a exception will be raised"""

    if not os.path.exists(path_dir):
        raise Exception(f"No file or folder with the path {path_dir} exists")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()  # pylint: disable=C0103

    parser.add_argument('--image', help="Input image")

    parser.add_argument('--folder', help="Input folder")

    parser.add_argument('--type', dest='format', choices=["correct", "nose", "chin"],
                        required=True, help="Type of output the program will produce")

    parser.add_argument('--mask', required=True, help="Mask image")

    parser.add_argument('--labels', required=True,
                        help="Mask labels csv files")

    parser.add_argument('--dataset', required=True,
                        help="Output dataset folder")

    args = parser.parse_args()    # pylint: disable=C0103

    fmt = args.format    # pylint: disable=C0103

    check_path(args.mask)
    check_path(args.labels)
    ensure_dir(args.dataset)

    # Checks if user has given either a image or folder
    if (args.folder is None and args.image is None):
        raise Exception(
            "Please specify the image or folder with --image or --folder")

    # Check which type of image to produce
    if fmt == 'correct':
        PATH = f"{os.getcwd()}/{args.dataset}/withMask"
        ARTIFICIAL_FACEMASK = correct_face_mask
    elif fmt == 'nose':
        PATH = f"{os.getcwd()}/{args.dataset}/incorrectMask"
        ARTIFICIAL_FACEMASK = incorrect_face_mask_nose
    elif fmt == 'chin':
        PATH = f"{os.getcwd()}/{args.dataset}/incorrectMask"
        ARTIFICIAL_FACEMASK = incorrect_face_mask_underchin
    else:
        sys.exit(1)

    # Checks if dir exists if not creates the dir
    ensure_dir(PATH)

    if args.folder:
        check_path(args.folder)
        # runs the program for a folder of images
        for filename in os.listdir(f"{os.getcwd()}/{args.folder}"):
            print(filename)
            output_image = ARTIFICIAL_FACEMASK(
                f"{args.folder}/{filename}", args.mask, args.labels)
            if not isinstance(output_image, str):
                cv2.imwrite(f"{PATH}/{filename}", output_image)
            else:
                print("No face has been detected")
    else:
        check_path(args.image)
        # runs the program for a single image
        output_image = ARTIFICIAL_FACEMASK(args.image, args.mask, args.labels)  # pylint: disable=C0103

        if isinstance(output_image, str):
            print("No face has been detected")
        else:
            filename = (args.image).split("/")[-1]  # pylint: disable=C0103

        print(f"{PATH}/{filename}")
        cv2.imwrite(f"{PATH}/{filename}", output_image)
