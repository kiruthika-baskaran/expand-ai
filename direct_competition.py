import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("data/karur_hospitality_clean.csv")

# Make coordinates numeric
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# Remove businesses without coordinates
df = df.dropna(subset=["latitude", "longitude"]).copy()


# Haversine distance function
def haversine(lat1, lon1, lat2, lon2):

    R = 6371

    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1)
        * np.cos(lat2)
        * np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arcsin(np.sqrt(a))

    return R * c


categories = [
    "hotel",
    "restaurant",
    "cafe",
    "fast_food"
]

# Create columns
for category in categories:
    df[f"{category}_competitors_1km"] = 0


# Calculate competition
for i, row in df.iterrows():

    distances = haversine(
        row["latitude"],
        row["longitude"],
        df["latitude"].values,
        df["longitude"].values
    )

    nearby = distances <= 1.0

    for category in categories:

        count = (
            (df["category"].values == category)
            & nearby
        ).sum()

        # Don't count the business itself
        if row["category"] == category:
            count -= 1

        df.loc[
            i,
            f"{category}_competitors_1km"
        ] = max(count, 0)


# Save result
df.to_csv(
    "data/karur_direct_competition.csv",
    index=False
)


print("=" * 60)
print("EXPAND AI - DIRECT COMPETITION ANALYSIS")
print("=" * 60)

print("\nBusinesses analysed:", len(df))

print("\nSample results:")

print(
    df[
        [
            "business_name",
            "category",
            "hotel_competitors_1km",
            "restaurant_competitors_1km",
            "cafe_competitors_1km",
            "fast_food_competitors_1km"
        ]
    ].head(15).to_string(index=False)
)

print("\nAverage competition by category:")

for category in categories:
    column = f"{category}_competitors_1km"
    print(
        f"{category}: "
        f"{df[column].mean():.2f}"
    )

print("\nSaved successfully!")
print("data/karur_direct_competition.csv")