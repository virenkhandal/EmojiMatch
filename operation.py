from main import text
from emojis import emojis
from textblob import TextBlob
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

message = TextBlob(text)

x = message.sentiment.polarity
y = message.sentiment.subjectivity


all_points = []
emojilist = ['happy', 'laugh', 'sad', 'angry']
for emoji in emojis:
    for i in emoji:
        sentiment = TextBlob(i).sentiment
        curr = [sentiment.polarity, sentiment.subjectivity]
        all_points.append(curr)

# emoji_polarity = []
# emoji_subjectivity = []
# for emoji in emojis:
#     curr_polarity = []
#     curr_subjectivity = []
#     for i in emoji:
#         curr_polarity.append(TextBlob(i).sentiment.polarity)
#         curr_subjectivity.append(TextBlob(i).sentiment.subjectivity)
#     emoji_polarity.append(curr_polarity)
#     emoji_subjectivity.append(curr_subjectivity)

X = np.array(all_points)
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

Y = np.array([[x, y]])
plt.scatter(X[:, 0], X[:, 1])

#print(kmeans.predict(Y))