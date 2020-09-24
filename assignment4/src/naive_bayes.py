# mutli: https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes
# bernoulli:  https://scikit-learn.org/stable/modules/naive_bayes.html#bernoulli-naive-bayes

from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os

# Method for creating a dataframe where each email-file is represented by a row.
# data is a list with tupels (folder_name:String, label:String) that tells this 
# method in which directories to look for files and how to label the files found.
def files_to_df(data):
    #Create empty dataframe
    df = pd.DataFrame(columns=['text', 'label'])
    for folder_name,label in data:
        for filename in os.listdir('../data/' + folder_name + '/'):
            # Open in read only mode, ignore any unicode decode errors
            with open(os.path.join('../data/' + folder_name + '/', filename), 'r', encoding='utf-8', errors='ignore') as f:
                # Add a row in dataframe with email-text and whether the email is spam or ham  
                df = df.append({'text':f.read(), 'label':label}, ignore_index=True)  
    return df 


# Create dataframes from files
training_data = [('hamtrain', 'ham'), ('spamtrain', 'spam')]
test_data = [('hamtest', 'ham'), ('spamtest', 'spam')]


# Create training and test dataframes. Not sure if shuffle is needed
df_training = shuffle(files_to_df(training_data))
df_test = shuffle(files_to_df(test_data))

X_train = df_training.text
Y_train = df_training.label


vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(X_train)

#Create classifier and fit for multinomial model
clfMulti = MultinomialNB()
clfMulti.fit(counts, Y_train)

#Create classifier and fit for bernoulli model
clfBernoulli = BernoulliNB(binarize=1)
clfBernoulli.fit(counts, Y_train)

X_test = df_test.text
Y_test = df_test.label

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


           

