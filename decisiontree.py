from main import text
from emojis import emojis, dict, emojidict
from textblob import TextBlob
from sklearn import tree
import numpy as np

X = []
Y = []
counter = 0
for key in emojidict:
    print(key, ": ", counter)
    for i in emojidict.get(key):
        m = TextBlob(i)
        curr = [m.sentiment.polarity]
        X.append(curr)
        Y.append(counter)
    counter = counter + 1

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
tree.plot_tree(clf) 