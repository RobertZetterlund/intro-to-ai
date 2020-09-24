import glob
import os
import shutil
import argparse


# python3 read_files.py --folder easy_ham
# python3 read_files.py --folder hard_ham
# python3 read_files.py --folder spam

PATH_TO_DATA = "../data/"

# Setup argument parser
parser = argparse.ArgumentParser(
    description="Copies files from raw data to train/test, expects name of raw data and percentage"
)
parser.add_argument("--folder", type=str,
                    help="folder name of raw data", default="easy_ham")
parser.add_argument("--percentage", type=int,
                    help="percentage of training data", default=75)

args = parser.parse_args()

folder = args.folder
percentage = args.percentage

train_path = os.path.join(PATH_TO_DATA + folder + "_train/")
test_path = os.path.join(PATH_TO_DATA + folder + "_test/")

all_files = glob.glob("../data/raw/" + folder + "/**")

size = len(all_files)
splitIndex = int(size * (percentage / 100))

test_files = all_files[:splitIndex]
train_files = all_files[splitIndex:]

# helper function for refreshing directory
def emptyDir(path):
    if os.path.isdir(path):
        shutil.rmtree(path) 
    os.mkdir(path)

# copy files to test folder
def copyFilesToDir(files, path):
    for file in files:
        shutil.copy(file, path)


emptyDir(test_path)
copyFilesToDir(test_files, test_path)

emptyDir(train_path)
copyFilesToDir(train_files, train_path)

