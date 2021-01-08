from main import text
from emojis import emojis, dict, emojidict
from textblob import TextBlob
from sklearn import svm
import numpy as np

# X = [[0, 0], [1, 1]]; [word.sentiment.polarity, word.sentiment.subjectivity]
# y = [0, 1]; labels for what each word is associated with

X = []
y = []
counter = 0
for key in emojidict:
    for i in emojidict.get(key):
        m = TextBlob(i)
        curr = [m.sentiment.polarity, m.sentiment.subjectivity]
        X.append(curr)
        y.append(counter)
    counter = counter + 1

clf = svm.SVC()
clf.fit(X, y)

message = [TextBlob(text).sentiment.polarity, TextBlob(text).sentiment.subjectivity]
print(clf.predict([message]))