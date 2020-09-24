# multi-naive bayes:
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
import glob
import numpy as np
import codecs

# helper method for extracting content of file
def getFileContent(filepaths):
    listOfContent = []
    for filepath in filepaths:
        file = open(filepath, mode='r', encoding="latin1")
        file_content = file.read()
        listOfContent.append(file_content)
        file.close()
    return listOfContent


# ====== READ FILES AND TRAIN MODEL ==========
hamtrain_paths = glob.glob("../data/hamtrain/**")[0:100]
ham_train = getFileContent(hamtrain_paths)

spamtrain_paths = glob.glob("../data/spamtrain/**")[0:100]
spam_train = getFileContent(spamtrain_paths)

vectorizer = CountVectorizer()

HAM_TRAIN_X = vectorizer.fit_transform(ham_train).toarray()
SPAM_TRAIN_X = vectorizer.fit_transform(spam_train).toarray()

# here 1 is ham, 0 is spam
HAM_TRAIN_Y = np.ones(len(HAM_TRAIN_X), dtype=int)
SPAM_TRAIN_Y = np.zeros(len(SPAM_TRAIN_X), dtype=int)

# ====== TRAIN CLASSIFIER ====
training_X = np.append(HAM_TRAIN_X,SPAM_TRAIN_X, axis=0)
training_Y = np.append(HAM_TRAIN_Y, SPAM_TRAIN_Y, axis=0)

clf = MultinomialNB()

clf.fit(training_X, training_Y)