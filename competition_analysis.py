import pandas as pd
import numpy as np

# Load cleaned data
df = pd.read_csv("data/karur_hospitality_clean.csv")

# Make coordinates numeric
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# Keep businesses with valid coordinates
df = df.dropna(subset=["latitude", "longitude"]).copy()


# Function to calculate distance between two coordinates
def haversine(lat1, lon1, lat2, lon2):

    R = 6371  # Earth radius in kilometers

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


# Calculate nearby competition
competitor_counts = []

for i, row in df.iterrows():

    distances = haversine(
        row["latitude"],
        row["longitude"],
        df["latitude"].values,
        df["longitude"].values
    )

    # Count businesses within 1 km
    # Exclude the business itself
    nearby = (distances <= 1.0).sum() - 1

    competitor_counts.append(nearby)


# Add feature
df["competitor_count_1km"] = competitor_counts


# Sort by competition
df = df.sort_values(
    "competitor_count_1km",
    ascending=False
)


# Save results
df.to_csv(
    "data/karur_competition_analysis.csv",
    index=False
)


print("=" * 60)
print("EXPAND AI - COMPETITION ANALYSIS")
print("=" * 60)

print("\nBusinesses analysed:", len(df))

print("\nTop 10 most competitive locations:")

print(
    df[
        [
            "business_name",
            "category",
            "competitor_count_1km"
        ]
    ].head(10).to_string(index=False)
)

print("\nCompetition statistics:")
print(df["competitor_count_1km"].describe())

print("\nSaved successfully!")
print("data/karur_competition_analysis.csv")