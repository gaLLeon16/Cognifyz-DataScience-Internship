import pandas as pd

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

df["Online Delivery"] = df["Has Online delivery"].apply(lambda x: 1 if x == "Yes" else 0)
df["Table Booking"] = df["Has Table booking"].apply(lambda x: 1 if x == "Yes" else 0)

top_cuisines = df[df["Rating Category"] == "Excellent"]["Primary Cuisine"].value_counts().head(10)
print("Top Cuisines in Excellent Rated Restaurants:")
print(top_cuisines)

delivery_rating = df.groupby("Online Delivery")["Aggregate rating"].mean()
booking_rating = df.groupby("Table Booking")["Aggregate rating"].mean()

print("\nAverage Rating with/without Online Delivery:")
print(delivery_rating)

print("\nAverage Rating with/without Table Booking:")
print(booking_rating)

correlations = df[["Votes", "Aggregate rating", "Price range", "Online Delivery", "Table Booking"]].corr()
print("\nCorrelation with Votes (Popularity):")
print(correlations["Votes"].sort_values(ascending=False))
