import os
import shutil
from PIL import Image
import argparse


def mov_to_trash(files):
    shutil.move(files, "Trash")

def main(name):
    directory = os.getcwd()
    TARGET_DIR = os.path.join(directory,name)

    os.chdir(TARGET_DIR)
    print(f" current directory we are is at : {os.getcwd()}")

    files = os.listdir(".")
    os.makedirs("Trash", exist_ok=True)
    print('Trash directory created')

    print("Starting to read file from the directory one by one ....")

    for files in files:
        try:
            print(f"Opening file {files} \n")
            Image.open(files)
        except Exception as e:
            mov_to_trash(files)
            print(f"Error: {e}")
            print(f"{files} moved to Trash directory")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--target", default = "Camera Roll")
    parsed_arg = args.parse_args()
    main(name= parsed_arg.target)
