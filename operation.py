from main import text
from emojis import emojis, dict
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

xy_list = []
for emoji in emojilist:
    sentiment = TextBlob(emoji).sentiment
    curr = [sentiment.polarity, sentiment.subjectivity]
    xy_list.append(curr)

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

X = np.array(xy_list)
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

data = np.array([[x, y]])
cry = [[TextBlob("cry").sentiment.polarity, TextBlob("cry").sentiment.subjectivity]]
happy = [[TextBlob("happy").sentiment.polarity, TextBlob("happy").sentiment.subjectivity]]
laugh = [[TextBlob("laugh").sentiment.polarity, TextBlob("laugh").sentiment.subjectivity]]
angry = [[TextBlob("angry").sentiment.polarity, TextBlob("angry").sentiment.subjectivity]]
# plt.scatter(X[:, 0], X[:, 1])

print("happy: ", kmeans.predict(happy))
print("laugh: ", kmeans.predict(laugh))
print("cry: ", kmeans.predict(cry))
print("angry: ", kmeans.predict(angry))
print("your message: ", kmeans.predict(data))

if kmeans.predict(data) == kmeans.predict(happy):
    print(text, dict.get("smile"))
elif kmeans.predict(data) == kmeans.predict(laugh):
    print(text, dict.get("laugh"))
elif kmeans.predict(data) == kmeans.predict(cry):
    print(text, dict.get("sad"))
elif kmeans.predict(data) == kmeans.predict(angry):
    print(text, dict.get("angry"))