from pathlib import Path

import pandas as pd

df = pd.read_csv(Path(__file__).with_name("titanic.csv"))

# Inspect
print(df.isna().sum())          # missing per column
print(df.duplicated().sum())
print(df.dtypes)

# Missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df = df.rename(columns={"2urvived": "Survived"})
df = df.drop(columns=["Cabin"], errors="ignore")
df = df.dropna()                     # drop any remaining
df = df.drop_duplicates()

# Types
df["Survived"] = df["Survived"].astype(int)

# Groupby
print(df.groupby("Sex")["Survived"].mean())
print(df.groupby("Pclass")["Fare"].agg(["mean", "max", "count"]))
print(df.groupby(["Pclass", "Sex"])["Survived"].mean())

# value_counts
print(df["Embarked"].value_counts())

# apply
df["AgeGroup"] = df["Age"].apply(lambda a: "child" if a < 18 else "adult")

# merge
depts = pd.DataFrame({"Pclass": [1, 2, 3], "Label": ["First", "Second", "Third"]})
df = df.merge(depts, on="Pclass", how="left")
print(df[["Pclass", "Label"]].head())