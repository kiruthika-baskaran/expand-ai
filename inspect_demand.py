import geopandas as gpd
import pandas as pd

print("=" * 60)
print("EXPAND AI - DEMAND DATA INSPECTION")
print("=" * 60)

# Load demand data
df = gpd.read_file(
    "data/karur_demand_indicators.geojson"
)

print("\nTotal records:", len(df))


# --------------------------------------------------
# 1. Amenity categories
# --------------------------------------------------

print("\n" + "=" * 60)
print("AMENITY TYPES")
print("=" * 60)

print(
    df["amenity"]
    .value_counts(dropna=False)
    .head(30)
)


# --------------------------------------------------
# 2. Healthcare categories
# --------------------------------------------------

print("\n" + "=" * 60)
print("HEALTHCARE TYPES")
print("=" * 60)

print(
    df["healthcare"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# 3. Education values
# --------------------------------------------------

print("\n" + "=" * 60)
print("EDUCATION VALUES")
print("=" * 60)

print(
    df["education"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# 4. Shop categories
# --------------------------------------------------

print("\n" + "=" * 60)
print("SHOP TYPES")
print("=" * 60)

print(
    df["shop"]
    .value_counts(dropna=False)
    .head(40)
)


# --------------------------------------------------
# 5. Office categories
# --------------------------------------------------

print("\n" + "=" * 60)
print("OFFICE TYPES")
print("=" * 60)

print(
    df["office"]
    .value_counts(dropna=False)
    .head(40)
)


# --------------------------------------------------
# 6. Transport
# --------------------------------------------------

print("\n" + "=" * 60)
print("PUBLIC TRANSPORT TYPES")
print("=" * 60)

print(
    df["public_transport"]
    .value_counts(dropna=False)
)


# --------------------------------------------------
# 7. Highway types
# --------------------------------------------------

print("\n" + "=" * 60)
print("HIGHWAY TYPES")
print("=" * 60)

print(
    df["highway"]
    .value_counts(dropna=False)
    .head(30)
)


# --------------------------------------------------
# 8. Railway types
# --------------------------------------------------

print("\n" + "=" * 60)
print("RAILWAY TYPES")
print("=" * 60)

print(
    df["railway"]
    .value_counts(dropna=False)
)


print("\n" + "=" * 60)
print("INSPECTION COMPLETE")
print("=" * 60)