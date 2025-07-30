import pandas as pd

data_path = r"C:\Users\rohit\OneDrive\Desktop\Cognifyz\LEVEL1\Task1\Dataset.csv"
df = pd.read_csv(data_path)

print("First 5 Rows of the Dataset:")
print(df.head())

print("\nShape of Dataset (Rows, Columns):")
print(f"{df.shape[0]} rows, {df.shape[1]} columns")

print("\nData Types of Columns:")
print(df.dtypes)

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

df_clean = df.dropna()

print("\nShape After Dropping Missing Values:")
print(df_clean.shape)

print("\nDistribution of Aggregate Ratings:")
print(df_clean["Aggregate rating"].value_counts())
