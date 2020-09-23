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
parser.add_argument("foldr_name", type=str,
                    help="name of folder to add to", default="ham")
parser.add_argument("percentage", type=int,
                    help="percentage of training data", default=75)

args = parser.parse_args()

raw_name = args.raw_name
foldr_name = args.foldr_name
percentage = args.percentage

path_to_foldr = "../data/"

train_path = path_to_foldr + foldr_name + "train"
test_path = path_to_foldr + foldr_name + "test"


all_files = glob.glob("../data/raw/" + raw_name + "/**")

size = len(all_files)
quarter = int(size * (percentage / 100))

test_files = all_files[:quarter]
train_files = all_files[quarter:]

for testfile in test_files:
    shutil.copy(testfile, test_path)

for trainfile in train_files:
    shutil.copy(trainfile, train_path)
