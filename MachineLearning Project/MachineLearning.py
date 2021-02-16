# tutorial found here: https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

# check versions of libs

import sys
# print ('Python:{}'.format(sys.version))

import scipy
# print ('scipy: {}'.format(scipy.__version__))

import numpy
# print ('numpy: {}'.format(numpy.__version__))

import matplotlib
# print ('matplotlib: {}'.format(matplotlib.__version__))

import pandas
# print ('pandas: {}'.format(pandas.__version__))

import sklearn
# print ('sklearn:{}'.format(sklearn.__version__ ))

# Load Libraries

from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load Dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# shape print - should be (150,5) indicating 150 instances and 5 attributes
# print(dataset.shape)

# head - peek at the data and see it all 
# print(dataset.head(20))

# descriptions 
# print(dataset.describe()) 

# class distribution
# print(dataset.groupby('class').size())

# Data Visualization
# Univariate Plots - Box and Whisker
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

# Histograms
# dataset.hist()
# pyplot.show()

# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()

