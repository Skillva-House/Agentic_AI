from pathlib import Path

import pandas as pd

students_file = Path(__file__).with_name("students.csv")
df = pd.read_csv(students_file)

print(df.head())
df.info()
print(df.describe())
print(df.shape, df.columns.tolist())

# Selecting
print(df["name"])
print(df[["name", "score"]])

# loc (labels) vs iloc (positions)
print(df.loc[0, "name"])
print(df.iloc[0, 0])
print(df.loc[df["score"] > 80, ["name", "score"]])

# Filtering
print(df[df["city"] == "Lahore"])
print(df[(df["score"] > 70) & (df["dept"] == "AI")])   # use & and |, with brackets

# Sorting
print(df.sort_values("score", ascending=False).head(3))

# New column
df["passed"] = df["score"] >= 70
print(df)