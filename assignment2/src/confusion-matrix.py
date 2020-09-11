## Author: {Tobias Lindroth & Robert Zetterlund}

import matplotlib.pyplot as plt
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import plot_confusion_matrix
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load iris dataset and get data and classification
bunch = load_iris()
X = bunch["data"]
y = bunch["target"]

# get classnames (setosa,versicolor,virginica)
class_names = bunch["target_names"]

# divide into training and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# Train one logistic classifier for each class
clf1 = OneVsRestClassifier(LogisticRegression()).fit(X_train, y_train)

# create confusion matrix
plot_confusion_matrix(clf1, X_test,y_test, display_labels=class_names, cmap=plt.get_cmap("Blues"))
plt.title("One versus rest classifier with logistic regression \n for the iris data set")

plt.show()