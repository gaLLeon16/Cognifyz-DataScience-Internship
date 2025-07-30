import pandas as pd

df = pd.read_csv(r"C:\Users\rohit\OneDrive\Desktop\Cognifyz\LEVEL1\Task1\Dataset.csv")

df = df.dropna()

table_booking_counts = df["Has Table booking"].value_counts()

print("Table Booking Availability:")
print(table_booking_counts)

total_restaurants = len(df)
table_booking_percent = (table_booking_counts["Yes"] / total_restaurants) * 100
no_table_booking_percent = (table_booking_counts["No"] / total_restaurants) * 100

print(f"\nPercentage with Table Booking: {table_booking_percent:.2f}%")
print(f"Percentage without Table Booking: {no_table_booking_percent:.2f}%")

avg_rating_with_booking = df[df["Has Table booking"] == "Yes"]["Aggregate rating"].mean()
avg_rating_without_booking = df[df["Has Table booking"] == "No"]["Aggregate rating"].mean()

print(f"\nAverage Rating (With Table Booking): {avg_rating_with_booking:.2f}")
print(f"Average Rating (Without Table Booking): {avg_rating_without_booking:.2f}")

delivery_counts = df["Has Online delivery"].value_counts()
print("\nOnline Delivery Availability:")
print(delivery_counts)

delivery_percent = (delivery_counts["Yes"] / total_restaurants) * 100
no_delivery_percent = (delivery_counts["No"] / total_restaurants) * 100

print(f"\nPercentage with Online Delivery: {delivery_percent:.2f}%")
print(f"Percentage without Online Delivery: {no_delivery_percent:.2f}%")

delivery_by_price = df[df["Has Online delivery"] == "Yes"]["Price range"].value_counts().sort_index()
print("\nOnline Delivery Available by Price Range:")
print(delivery_by_price)
