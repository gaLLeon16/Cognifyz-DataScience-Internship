import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

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
df["Price Label"] = df["Price range"].apply(lambda x: "Budget" if x <= 2 else "Premium")
df["Online Delivery"] = df["Has Online delivery"].apply(lambda x: 1 if x == "Yes" else 0)
df["Table Booking"] = df["Has Table booking"].apply(lambda x: 1 if x == "Yes" else 0)

features = df[["Price range", "Votes", "Online Delivery", "Table Booking"]]
target = df["Rating Category"]

target = target.map({
    "Unrated": 0,
    "Poor": 1,
    "Average": 2,
    "Good": 3,
    "Excellent": 4
})

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
