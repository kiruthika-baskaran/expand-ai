import pandas as pd
import folium

# Load cleaned dataset
df = pd.read_csv("data/karur_hospitality_clean.csv")

# Make sure coordinates are numeric
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# Remove records without valid coordinates
map_df = df.dropna(subset=["latitude", "longitude"]).copy()

print("Total businesses:", len(df))
print("Businesses with valid coordinates:", len(map_df))
print("Businesses skipped:", len(df) - len(map_df))

# Create map
karur_map = folium.Map(
    location=[10.9600, 78.0760],
    zoom_start=13
)

# Add businesses
for _, row in map_df.iterrows():

    category = row["category"]

    if category == "hotel":
        icon = "home"
    elif category == "restaurant":
        icon = "cutlery"
    elif category == "cafe":
        icon = "coffee"
    else:
        icon = "shopping-cart"

    # Handle missing values in popup
    cuisine = row["cuisine"] if pd.notna(row["cuisine"]) else "Not available"
    phone = row["phone"] if pd.notna(row["phone"]) else "Not available"

    popup_text = f"""
    <b>{row['business_name']}</b><br>
    Category: {category}<br>
    Cuisine: {cuisine}<br>
    Phone: {phone}
    """

    folium.Marker(
        location=[
            float(row["latitude"]),
            float(row["longitude"])
        ],
        popup=popup_text,
        tooltip=row["business_name"],
        icon=folium.Icon(icon=icon)
    ).add_to(karur_map)

# Save map
karur_map.save("karur_business_map.html")

print("\nMap created successfully!")
print("Open karur_business_map.html in your browser.")