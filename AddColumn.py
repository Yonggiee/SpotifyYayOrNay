import pandas as pd

f = pd.read_csv("train.csv")
f['isLiked'] = [1 if x >=0.75 else 0 for x in f['danceability']]
f.to_csv("train.csv", index=False)
