"""renames image names"""
import os
import sys


def rename_image(path, img_name):
    """renames the image"""
    for i, image in enumerate(os.listdir(path)):
        # set a path for the renamed images and their new name
        os.rename(path+"/"+image, path+"/"+img_name+str(i+1).zfill(4)+".jpg")


if __name__ == "__main__":
    current_dir = os.path.dirname(
        os.path.realpath(__file__))  # pylint: disable=C0103
    parent_dir = os.path.dirname(current_dir)  # pylint: disable=C0103
    sys.path.append(parent_dir)

    current_path = os.getcwd()  # pylint: disable=C0103
    args = sys.argv  # pylint: disable=C0103

    def print_available_folders(path):
        """function to print all the available subdirectories of the dataset folder"""

        print("Available Folders:")
        for i, folder in enumerate(os.listdir(path + dataset_folder_name)):
            print("\t"+str(i+1)+") "+folder)

    # check if the running format is correct
    if len(args) != 3:
        print("Wrong format!")
        print("Please try again by specifying a dataset folder name and the folder name of the images you want to remove")  # pylint: disable=C0301
        print("Correct format:")
        print(
            "\t python rename_images.py  {folder name of the data set}  {folder name of the images you want to rename}")  # pylint: disable=C0301
        sys.exit(0)

    # dataset folder name
    dataset_folder_name = args[1]  # pylint: disable=C0103

    # check whether the given dataset folder name exists
    if dataset_folder_name not in os.listdir(parent_dir):
        print("Invalid dataset folder name\nPlease try again")
        sys.exit(0)

    dataset_folder_name = r"\\" + args[1]  # pylint: disable=C0103


# check whether the dataset directory has other subdirectories
    if len(os.listdir(parent_dir+dataset_folder_name)) == 0:
        print("The current dataset directory has no other subfolders")
        print("Please create subdirectories and try again")
        sys.exit(0)

# get the foldername
    folder_within_dataset = args[2]  # pylint: disable=C0103

    if folder_within_dataset == "incorrectMask":
        IMAGENAME = "incorrect-mask-"
    elif folder_within_dataset == "withMask":
        IMAGENAME = "mask-"
    elif folder_within_dataset == "withoutMask":
        IMAGENAME = "no-mask-"
    else:
        print("Wrong Folder Name")
        print_available_folders(parent_dir)
        sys.exit(0)


# add the subdirectory name on the current path
    parent_dir += dataset_folder_name+r'\{}'.format(folder_within_dataset)

    # the purpose of this renamimg is to rename the images names to something
    # that does not exists before in order to avoid FileExistsError
    rename_image(parent_dir, "avoidFileExistsError")

    # the actual renaming according to the current path
    rename_image(parent_dir, IMAGENAME)

    print("Renaming succesfully completed")
