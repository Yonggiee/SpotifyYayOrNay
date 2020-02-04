import pandas as pd

f = pd.read_csv("training.csv")
keep_col = ['danceability', 'energy', 'key',
            'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 
            'tempo']
new_f = f[keep_col]
new_f.to_csv("removedColsTraining.csv", index=False)

