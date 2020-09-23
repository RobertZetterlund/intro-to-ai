import glob
import os
import shutil



easy_ham = glob.glob('../data/raw/easy_ham/**')

#print(easy_ham)

# move 1/4 of folder

size =  len(easy_ham)
quarter = size//4




test_ham = easy_ham[:quarter]
train_ham = easy_ham[quarter:]

print(len(easy_ham))
print(len(test_ham))
print(len(train_ham))


for testfile in test_ham:
    shutil.copy(testfile, '../data/hamtest')

for trainfile in train_ham:
    shutil.copy(trainfile, "../data/hamtrain")