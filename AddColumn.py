import pandas as pd

def addColumn(filename, value):
    f = pd.read_csv(filename)
    f['isLiked'] = value
    return f

yes = addColumn("Yes.csv", 1)
no = addColumn("No.csv", 0)
result = pd.concat([yes, no])
result.to_csv("train.csv", index=False)
