import osmnx as ox
import os

print("Downloading Karur map data...")

places = ox.features_from_place(
    "Karur, Tamil Nadu, India",
    tags={
        "amenity": ["restaurant", "cafe", "fast_food"],
        "tourism": ["hotel", "guest_house"]
    }
)

print("\nData downloaded successfully!")
print("Number of records:", len(places))

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save the raw OpenStreetMap data
places.to_csv("data/karur_hospitality_raw.csv")

print("\nDataset saved successfully!")
print("File: data/karur_hospitality_raw.csv")