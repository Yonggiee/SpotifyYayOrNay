import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split

songs = pd.read_csv("train.csv")
feature_cols = ['danceability', 'energy', 'key', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence',
                'tempo']

X_train, X_test, y_train, y_test = train_test_split(songs, songs['isLiked'], test_size=0.33, random_state=43)

X_trainFeat = X_train[feature_cols]  # Features
X_testFeat = X_test[feature_cols]

clf = DecisionTreeClassifier()
clf = clf.fit(X_trainFeat, y_train)

y_pred = clf.predict(X_testFeat[feature_cols])

#output in new csv file
results = X_test.copy()
results['isLiked'] = y_pred
results = results[['name', 'isLiked']]
results.to_csv("results.csv", index=False)
