from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import plot_confusion_matrix
from sklearn.datasets import load_iris

iris = load_iris()

X, y = load_iris(return_X_y=True)
print(y)
class_names = iris.target_names
print(class_names)

clf1 = OneVsRestClassifier(LogisticRegression(random_state=0)).fit(X, y)


plot_confusion_matrix(clf1, X,y, display_labels=class_names, cmap=plt.cm.Blues)

plt.show()