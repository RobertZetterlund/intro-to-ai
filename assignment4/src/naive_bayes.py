# mutli: https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes
# bernoulli:  https://scikit-learn.org/stable/modules/naive_bayes.html#bernoulli-naive-bayes

from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os
import argparse

#all_content = [content.split(filterOn,1)[1] for content in all_content]

parser = argparse.ArgumentParser(
    description="Uses naive bayes to filter spam and ham"
)

# using "Date:" improves classification by 1 percent.
parser.add_argument("--filterOn", type=str,
                    help="string to filterOn", default="")
args = parser.parse_args()

filterOn = args.filterOn

# Method for creating a dataframe where each email-file is represented by a row.
# data is a list with tupels (folder_name:String, label:String) that tells this 
# method in which directories to look for files and how to label the files found.
def files_to_df(data):
    #Create empty dataframe
    df = pd.DataFrame(columns=['text', 'label'])
    for folder_name,label in data:
        for filename in os.listdir('../data/' + folder_name + '/'):
            # Open in read only mode, ignore any unicode decode errors
            with open(os.path.join('../data/' + folder_name + '/', filename), 'r', encoding='latin1') as f:
                # Add a row in dataframe with email-text and whether the email is spam or ham  
                content = f.read()
                if filterOn:
                    ## currently selects last part of email when finding a filterOn String,
                    ## this might be faulty if filterOn is not unique, perhaps consider 
                    ## selecting "second", however, if keyword to filterOn is not in email that crashes.
                    content = content.split(filterOn,1)[-1]

                df = df.append({'text':content, 'label':label}, ignore_index=True)  
    return df 


# Create dataframes from files
training_data = [('hamtrain', 'ham'), ('spamtrain', 'spam')]
test_data = [('hamtest', 'ham'), ('spamtest', 'spam')]


# Create training and test dataframes. Not sure if shuffle is needed
df_training = shuffle(files_to_df(training_data))
df_test = shuffle(files_to_df(test_data))

X_train = df_training.text
Y_train = df_training.label

# Count how many times each word occurs (for each email).
# Fit creates vocabulary with all words in all the emails
# Transform creates a vector for each document. 
# Each vector has the length of the entire vocabulary and 
# an integer count for the number of times each word appeared in the document.
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(X_train)

#Create classifier and fit for multinomial model.
clfMulti = MultinomialNB()
clfMulti.fit(counts, Y_train)

#Create classifier and fit for bernoulli model
clfBernoulli = BernoulliNB(binarize=1)
clfBernoulli.fit(counts, Y_train)

X_test = df_test.text
Y_test = df_test.label

#Transforms each document into a vector (with length of vocabulary of train documents) with an 
#integer count for the number of times each word appeared in the document
example_count = vectorizer.transform(X_test)

# Predict labels on the test data set 
predictionsMulti = clfMulti.predict(example_count)
predictionsBernoulli = clfBernoulli.predict(example_count)

# Calculate percentage of correct classified labels
zippedMulti = zip(Y_test, predictionsMulti)
zippedBernoulli = zip(Y_test, predictionsBernoulli)
percentCorrectMulti = (sum(x == y for x, y in zippedMulti) / len(predictionsMulti))*100
percentCorrectBernoulli = (sum(x == y for x, y in zippedBernoulli) / len(predictionsBernoulli))*100

print(percentCorrectMulti, "% were classified correctly by Multinomial")
print(percentCorrectBernoulli, "% were classified correctly by Bernoulli")


           

