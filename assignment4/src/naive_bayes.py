# Author: {Tobias Lindroth & Robert Zetterlund}
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import os
import re
from sklearn.metrics import plot_confusion_matrix
import argparse
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import email


parser = argparse.ArgumentParser(
    description="Uses naive bayes to filter spam and ham, a good result can be achieved via argument: --token_pattern True "
)
# using "Date:" improves classification by 1 percent for bernoulli (if easy)
parser.add_argument("--filterOn", type=str,
                    help="string to filterOn", default="")

parser.add_argument("--difficulty", type=str,
                    help="difficulty of ham, enum either 'easy' or 'hard'", default="easy")

parser.add_argument("--nrFiles", type=int,
                    help="determines the number of files to read, speeds up debugging", default=-1)

parser.add_argument("--stop_words",  type=str,
                    help="Uses countvectorizers stop_words, default is english", default=None)
parser.add_argument("--token_pattern",  type=bool,
                    help="Uses a regex to help tokenization, default is pythons own. If set to true, we will use '[a-z]{3,}' which ignores special signs and digits, \
                     and only accepts words longer than 2 ", default=False)
parser.add_argument("--min_df",  type=float,
                    help="Float in range [0.0, 1.0] or int, default=1 When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold. This value is also called cut-off in the literature. If float, the parameter represents a proportion of documents, integer absolute counts", default=1)
parser.add_argument("--max_df",  type=float,
                    help="Float in range [0.0, 1.0] or int, default=1.0 When building the vocabulary ignore terms that have a document frequency strictly higher than the given threshold. If float, the parameter represents a proportion of documents, integer absolute counts.", default=1.0)
parser.add_argument("--email_filtering", type=bool,
                    help="Whether to use email parse to remove header and footer", default=False)


args = parser.parse_args()

filterOn = args.filterOn
difficulty = args.difficulty
nrFiles = args.nrFiles
stop_words = args.stop_words
token_pattern = args.token_pattern
min_df = args.min_df
max_df = args.max_df
emailFiltering = args.email_filtering

# Tries to remove the header and footers from the email
def getBodyFromEmail(mail):
    return getPayload(email.message_from_string(mail))

# Recursive function that fetches the payload from a Message object
# Returns a string
def getPayload(mail):
    if mail.is_multipart():
        return '\n'.join(list(map(lambda x: getPayload(x), mail.get_payload())))
    else:
        return mail.get_payload()


# Method for creating a dataframe where each email-file is represented by a row.
# data is a list with tupels (folder_name:String, label:String) that tells this
# method in which directories to look for files and how to label the files found.
def files_to_df(data):
    # Create empty dataframe
    df = pd.DataFrame(columns=['text', 'label'])
    for folder_name, label in data:
        for filename in os.listdir('../data/' + folder_name + '/')[:nrFiles]:
            # Open in read only mode, ignore any unicode decode errors
            with open(os.path.join('../data/' + folder_name + '/', filename), 'r', encoding='latin1') as f:
                # Add a row in dataframe with email-text and whether the email is spam or ham
                content = f.read()
                if filterOn:
                    content = content.split(filterOn, 1)[-1]
                if emailFiltering:
                    content = getBodyFromEmail(content)

                df = df.append(
                    {'text': content, 'label': label}, ignore_index=True)
    return df


# Create dataframes from files
training_data = [(difficulty + '_ham_train', 'ham'), ('spam_train', 'spam')]
test_data = [(difficulty + '_ham_test', 'ham'), ('spam_test', 'spam')]


# Create training and test dataframes. Not sure if shuffle is needed
df_training = files_to_df(training_data)
df_test = files_to_df(test_data)

X_train = df_training.text
Y_train = df_training.label

# Count how many times each word occurs (for each email).
# Fit creates vocabulary with all words in all the emails
# Transform creates a vector for each document.
# Each vector has the length of the entire vocabulary and
# an integer count for the number of times each word appeared in the document.
myPattern = r'[a-z]{4,}' if token_pattern else r'(?u)\b\w\w+\b'

vectorizer = CountVectorizer(
    stop_words=stop_words, max_df=max_df, min_df=min_df, token_pattern=myPattern)
counts = vectorizer.fit_transform(X_train)

# Create classifier and fit for multinomial model.
clfMulti = MultinomialNB()
clfMulti.fit(counts, Y_train)

# Create classifier and fit for bernoulli model
clfBernoulli = BernoulliNB(binarize=1)
clfBernoulli.fit(counts, Y_train)

X_test = df_test.text
Y_test = df_test.label

# Transforms each document into a vector (with length of vocabulary of train documents) with an
# integer count for the number of times each word appeared in the document
example_count = vectorizer.transform(X_test)

# Predict labels on the test data set
predictionsMulti = clfMulti.predict(example_count)
predictionsBernoulli = clfBernoulli.predict(example_count)


def getPercentageCorrect(predictions):
    zippedTargetsPredictions = zip(Y_test, predictions)
    return sum(target == prediction for target, prediction in zippedTargetsPredictions) / len(predictions)*100


percentCorrectMulti = getPercentageCorrect(predictionsMulti)
percentCorrectBernoulli = getPercentageCorrect(predictionsBernoulli)

print(percentCorrectMulti, "% were classified correctly by Multinomial")
print(percentCorrectBernoulli, "% were classified correctly by Bernoulli")

word_count = counts.sum(axis=0).tolist()[0]
words = vectorizer.get_feature_names()
word_df = pd.DataFrame(zip(words, word_count),
                       columns=['word', 'word_count']
                       ).sort_values(by=['word_count'], ascending=False)

#print("Top 100 words \n", word_df["word"][0:100].tolist())


# Create confusion matrixes
bConfusion = confusion_matrix(Y_test, predictionsBernoulli)
mConfusion = confusion_matrix(Y_test, predictionsMulti)

bernoulliConfusion = ConfusionMatrixDisplay(
    confusion_matrix=bConfusion, display_labels=['ham', 'spam'])
multiConfusion = ConfusionMatrixDisplay(
    confusion_matrix=mConfusion, display_labels=['ham', 'spam'])

# Plot confusion matrixes
fig, ax = plt.subplots(nrows=1, ncols=2)
bernoulliConfusion.plot(ax=ax[0], cmap=plt.get_cmap("Blues"))
multiConfusion.plot(ax=ax[1], cmap=plt.get_cmap("Greens"))

# Set titles
bernoulliConfusion.ax_.set_title("Bernoulli classifier")
multiConfusion.ax_.set_title("Multinomial classifier")
plt.show()
