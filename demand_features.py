import geopandas as gpd
import pandas as pd
import numpy as np

print("=" * 60)
print("EXPAND AI - CLEAN DEMAND FEATURES")
print("=" * 60)


# --------------------------------------------------
# 1. Load hospitality businesses
# --------------------------------------------------

businesses = pd.read_csv(
    "data/karur_hospitality_clean.csv"
)

businesses["latitude"] = pd.to_numeric(
    businesses["latitude"],
    errors="coerce"
)

businesses["longitude"] = pd.to_numeric(
    businesses["longitude"],
    errors="coerce"
)

businesses = businesses.dropna(
    subset=["latitude", "longitude"]
).copy()


# --------------------------------------------------
# 2. Load demand indicators
# --------------------------------------------------

demand = gpd.read_file(
    "data/karur_demand_indicators.geojson"
)

print("\nHospitality businesses:", len(businesses))
print("Demand records:", len(demand))


# --------------------------------------------------
# 3. Prepare coordinates correctly
# --------------------------------------------------

demand_projected = demand.to_crs("EPSG:32644")

centroids = demand_projected.geometry.centroid

centroids = centroids.to_crs("EPSG:4326")

demand["latitude"] = centroids.y
demand["longitude"] = centroids.x


# --------------------------------------------------
# 4. Create clean demand categories
# --------------------------------------------------

def value_exists(value):
    return pd.notna(value)


def classify_demand(row):

    categories = set()

    # Healthcare
    if (
        row.get("amenity") == "hospital"
        or row.get("healthcare") == "hospital"
    ):
        categories.add("healthcare")

    # Education
    if (
        row.get("amenity") in ["school", "college"]
        or row.get("education") == "school"
    ):
        categories.add("education")

    # Commercial
    if value_exists(row.get("shop")):
        categories.add("commercial")

    # Financial
    if row.get("amenity") in ["bank", "atm"]:
        categories.add("financial")

    # Transport
    if (
        value_exists(row.get("public_transport"))
        or row.get("highway") == "bus_stop"
        or value_exists(row.get("railway"))
    ):
        categories.add("transport")

    # Business / employment
    if value_exists(row.get("office")):
        categories.add("business")

    return list(categories)


demand["demand_categories"] = demand.apply(
    classify_demand,
    axis=1
)


# --------------------------------------------------
# 5. Distance calculation
# --------------------------------------------------

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
        +
        np.cos(lat1)
        * np.cos(lat2)
        * np.sin(dlon / 2) ** 2
    )

    return R * (
        2 * np.arcsin(np.sqrt(a))
    )


# --------------------------------------------------
# 6. Calculate demand around each business
# --------------------------------------------------

results = []

for _, business in businesses.iterrows():

    distances = haversine(
        business["latitude"],
        business["longitude"],
        demand["latitude"].values,
        demand["longitude"].values
    )

    nearby = demand.loc[
        distances <= 1.0
    ].copy()

    healthcare = 0
    education = 0
    commercial = 0
    financial = 0
    transport = 0
    business_activity = 0

    for categories in nearby["demand_categories"]:

        if "healthcare" in categories:
            healthcare += 1

        if "education" in categories:
            education += 1

        if "commercial" in categories:
            commercial += 1

        if "financial" in categories:
            financial += 1

        if "transport" in categories:
            transport += 1

        if "business" in categories:
            business_activity += 1


    results.append({

        "business_name":
            business["business_name"],

        "category":
            business["category"],

        "latitude":
            business["latitude"],

        "longitude":
            business["longitude"],

        "healthcare_1km":
            healthcare,

        "education_1km":
            education,

        "commercial_1km":
            commercial,

        "financial_1km":
            financial,

        "transport_1km":
            transport,

        "business_activity_1km":
            business_activity
    })


# --------------------------------------------------
# 7. Create DataFrame
# --------------------------------------------------

result = pd.DataFrame(results)


# --------------------------------------------------
# 8. Total demand signals
# --------------------------------------------------

demand_columns = [
    "healthcare_1km",
    "education_1km",
    "commercial_1km",
    "financial_1km",
    "transport_1km",
    "business_activity_1km"
]

result["total_demand_signals"] = (
    result[demand_columns].sum(axis=1)
)


# --------------------------------------------------
# 9. Display results
# --------------------------------------------------

print("\nTop 10 locations by clean demand signals:\n")

print(
    result[
        [
            "business_name",
            "category",
            "healthcare_1km",
            "education_1km",
            "commercial_1km",
            "financial_1km",
            "transport_1km",
            "business_activity_1km",
            "total_demand_signals"
        ]
    ]
    .sort_values(
        "total_demand_signals",
        ascending=False
    )
    .head(10)
    .to_string(index=False)
)


# --------------------------------------------------
# 10. Save
# --------------------------------------------------

result.to_csv(
    "data/karur_demand_features.csv",
    index=False
)

print("\nSaved successfully!")

print(
    "data/karur_demand_features.csv"
)

print("\nClean demand feature analysis complete!")