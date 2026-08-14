import pandas as pd
import numpy as np

print("=" * 60)
print("EXPAND AI - OPPORTUNITY SCORE")
print("=" * 60)


# --------------------------------------------------
# 1. Load datasets
# --------------------------------------------------

competition = pd.read_csv(
    "data/karur_competition_analysis.csv"
)

direct_competition = pd.read_csv(
    "data/karur_direct_competition.csv"
)

density = pd.read_csv(
    "data/karur_business_density.csv"
)

demand = pd.read_csv(
    "data/karur_demand_features.csv"
)


# --------------------------------------------------
# 2. Keep only useful columns
# --------------------------------------------------

competition = competition[
    [
        "business_name",
        "competitor_count_1km"
    ]
]

direct_competition = direct_competition[
    [
        "business_name",
        "hotel_competitors_1km",
        "restaurant_competitors_1km",
        "cafe_competitors_1km",
        "fast_food_competitors_1km"
    ]
]

density = density[
    [
        "business_name",
        "business_density_1km"
    ]
]


# --------------------------------------------------
# 3. Merge datasets
# --------------------------------------------------

result = demand.merge(
    competition,
    on="business_name",
    how="left"
)

result = result.merge(
    direct_competition,
    on="business_name",
    how="left"
)

result = result.merge(
    density,
    on="business_name",
    how="left"
)


# --------------------------------------------------
# 4. Fill missing values
# --------------------------------------------------

numeric_columns = result.select_dtypes(
    include=np.number
).columns

result[numeric_columns] = (
    result[numeric_columns]
    .fillna(0)
)


# --------------------------------------------------
# 5. Normalize a feature to 0-100
# --------------------------------------------------

def normalize(series):

    minimum = series.min()
    maximum = series.max()

    if maximum == minimum:
        return pd.Series(
            50,
            index=series.index
        )

    return (
        (series - minimum)
        /
        (maximum - minimum)
        * 100
    )


# --------------------------------------------------
# 6. Demand score
# --------------------------------------------------

demand_features = [
    "healthcare_1km",
    "education_1km",
    "commercial_1km",
    "financial_1km",
    "transport_1km",
    "business_activity_1km"
]


result["demand_score"] = (
    result[demand_features]
    .apply(normalize)
    .mean(axis=1)
)


# --------------------------------------------------
# 7. Competition score
# --------------------------------------------------
# Higher competition = lower opportunity

result["competition_pressure"] = normalize(
    result["competitor_count_1km"]
)

result["competition_score"] = (
    100 - result["competition_pressure"]
)


# --------------------------------------------------
# 8. Direct competition pressure
# --------------------------------------------------

direct_columns = [
    "hotel_competitors_1km",
    "restaurant_competitors_1km",
    "cafe_competitors_1km",
    "fast_food_competitors_1km"
]

result["direct_competition_pressure"] = (
    result[direct_columns]
    .apply(normalize)
    .mean(axis=1)
)

result["direct_competition_score"] = (
    100 -
    result["direct_competition_pressure"]
)


# --------------------------------------------------
# 9. Density score
# --------------------------------------------------

result["density_pressure"] = normalize(
    result["business_density_1km"]
)

result["density_score"] = (
    100 - result["density_pressure"]
)


# --------------------------------------------------
# 10. Final Opportunity Score
# --------------------------------------------------

result["opportunity_score"] = (
    result["demand_score"] * 0.40
    +
    result["competition_score"] * 0.25
    +
    result["direct_competition_score"] * 0.20
    +
    result["density_score"] * 0.15
)


# --------------------------------------------------
# 11. Opportunity category
# --------------------------------------------------

def opportunity_category(score):

    if score >= 70:
        return "High Opportunity"

    elif score >= 50:
        return "Moderate Opportunity"

    else:
        return "Low Opportunity"


result["opportunity_category"] = (
    result["opportunity_score"]
    .apply(opportunity_category)
)


# --------------------------------------------------
# 12. Rank locations
# --------------------------------------------------

result["opportunity_rank"] = (
    result["opportunity_score"]
    .rank(
        ascending=False,
        method="min"
    )
    .astype(int)
)


# --------------------------------------------------
# 13. Display top locations
# --------------------------------------------------

top_locations = result.sort_values(
    "opportunity_score",
    ascending=False
).head(10)


print("\nTOP 10 EXPANSION OPPORTUNITIES")
print("-" * 60)

print(
    top_locations[
        [
            "opportunity_rank",
            "business_name",
            "category",
            "demand_score",
            "competition_score",
            "direct_competition_score",
            "density_score",
            "opportunity_score",
            "opportunity_category"
        ]
    ].to_string(index=False)
)


# --------------------------------------------------
# 14. Summary
# --------------------------------------------------

print("\n" + "=" * 60)
print("OPPORTUNITY SUMMARY")
print("=" * 60)

print(
    result["opportunity_category"]
    .value_counts()
)


# --------------------------------------------------
# 15. Save
# --------------------------------------------------

result = result.sort_values(
    "opportunity_score",
    ascending=False
)

result.to_csv(
    "data/expand_ai_opportunity_scores.csv",
    index=False
)

print("\nSaved successfully!")

print(
    "data/expand_ai_opportunity_scores.csv"
)

print("\nExpand AI opportunity scoring complete!")