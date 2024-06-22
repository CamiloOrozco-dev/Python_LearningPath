import pandas as pd

df = pd.read_csv("/content/kl.csv", index_col=0, encoding="latin1")
df.head()
