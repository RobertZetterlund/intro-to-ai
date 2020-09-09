from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import plot_confusion_matrix
from sklearn.datasets import load_iris

# Load iris dataset and get data and classification
bunch = load_iris()
X = bunch["data"]
y = bunch["target"]

# get classnames (setosa,versicolor,virginica)
class_names = bunch["target_names"]

# Use use onevsrestclassifier with a logistic regression.......
# Train one logistic classifier for each class
clf1 = OneVsRestClassifier(LogisticRegression()).fit(X, y)

# create confusion matrix
plot_confusion_matrix(clf1, X,y, display_labels=class_names, cmap=plt.cm.get_cmap("Blues"))

# show!!!!
plt.show()