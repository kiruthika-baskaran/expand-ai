import os
import osmnx as ox
import pandas as pd

print("=" * 60)
print("EXPAND AI - DEMAND DATA COLLECTION")
print("=" * 60)

print("\nDownloading Karur demand indicators...")

tags = {
    "amenity": [
        "school",
        "college",
        "hospital",
        "bank",
        "atm"
    ],
    "shop": True,
    "office": True,
    "public_transport": True
}

try:

    gdf = ox.features_from_place(
        "Karur, Tamil Nadu, India",
        tags=tags
    )

    print("\nData downloaded successfully!")

    print("Number of records:", len(gdf))

    print("\nAvailable columns:")
    print(list(gdf.columns))

    # Save raw demand data
    os.makedirs("data", exist_ok=True)

    gdf.to_file(
        "data/karur_demand_indicators.geojson",
        driver="GeoJSON"
    )

    print("\nSaved successfully!")
    print("data/karur_demand_indicators.geojson")

except Exception as e:

    print("\nError:")
    print(e)