# 🚀 Expand AI

### Make Smarter Expansion Decisions.

<p align="center">
  <strong>Location Intelligence for Hospitality Business Expansion</strong>
</p>

<p align="center">
  A data-driven decision-support system for identifying and evaluating hospitality expansion opportunities.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas" alt="Pandas">
  <img src="https://img.shields.io/badge/GeoPandas-Geospatial%20Analysis-139C5A" alt="GeoPandas">
  <img src="https://img.shields.io/badge/Folium-Interactive%20Maps-green" alt="Folium">
  <img src="https://img.shields.io/badge/OpenStreetMap-Data-orange?logo=openstreetmap" alt="OpenStreetMap">
  <img src="https://img.shields.io/badge/Status-Version%201-yellow" alt="Project Status">
</p>

---

## 📌 Overview

**Expand AI** is a location intelligence and decision-support project designed to help hotels, restaurants, entrepreneurs, consultants, and investors evaluate potential business expansion opportunities.

Instead of relying entirely on intuition, the project combines:

- Geographic analysis
- Hospitality business data
- Competition analysis
- Direct competition analysis
- Business density
- Demand indicators
- Feature engineering
- Opportunity scoring

The current implementation focuses on **Karur, Tamil Nadu, India** and represents the first stage of a larger location intelligence platform.

---

# 🎯 Problem Statement

Choosing a location for a new hotel or restaurant is a complex business decision.

Traditional expansion decisions may depend heavily on:

- Personal experience
- Intuition
- Local knowledge
- Limited competitor information
- Incomplete market research

This creates a challenge:

> **How can we use data to identify locations that may have stronger expansion potential?**

Expand AI addresses this problem by combining geographic and business information into a structured analytical workflow.

---

# 💡 Project Objective

The primary objective is to develop a data-driven framework that evaluates hospitality expansion opportunities based on measurable location characteristics.

The current system analyzes:

| Dimension | What is measured |
|---|---|
| 📍 Location | Geographic position |
| 🏪 Competition | Nearby hospitality businesses |
| 🎯 Direct Competition | Competition by business category |
| 📈 Business Density | Hospitality concentration |
| 🏥 Healthcare | Nearby hospitals and healthcare facilities |
| 🎓 Education | Schools and colleges |
| 🛍️ Commercial Activity | Nearby shops and businesses |
| 🏦 Financial Activity | Banks and ATMs |
| 🚌 Transportation | Bus and railway infrastructure |
| 🏢 Business Activity | Offices and organizations |

---

# 🗺️ Study Area

### Current Geographic Focus

**Karur, Tamil Nadu, India**

The current dataset contains:

- **45** cleaned hospitality records
- **44** businesses with valid coordinates
- **216** demand indicator records

Hospitality categories currently include:

- Hotels
- Restaurants
- Fast Food
- Cafes

---

# 📊 Data Source

The current geographic and business data is collected from:

**OpenStreetMap**

The project uses OpenStreetMap data to identify hospitality businesses and surrounding demand indicators.

### Hospitality Data

Collected attributes include:

- Business name
- Business category
- Latitude
- Longitude
- Cuisine
- Phone
- Street
- Postcode
- Opening hours
- Website
- Vegetarian information
- Rooms
- Source

### Demand Data

The demand dataset contains location-based indicators including:

- Hospitals
- Schools
- Colleges
- Shops
- Banks
- ATMs
- Bus stations
- Public transportation
- Railway infrastructure
- Offices
- Government organizations
- Other commercial activity

---

# 🧠 Analytical Methodology

Expand AI follows a structured spatial analytics pipeline.

```text
                    OpenStreetMap
                         │
                         ▼
                Data Collection
                         │
                         ▼
                 Data Exploration
                         │
                         ▼
                   Data Cleaning
                         │
                         ▼
               Geographic Mapping
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     Competition   Business Density   Demand
          │              │              │
          ▼              ▼              ▼
      Direct Competition Analysis
                         │
                         ▼
                 Feature Engineering
                         │
                         ▼
                  Opportunity Score
                         │
                         ▼
              Expansion Opportunity


🔄 Data Processing Pipeline

1️⃣ Data Collection

Hospitality businesses were collected from OpenStreetMap using geographic queries for the Karur study area.

The raw dataset contains geographic coordinates and available business attributes.

2️⃣ Data Exploration

The raw dataset was inspected to understand:

Dataset dimensions
Available columns
Data types
Missing values
Business categories
Tourism classifications
Named businesses
Data availability

This step helped determine which variables could be reliably used for downstream analysis.

3️⃣ Data Cleaning

The raw geographic dataset was transformed into a structured hospitality dataset.

The cleaned dataset contains standardized fields such as:

business_name
category
latitude
longitude
cuisine
phone
street
postcode
opening_hours
website
vegetarian
rooms
source

Invalid or incomplete geographic records were excluded from spatial analysis where necessary.

🗺️ Geographic Visualization

An interactive business map was created using Folium.

The map allows hospitality businesses to be visualized geographically and provides a foundation for spatial analysis.

Output:

karur_business_map.html

🏪 Competition Analysis

Competition is calculated by examining nearby hospitality businesses within a 1 km radius.

This produces a local competition measure for each business.

Example interpretation

Low nearby businesses
        ↓
Lower observed competition

High nearby businesses
        ↓
Higher observed competition

The analysis helps identify areas with concentrated hospitality activity.

🎯 Direct Competition Analysis

General competition does not always represent direct competition.

For example, a restaurant may compete more directly with other restaurants than with hotels.

Therefore, Expand AI separately measures competition by category:

Hotel competitors
Restaurant competitors
Cafe competitors
Fast-food competitors

This provides a more granular view of the competitive environment.

📈 Business Density Analysis

Business density measures the concentration of hospitality businesses around a location.

The current implementation evaluates the number of businesses within a 1 km radius.

This creates a spatial density feature that can be used alongside demand and competition indicators.

📊 Demand Signal Analysis

Demand is approximated using nearby geographic indicators.

The current system considers:

Healthcare

Nearby hospitals and healthcare facilities.

Education

Schools and colleges.

Commercial Activity

Nearby shops and commercial establishments.

Financial Activity

Banks and ATMs.

Transportation

Bus and railway infrastructure.

Business Activity

Offices and organizations.

These indicators are converted into numerical features for each hospitality location.

🧬 Feature Engineering

Raw geographic information is transformed into analytical features.

Current engineered features include:

healthcare_1km
education_1km
commercial_1km
financial_1km
transport_1km
business_activity_1km
total_demand_signals

These features provide a structured representation of the surrounding environment of each hospitality business.

⭐ Opportunity Scoring

The current Version 1 system combines multiple analytical dimensions into an initial opportunity score.

The scoring framework considers:

Demand
   +
Competition
   +
Direct Competition
   +
Business Density
   ↓
Opportunity Score

The resulting score is used to classify locations into opportunity categories.

Current categories
🟢 High potential
🟡 Moderate Opportunity
🔴 Low Opportunity

Important: The current opportunity score is a rule-based analytical framework. It is not yet a machine-learning prediction model and should not be interpreted as a definitive investment recommendation.

📌 Current Results

The current analysis produced:

| Metric                            | Result |
| --------------------------------- | -----: |
| Raw hospitality records           |     47 |
| Clean hospitality records         |     45 |
| Businesses with valid coordinates |     44 |
| Demand indicator records          |    216 |
| Hospitality categories            |      4 |
| Competition analysis              |      ✅ |
| Direct competition analysis       |      ✅ |
| Business density analysis         |      ✅ |
| Demand feature engineering        |      ✅ |
| Opportunity scoring               |      ✅ |

Opportunity Analysis

Current scoring produced:

18 Moderate Opportunity records
40 Low Opportunity records

These are analytical outputs from the current scoring framework and should be interpreted within the limitations of the available data.

⚠️ Current Limitations

The current Version 1 system has several limitations.

Data Coverage

OpenStreetMap coverage is not guaranteed to be complete or uniform across all locations.

Demand Estimation

Demand is currently approximated using nearby geographic indicators rather than actual customer transaction data.

Competition

Competition is measured using geographic proximity and available business categories.

Financial Analysis

Revenue, profit, ROI, and investment risk are not yet calculated using real financial data.

Machine Learning

The current opportunity score is rule-based and does not yet represent a trained predictive model.

🤖 Machine Learning Roadmap

A major future objective is to develop a machine learning model for demand prediction.

Potential features include:

Location
Business Category
Competition
Business Density
Healthcare Activity
Education Activity
Commercial Activity
Financial Activity
Transportation
Business Activity

Potential target variables could eventually include:

Customer demand
Estimated footfall
Revenue potential
Business performance

The final target will depend on the availability of reliable historical business data.

💰 Financial Intelligence Roadmap

Future versions will extend the system beyond location analysis.

Potential financial outputs include:

Estimated Customers
        ↓
Average Order Value
        ↓
Estimated Revenue
        ↓
Operating Costs
        ↓
Estimated Profit
        ↓
ROI
        ↓
Investment Risk

This would allow Expand AI to evaluate both:

"Is this location attractive?"

and

"Is this expansion financially viable?"

🏗️ Future System Architecture

The long-term vision is:

                DATA SOURCES
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
   Geographic     Business     Financial
      Data          Data          Data
        │            │            │
        └────────────┼────────────┘
                     ▼
              Data Processing
                     │
                     ▼
            Feature Engineering
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     Demand      Competition    Location
     Model         Model         Model
        │            │            │
        └────────────┼────────────┘
                     ▼
              Opportunity Model
                     │
                     ▼
             Financial Analysis
                     │
                     ▼
              Risk Assessment
                     │
                     ▼
            Business Recommendation


📁 Project Structure

Expand AI/
│
├── Data/
│   ├── karur_hospitality_raw.csv
│   ├── karur_hospitality_clean.csv
│   ├── karur_competition_analysis.csv
│   ├── karur_direct_competition.csv
│   ├── karur_business_density.csv
│   ├── karur_demand_indicators.geojson
│   ├── karur_demand_analysis.csv
│   ├── karur_demand_features.csv
│   └── expand_ai_opportunity_scores.csv
│
├── get_karur_data.py
├── explore_data.py
├── clean_data.py
├── karur_business_map.py
├── competition_analysis.py
├── direct_competition.py
├── business_density.py
├── demand_data.py
├── demand_analysis.py
├── demand_features.py
├── inspect_demand.py
├── opportunity_score.py
│
├── karur_business_map.html
├── README.md
└── .gitignore

🛠️ Technology Stack

| Technology    | Purpose             |
| ------------- | ------------------- |
| Python        | Core development    |
| Pandas        | Data manipulation   |
| GeoPandas     | Geospatial analysis |
| Folium        | Interactive maps    |
| OpenStreetMap | Geographic data     |
| Git           | Version control     |
| GitHub        | Project repository  |


🚀 Version 1 Progress
Completed
 Hospitality data collection
 Data exploration
 Data cleaning
 Geographic visualization
 Competition analysis
 Direct competition analysis
 Business density analysis
 Demand data collection
 Demand feature engineering
 Opportunity scoring
 GitHub repository setup

In Progress / Planned
 Improve demand estimation
 Add demographic data
 Improve accessibility analysis
 Add historical business performance data
 Develop demand prediction model
 Add financial modeling
 Add ROI estimation
 Add risk scoring
 Build interactive dashboard
 Expand to additional cities

🔮 Future Vision

The long-term goal of Expand AI is to evolve from a spatial analytics project into a complete hospitality location intelligence platform.

The system aims to answer:

"Where should I open my next business?"

using a combination of:

Data + Spatial Analytics + Machine Learning + Financial Analysis

The final goal is not simply to produce a score.

It is to provide a transparent explanation of why a location may represent a particular business opportunity.

📚 Project Learning Areas

This project provides practical experience across:

Data Collection
Data Cleaning
Exploratory Data Analysis
Geospatial Data Analysis
Feature Engineering
Spatial Competition Analysis
Business Intelligence
Decision Support Systems
Machine Learning Preparation
Git & GitHub

📍 Project Status

Version 1 — Spatial Data Collection, Analysis & Opportunity Scoring

The current version establishes the data and analytical foundation required for future demand prediction, financial modeling, and interactive decision support.

👩‍💻 Author

Kiruthika Baskaran

Data Science | AI | Business Analytics

⭐ Project Philosophy

Complex problems. Simple explanations. Data-driven decisions.

🚀 Expand AI

Make Smarter Expansion Decisions.