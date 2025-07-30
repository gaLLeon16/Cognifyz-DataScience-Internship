import pandas as pd

data_path = r"C:\Users\rohit\OneDrive\Desktop\Cognifyz\LEVEL1\Task1\Dataset.csv"
df = pd.read_csv(data_path)

df = df.dropna()

print("Basic Statistical Measures:")
print(df.describe())  

print("\nMedian Values:")
print(df.median(numeric_only=True))

print("\nTop Countries by Restaurant Count:")
print(df['Country Code'].value_counts().head(5))

print("\nTop Cities by Restaurant Count:")
print(df['City'].value_counts().head(10))

print("\nTop Cuisines by Restaurant Count:")
print(df['Cuisines'].value_counts().head(10))
