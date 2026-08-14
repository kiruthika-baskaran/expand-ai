import pandas as pd
import geopandas as gpd
import numpy as np


print("=" * 60)
print("EXPAND AI - DEMAND FEATURE ANALYSIS")
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
print("Demand indicators:", len(demand))


# --------------------------------------------------
# 3. Create latitude / longitude for demand data
# --------------------------------------------------

demand = demand.to_crs("EPSG:4326")

# Convert to a projected CRS suitable for distance calculations
demand_projected = demand.to_crs("EPSG:32644")

# Calculate centroid in projected coordinates
centroids = demand_projected.geometry.centroid

# Convert centroids back to latitude/longitude
centroids = centroids.to_crs("EPSG:4326")

demand["latitude"] = centroids.y
demand["longitude"] = centroids.x


# --------------------------------------------------
# 4. Distance function
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

    c = 2 * np.arcsin(
        np.sqrt(a)
    )

    return R * c


# --------------------------------------------------
# 5. Count demand indicators around each business
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


    # Education
    education_count = (
        nearby["education"]
        .notna()
        .sum()
    )


    # Healthcare
    healthcare_count = (
        nearby["healthcare"]
        .notna()
        .sum()
    )


    # Shops
    shop_count = (
        nearby["shop"]
        .notna()
        .sum()
    )


    # Banks / ATMs
    bank_count = (
        (
            nearby["amenity"]
            .isin(["bank", "atm"])
        )
        .sum()
    )


    # Transport
    transport_count = (
        (
            nearby["public_transport"]
            .notna()
        )
        |
        (
            nearby["highway"]
            .isin(["bus_stop"])
        )
        |
        (
            nearby["railway"]
            .notna()
        )
    ).sum()


    # Offices
    office_count = (
        nearby["office"]
        .notna()
        .sum()
    )


    results.append({

        "business_name":
            business["business_name"],

        "category":
            business["category"],

        "latitude":
            business["latitude"],

        "longitude":
            business["longitude"],

        "education_1km":
            education_count,

        "healthcare_1km":
            healthcare_count,

        "shops_1km":
            shop_count,

        "banks_atms_1km":
            bank_count,

        "transport_1km":
            transport_count,

        "offices_1km":
            office_count
    })


# --------------------------------------------------
# 6. Create final demand dataset
# --------------------------------------------------

result_df = pd.DataFrame(results)


# --------------------------------------------------
# 7. Create total demand signals
# --------------------------------------------------

demand_columns = [
    "education_1km",
    "healthcare_1km",
    "shops_1km",
    "banks_atms_1km",
    "transport_1km",
    "offices_1km"
]

result_df["total_demand_signals"] = (
    result_df[demand_columns]
    .sum(axis=1)
)


# --------------------------------------------------
# 8. Display results
# --------------------------------------------------

print("\nTop 10 locations by demand signals:")

print(
    result_df[
        [
            "business_name",
            "category",
            "education_1km",
            "healthcare_1km",
            "shops_1km",
            "banks_atms_1km",
            "transport_1km",
            "offices_1km",
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
# 9. Save
# --------------------------------------------------

result_df.to_csv(
    "data/karur_demand_analysis.csv",
    index=False
)


print("\nSaved successfully!")

print(
    "data/karur_demand_analysis.csv"
)

print("\nDemand analysis complete!")