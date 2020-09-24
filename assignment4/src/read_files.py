import glob
import os
import shutil
import argparse


# python3 read_files.py easy_ham ham 75
# python3 read_files.py hard_ham ham 75
# python3 read_files.py spam spam 75

# Setup argument parser
parser = argparse.ArgumentParser(
    description="Copies files from raw data to train/test, expects name of raw data and percentage"
)
parser.add_argument("raw_name", type=str,
                    help="name of raw data", default="easy_ham")
parser.add_argument("folder_name", type=str,
                    help="name of folder to add to", default="ham")
parser.add_argument("percentage", type=int,
                    help="percentage of training data", default=75)

args = parser.parse_args()

raw_name = args.raw_name
folder_name = args.folder_name
percentage = args.percentage

path_to_folder = "../data/"

train_path = path_to_folder + folder_name + "train"
test_path = path_to_folder + folder_name + "test"


all_files = glob.glob("../data/raw/" + raw_name + "/**")

size = len(all_files)
splitIndex = int(size * (percentage / 100))

test_files = all_files[:splitIndex]
train_files = all_files[splitIndex:]

for testfile in test_files:
    shutil.copy(testfile, test_path)

for trainfile in train_files:
    shutil.copy(trainfile, train_path)
