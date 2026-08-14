🚀 Expand AI
Make Smarter Expansion Decisions.

Expand AI is a data-driven decision-support project designed to help hotels and restaurants identify promising locations for business expansion.

The project currently focuses on Karur, Tamil Nadu, and uses geographic, demand, competition, and business-density data to evaluate hospitality business opportunities.

🎯 Problem Statement

Hotels and restaurants often choose new locations based on intuition, experience, and limited market information.

Expand AI aims to make this process more data-driven by analyzing:

📍 Location
📊 Demand signals
🏪 Competition
📈 Business density
🏥 Nearby healthcare facilities
🎓 Education facilities
🛍️ Commercial activity
🏦 Banks and ATMs
🚌 Transportation
🏢 Business activity
💡 Project Objective

The main objective of Expand AI is to identify locations that may offer better expansion opportunities for hospitality businesses.

The system analyzes existing businesses and nearby location-based demand indicators to generate an initial opportunity score.

👥 Target Users

Expand AI is designed for:

🏨 Hotel owners
🍴 Restaurant owners
🚀 Entrepreneurs
💼 Business consultants
💰 Investors
📍 Current Project: Karur

The first version of Expand AI focuses on hospitality businesses in Karur, Tamil Nadu, India.

The project currently analyzes 44 hospitality businesses with valid geographic coordinates.

Business categories include:

Hotels
Restaurants
Fast Food
Cafes
📊 Data Sources

The current project uses geographic and business information collected from OpenStreetMap.

The data includes:

Hospitality Data
Business name
Business category
Location
Cuisine
Phone number
Street
Postcode
Opening hours
Website
Vegetarian information
Demand Indicators
Hospitals
Schools
Colleges
Shops
Banks
ATMs
Bus stations
Public transportation
Railway infrastructure
Offices
Other commercial activity
🔎 Analysis Pipeline

The project follows a step-by-step data analysis pipeline.

OpenStreetMap Data
↓
Data Collection
↓
Data Exploration
↓
Data Cleaning
↓
Business Mapping
↓
Competition Analysis
↓
Direct Competition Analysis
↓
Business Density Analysis
↓
Demand Data Collection
↓
Demand Feature Engineering
↓
Opportunity Scoring

🧹 1. Data Collection & Cleaning

Raw hospitality data is collected and transformed into a cleaner structured dataset.

The cleaned dataset contains:

Business name
Category
Latitude
Longitude
Cuisine
Phone
Street
Postcode
Opening hours
Website
Vegetarian information
Rooms
Source
🗺️ 2. Business Mapping

A geographic map was created using Folium to visualize hospitality businesses across the study area.

The map helps identify where businesses are concentrated geographically.

🏪 3. Competition Analysis

Competition is measured by counting nearby businesses within a 1 km radius.

This helps identify locations with:

High competition
Medium competition
Low competition
🎯 4. Direct Competition Analysis

Competition is also separated by business category.

For example:

Hotel competitors
Restaurant competitors
Cafe competitors
Fast-food competitors

This provides a more meaningful view of direct competition.

📈 5. Business Density Analysis

Business density measures how many hospitality businesses exist around a particular location.

A higher density indicates that many businesses are operating nearby.

This can help identify highly concentrated commercial areas.

📊 6. Demand Analysis

Demand signals are estimated using nearby location-based indicators.

The project currently considers:

Demand Feature	Example
Healthcare	Hospitals
Education	Schools & colleges
Commercial	Shops
Financial	Banks & ATMs
Transport	Bus & railway infrastructure
Business Activity	Offices & organizations
🧠 7. Feature Engineering

The raw demand information is converted into structured features.

Current demand features include:

Healthcare score
Education score
Commercial score
Financial score
Transport score
Business activity score

These features are combined into a total demand signal.

⭐ 8. Opportunity Scoring

Expand AI combines multiple signals to calculate an initial opportunity score.

The current scoring system considers:

Demand
Competition
Direct competition
Business density

The result is an initial classification such as:

🟢 High potential
🟡 Moderate opportunity
🔴 Low opportunity

The current scoring system is an early Version 1 approach and is not yet a machine-learning prediction model.

📌 Current Results

The current analysis produced:

45 cleaned hospitality records
44 businesses with valid coordinates
216 demand indicator records
Competition analysis
Direct competition analysis
Business density analysis
Demand feature analysis
Opportunity scoring

The current opportunity analysis identified:

18 Moderate Opportunity records
40 Low Opportunity records

These results should be treated as initial analytical signals, not final business investment recommendations.

🤖 Future Machine Learning Goal

The next stage of Expand AI is to develop a machine learning model that can estimate potential customer demand.

Potential features include:

Location
Business category
Nearby demand indicators
Competition
Business density
Commercial activity
Transportation access

The goal is to move from simple rule-based scoring toward a more data-driven predictive system.

💰 Future Financial Analysis

Future versions will add financial analysis such as:

Estimated customers
Average order value
Revenue
Operating costs
Profit
ROI
Investment requirement
Risk assessment

This will allow the system to connect location opportunity with financial feasibility.

🛠️ Technologies Used
🐍 Python
🐼 Pandas
🌍 GeoPandas
🗺️ Folium
🗺️ OpenStreetMap
🔧 Git
🐙 GitHub
📁 Project Structure

Expand AI/
│
├── Data/
│ ├── karur_hospitality_raw.csv
│ ├── karur_hospitality_clean.csv
│ ├── karur_competition_analysis.csv
│ ├── karur_direct_competition.csv
│ ├── karur_business_density.csv
│ ├── karur_demand_indicators.geojson
│ ├── karur_demand_analysis.csv
│ ├── karur_demand_features.csv
│ └── expand_ai_opportunity_scores.csv
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

🚀 Version 1 Status
Completed
 Karur hospitality data collection
 Data exploration
 Data cleaning
 Business mapping
 Competition analysis
 Direct competition analysis
 Business density analysis
 Demand data collection
 Demand feature engineering
 Opportunity scoring
 GitHub repository setup
Next Steps
 Improve demand estimation
 Add demographic data
 Add accessibility analysis
 Develop machine learning model
 Add financial calculations
 Build interactive dashboard
 Improve opportunity scoring
 Expand to additional locations
🔮 Future Vision

Expand AI aims to become a location intelligence platform that helps hospitality businesses answer:

"Where should I open my next business?"

Instead of relying only on intuition, the goal is to combine data + analytics + machine learning + financial analysis to provide transparent and actionable expansion insights.

📌 Project Status

Version 1 — Data Collection, Spatial Analysis & Opportunity Scoring

Built as a practical data science project using real geographic business data from Karur.

Built with Python & Data Science ❤️

Expand AI - Make Smarter Expansion Decisions.