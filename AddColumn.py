import pandas as pd

f = pd.read_csv("train.csv")
f['isLiked'] = [1 if x >=0.75 else 0 for x in f['danceability']]
# keep_col = ['danceability', 'energy', 'key',
#             'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 
#             'tempo']
# new_f = f[keep_col]
f.to_csv("train.csv", index=False)
