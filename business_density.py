import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("data/karur_hospitality_clean.csv")

# Make coordinates numeric
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# Keep only businesses with valid coordinates
df = df.dropna(subset=["latitude", "longitude"]).copy()


# Calculate distance between coordinates
def haversine(lat1, lon1, lat2, lon2):

    R = 6371  # Earth radius in km

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


density_counts = []

for _, row in df.iterrows():

    distances = haversine(
        row["latitude"],
        row["longitude"],
        df["latitude"].values,
        df["longitude"].values
    )

    # Count ALL businesses within 1 km
    # Exclude the business itself
    nearby_businesses = (distances <= 1.0).sum() - 1

    density_counts.append(nearby_businesses)


# Add density feature
df["business_density_1km"] = density_counts


# Save dataset
df.to_csv(
    "data/karur_business_density.csv",
    index=False
)


print("=" * 60)
print("EXPAND AI - BUSINESS DENSITY ANALYSIS")
print("=" * 60)

print("\nBusinesses analysed:", len(df))

print("\nTop 10 highest-density locations:")

print(
    df[
        [
            "business_name",
            "category",
            "business_density_1km"
        ]
    ]
    .sort_values(
        "business_density_1km",
        ascending=False
    )
    .head(10)
    .to_string(index=False)
)

print("\nDensity statistics:")

print(
    df["business_density_1km"].describe()
)

print("\nSaved successfully!")
print("data/karur_business_density.csv")