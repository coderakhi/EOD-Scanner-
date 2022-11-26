import pandas as pd

df = pd.read_csv("3131.csv", parse_dates=True, index_col="datetime")

df["year"] = df.index.year
df["month"] = df.index.strftime("%B")
df["week"] = df.index.isocalendar().week

print(df)
result = []
for group_index, sliced_df in df.groupby(["year"]):
    print(sliced_df)







