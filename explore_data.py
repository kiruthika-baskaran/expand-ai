import pandas as pd

# Load the raw dataset
df = pd.read_csv("data/karur_hospitality_raw.csv")

print("=" * 60)
print("EXPAND AI - KARUR HOSPITALITY DATA EXPLORATION")
print("=" * 60)

# 1. Dataset size
print("\n1. DATASET SHAPE")
print(df.shape)

# 2. Column names
print("\n2. COLUMNS")
for column in df.columns:
    print("-", column)

# 3. First 10 records
print("\n3. FIRST 10 RECORDS")
print(df.head(10).to_string())

# 4. Data types
print("\n4. DATA TYPES")
print(df.dtypes)

# 5. Missing values
print("\n5. MISSING VALUES")
missing = df.isnull().sum()
print(missing[missing > 0].sort_values(ascending=False))

# 6. Non-missing percentage
print("\n6. DATA AVAILABILITY (%)")
availability = (df.notnull().mean() * 100).sort_values(ascending=False)
print(availability)

# 7. Business types
print("\n7. AMENITY TYPES")
print(df["amenity"].value_counts(dropna=False))

# 8. Tourism types
print("\n8. TOURISM TYPES")
print(df["tourism"].value_counts(dropna=False))

# 9. Named businesses
print("\n9. NAMED BUSINESSES")
if "name" in df.columns:
    print(df["name"].dropna().to_string(index=False))

print("\n" + "=" * 60)
print("EXPLORATION COMPLETE")
print("=" * 60)