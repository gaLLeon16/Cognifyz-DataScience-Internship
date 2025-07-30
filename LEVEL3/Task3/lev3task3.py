import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\rohit\OneDrive\Desktop\Cognifyz\LEVEL1\Task1\Dataset.csv")
df = df.dropna()

def rating_to_category(rating):
    if rating == 0.0:
        return "Unrated"
    elif rating <= 2.5:
        return "Poor"
    elif rating <= 3.5:
        return "Average"
    elif rating <= 4.5:
        return "Good"
    else:
        return "Excellent"

df["Rating Category"] = df["Aggregate rating"].apply(rating_to_category)
df["Primary Cuisine"] = df["Cuisines"].apply(lambda x: x.split(",")[0].strip())
df["Online Delivery"] = df["Has Online delivery"].apply(lambda x: "Yes" if x == "Yes" else "No")
df["Table Booking"] = df["Has Table booking"].apply(lambda x: "Yes" if x == "Yes" else "No")

plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Rating Category", order=["Unrated", "Poor", "Average", "Good", "Excellent"])
plt.title("Rating Category Distribution")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

plt.figure(figsize=(8, 5))
top_cuisines = df["Primary Cuisine"].value_counts().head(10)
sns.barplot(x=top_cuisines.values, y=top_cuisines.index)
plt.title("Top 10 Primary Cuisines")
plt.xlabel("Number of Restaurants")
plt.tight_layout()
plt.savefig("top_cuisines.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Price range", y="Votes")
plt.title("Votes by Price Range")
plt.tight_layout()
plt.savefig("votes_by_price.png")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Online Delivery", y="Aggregate rating")
plt.title("Rating vs Online Delivery")
plt.tight_layout()
plt.savefig("rating_vs_delivery.png")
plt.show()

plt.figure(figsize=(6, 4))
sns.boxplot(data=df, x="Table Booking", y="Aggregate rating")
plt.title("Rating vs Table Booking")
plt.tight_layout()
plt.savefig("rating_vs_booking.png")
plt.show()
