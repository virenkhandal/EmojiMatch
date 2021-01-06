from main import text
from emojis import emojis, dict
from textblob import TextBlob
from sklearn import svm
from kmeans import xy_list
import numpy as np

clf = svm.SVC()
X = np.array(xy_list)
# clf.fit(X[:, 0], X[:, 1])