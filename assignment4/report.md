# Assignment 3: Spam classification using Naïve Bayes

## Tobias Lindroth: x hrs

## Robert Zetterlund: y hrs

## _Question 1_ - Preprocessing

<!-- 
a. Note that the email files contain a lot of extra information, besides the actual message.
Ignore that for now and run on the entire text. Further down (in the higher-grade part),
you will be asked to filter out the headers and footers.

b. We don’t want to train and test on the same data. Split the spam and the ham datasets
in a training set and a test set. -->

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
- Approximatly `96.2 %` of the documents were classified correctly by Multinomial. The confusion matrix below shows that it was good at classifying ham
- Approximatly `87.5 %` of the documetns were classified correctly by Bernoulli

<p align="center">
    <img src="fig/q2_easy_ham_confusion.png">
    <p align="center">Figure 1: A confusion matrix showing how the different classifiers performed for easy-ham <p>
<p>

Spam versus hard ham:
- Approximately `91.1 %` of the documents were classified correctly by Multinomial. The confusion matrix below shows that the multinomial classifier was good at predicting spam as spam, but sometimes predicted ham as spam. 
- Approxiamtely `84.8 %` of the documents were classified correctly by Bernoulli. The confusion matrix below shows that the bernoulli classifier was good at predicting spam as spam, but sometimes predicted ham as spam. 

<p align="center">
    <img src="fig/q2_hard_ham_confusion.png">
    <p align="center">Figure 2: A confusion matrix showing how the different classifiers performed for easy-ham  <p>
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

c. If the training set were mostly spam messages, then the prior probability of spam would be very high. This would mean that when classyfing new emails, many ham-emails would be classified as spam emails.

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