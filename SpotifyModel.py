import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
# Import train_test_split function
from sklearn.model_selection import train_test_split

songs = pd.read_csv("removedColsTraining.csv")
feature_cols = ['danceability', 'energy', 'key',
                'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence',
                'tempo']
X = songs[feature_cols]  # Features
y = songs['isLiked']  # Target variable

clf = DecisionTreeClassifier()
clf = clf.fit(X, y)

testSet = pd.read_csv("removedColsTest.csv")
y_pred = clf.predict(testSet)
print(y_pred)