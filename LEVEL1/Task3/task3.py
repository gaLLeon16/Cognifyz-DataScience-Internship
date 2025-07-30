import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_path = r"C:\Users\rohit\OneDrive\Desktop\Cognifyz\LEVEL1\Task1\Dataset.csv"
df = pd.read_csv(data_path)

df = df.dropna()

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x='Longitude',
    y='Latitude',
    hue='Aggregate rating',
    palette='coolwarm',
    alpha=0.6,
    edgecolor=None
)

plt.title('Geospatial Distribution of Restaurants')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Aggregate Rating')
plt.tight_layout()
plt.savefig("level1_task3_output.png")
plt.show()
