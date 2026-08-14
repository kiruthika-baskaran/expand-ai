import pandas as pd
import re

# Load raw data
df = pd.read_csv("data/karur_hospitality_raw.csv")

print("Raw dataset:", df.shape)

# Create clean dataframe
clean = pd.DataFrame()

# Business name
clean["business_name"] = df["name"]

# If name is missing, use English name
clean["business_name"] = clean["business_name"].fillna(df["name:en"])

# Create category
def get_category(row):
    if pd.notna(row["tourism"]) and row["tourism"] == "hotel":
        if pd.notna(row["amenity"]) and row["amenity"] == "restaurant":
            return "hotel_restaurant"
        return "hotel"

    if pd.notna(row["amenity"]):
        return row["amenity"]

    return "other"

clean["category"] = df.apply(get_category, axis=1)


# Extract latitude and longitude from geometry
def extract_coordinates(geometry):
    if pd.isna(geometry):
        return pd.Series([None, None])

    match = re.search(
        r"POINT \(([-\d.]+) ([-\d.]+)\)",
        str(geometry)
    )

    if match:
        longitude = float(match.group(1))
        latitude = float(match.group(2))
        return pd.Series([latitude, longitude])

    return pd.Series([None, None])


clean[["latitude", "longitude"]] = df["geometry"].apply(
    extract_coordinates
)


# Other useful columns
clean["cuisine"] = df["cuisine"]
clean["phone"] = df["phone"]
clean["street"] = df["addr:street"]
clean["postcode"] = df["addr:postcode"]
clean["opening_hours"] = df["opening_hours"]
clean["website"] = df["website"]
clean["vegetarian"] = df["diet:vegetarian"]
clean["rooms"] = df["rooms"]

# Source
clean["source"] = "OpenStreetMap"

# Remove records without a business name
clean = clean[clean["business_name"].notna()]

# Remove exact duplicate rows
clean = clean.drop_duplicates()

# Reset index
clean = clean.reset_index(drop=True)

# Save cleaned dataset
clean.to_csv(
    "data/karur_hospitality_clean.csv",
    index=False
)

print("\nClean dataset:", clean.shape)

print("\nCategories:")
print(clean["category"].value_counts())

print("\nFirst 10 clean records:")
print(clean.head(10).to_string(index=False))

print("\nSaved successfully!")
print("data/karur_hospitality_clean.csv")