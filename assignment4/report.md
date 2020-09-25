# Assignment 3: Spam classification using Naïve Bayes

## Tobias Lindroth: x hrs

## Robert Zetterlund: y hrs

## _Question 1_ - Preprocessing


## a
We read through some of the emails and find that some of them have date, reciever and sender in them. We regard this as extra information.
<!-- 
a. Note that the email files contain a lot of extra information, besides the actual message.
Ignore that for now and run on the entire text. Further down (in the higher-grade part),
you will be asked to filter out the headers and footers.
-->
## b
<!--
b. We don’t want to train and test on the same data. Split the spam and the ham datasets
in a training set and a test set. -->

In order to split the datasets we create `split_files.py` which is runnable using arguments to specify which `folder` to copy from and which `percentage` of files that should be training.

```python
# get all filenames
all_files = glob.glob("../data/raw/" + folder + "/**")

# get splitindex
size = len(all_files)
splitIndex = int(size * (percentage / 100))

# create two list of filenames
test_files = all_files[:splitIndex]
train_files = all_files[splitIndex:]

# empty directory of test_path, then copy files to test_path.
emptyDir(test_path)
copyFilesToDir(test_files, test_path)
```

Here are the helper functions:

```python
# helper function for refreshing directory
def emptyDir(path):
    if os.path.isdir(path):
        shutil.rmtree(path) 
    os.mkdir(path)

# copy files to test folder
def copyFilesToDir(files, path):
    for file in files:
        shutil.copy(file, path)
```


## _Question 2_ 


<!-- 
Write a Python program that: 
a. Uses four datasets (hamtrain, spamtrain, hamtest, and spamtest)

b. Using a Naïve Bayes classifier (e.g. Sklearn), classifies the test sets and reports the
percentage of ham and spam test sets that were classified correctly. You can use
CountVectorizer to transform the email texts into vectors. Please note that there are
different types of Naïve Bayes Classifier in SKlearn (Document is available here). Test two
of these classifiers: 1. Multinomial Naive Bayes and 2. Bernoulli Naive Bayes that are well
suited for this problem. For the case of Bernoulli Naive Bayes you should use the
parameter binarize to make the features binary. Discuss the differences between these
two classifiers. 
--> 
Here are some snippets of the code, this is the multinomial model but it is the same for the Bernoulli.

```python
# Create classifier and fit for multinomial model.
clfMulti = MultinomialNB() # if bernoulli: use BernoulliNB instead
clfMulti.fit(counts, Y_train)

example_count = vectorizer.transform(X_test)
predictionsMulti = clfMulti.predict(example_count)

def getPercentageCorrect(predictions):
    zippedTargetsPredictions = zip(Y_test, predictions)
    return sum(target == prediction for target, prediction in zippedTargetsPredictions) / len(predictions)*100

percentCorrectMulti = getPercentageCorrect(predictionsMulti)
```
We get:

* Bernoulli: `97.50%`
* Multinomial: `88.84%`



The bernoulli naive bayes classifier classifies documents based on words being absent or present. 

The multinomial naive bayes classifier classifies documents based on the amount of times words are present in a document. 

That is, an email with the text "You have won money" would get the same classification by bernoulli as the email "You have won money money money money". The multinomial classifier would, on the other hand, would take into account that the second email contains the word "money" four times. 

## _Question 3_ 
<!--
Run your program on
i. Spam versus easy-ham
ii. Spam versus hard-ham
and include the results in your report. 
 -->

Spam versus easy ham:
- **Multinomial**: Approximatly `97.6 %` of the documents were classified correctly. 
- **Bernoulli:** Approximatly `88.8 %` of the documents were classified correctly.

The confusion matrices below shows that both classifiers were good at classifying ham correctly, but sometimes classified spam as ham.

<p align="center">
    <img src="fig/q2_easy_ham_confusion.png">
    <p align="center">Figure 1: Confusion matrices showing how the different classifiers performed for easy-ham <p>
<p>

Spam versus hard ham:
- **Multinomial**: Approximately `91.4 %` of the documents were classified correctly. The confusion matrix below shows that the classifier were quite accurate but classified both ham and spam wrong sometimes. 
- **Bernoulli**: Approxiamtely `84.5 %` of the documents were classified correctly. The confusion matrix below shows that the bernoulli classifier very accurately classified spam as spam, but sometimes classified ham as spam. 

<p align="center">
    <img src="fig/q2_hard_ham_confusion.png">
    <p align="center">Figure 2: Confusion matrices showing how the different classifiers performed for easy-ham  <p>
<p>


## _Question 4_ 

<!--
To avoid classification based on common and uninformative words it is common to filter
these out. 

a. Argue why this may be useful. Try finding the words that are too common/uncommon
in the dataset.
b. Use the parameters in Sklearn’s CountVectorizer to filter out these words. Run the
updated program on your data and record how the results differ from 3. You have
two options to do this in Sklearn: either using the words found in part (a) or letting
Sklearn do it for you. 
-->

## _Question 5_
## A

## B
If the data that is inserted into the training set is very skewed, that is, a majority of the data is of one class, the results will also be skewed. This is because the model will almost only be exposed to one class. 

Let's take the spam and ham emails as an example. If the training dataset almost only consists of ham emails, then the model will believe it is much more likely that the next email also is ham, just because there are som much more ham than spam emails. The prior, p(ham) will be close to 1. 

Furthermore, a lot of the words that are in spam emails, but not ham, will not be entered into the vocabulary since there are so few spam-emails in the training set. This will make it more difficult for the model to classify spam as spam since words that are used in spam emails may not even be in the vocabulary.

One way to fix this would be to trunkate the majority class in the training dataset. This will of course mean a loss of information but it will also lead to more equal datasets and because of that the model will probably be more accurate. 

Another way to fix it could be to add more data to the minority class(es) in the training dataset. This of course means that you need to generate new data in some way or perhaps even duplicate data. 

An additional idea is that you perhaps could add some weight to the data in the minority classes to make the model count minorority classes more importantly. 


## c
By applying the logic from question b, we belive a training set with mostly spam emails would lead to many ham messages in the test set to be classified as spam. 

By removing all but 10 ham-emails from the data set, while keeping all the spam, we get the following result:

**Multinomial**: Approximatly `22.3 %` were classified correctly.

**Bernoulli**: Approxiamtely `16.4 %` were classified correctly.

The models accuracy decreased drastically. And by looking at the confusion matrices below we note that almost all emails are classified as spam. 

<p align="center">
    <img src="fig/q5_easy_ham_only_10.png">
    <p align="center">Figure 3: Confusion matrices showing how the different classifiers performed when there were only 10 ham-emails.   <p>
<p>

<!-- 
Filter out the headers and the footers of the emails before you run on them. The format may
vary somewhat between emails, which can make this a bit tricky, so perfect filtering is not
required. Run your program again and answer the following questions: 

a. Does the result improve from 3 and 4?
b. The split of the data set into a training set and a test set can lead to very skewed results.
Why is this, and do you have suggestions on remedies?
c. What do you expect would happen if your training set were mostly spam messages
while your test set were mostly ham messages? 
-->