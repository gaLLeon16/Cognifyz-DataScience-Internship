import pandas as pd

data_path = r"C:\Users\rohit\OneDrive\Desktop\Cognifyz\LEVEL1\Task1\Dataset.csv"
df = pd.read_csv(data_path)

df = df.dropna()

most_common_price_range = df["Price range"].value_counts().idxmax()
print(f"Most Common Price Range: {most_common_price_range}")

avg_rating_per_price = df.groupby("Price range")["Aggregate rating"].mean()
print("\nAverage Aggregate Rating for Each Price Range:")
print(avg_rating_per_price)

best_price_range = avg_rating_per_price.idxmax()
print(f"\nPrice Range with Highest Average Rating: {best_price_range}")

most_common_color = df[df["Price range"] == best_price_range]["Rating color"].mode()[0]
print(f"Most Common Rating Color in Price Range {best_price_range}: {most_common_color}")
