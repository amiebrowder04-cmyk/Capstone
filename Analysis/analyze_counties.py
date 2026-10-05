import pandas as pd 
from sklearn.preprocessing import StandardScaler


DATA_PATH = "Final_combined_data/county_ml_results.csv"

# Read in the County ML Results
df = pd.read_csv(DATA_PATH)

# Standarize the People Per Nonprofit and create the Support Gap Score 
scaler = StandardScaler()

df["Support_Gap_Score"] = scaler.fit_transform(
    df[["People_Per_Nonprofit"]]
)

# Calculate the Final Score
df["Final_Score"] = (
    (df["Needs_Score"] * 0.50)
    + (df["Support_Gap_Score"] * 0.50)
)

# Save the results into final coutny analysis 
OUTPUT_PATH = "Final_combined_data/final_county_analysis.csv"

df.to_csv(OUTPUT_PATH, index = False)

print(f"Final county analysis saved to {OUTPUT_PATH}")

# Save the top 3 counties to a CSV file 
top_counties = df[[
    "County",
    "Cluster",
    "Needs_Score",
    "Support_Gap_Score",
    "Final_Score"
]].sort_values("Final_Score", ascending =False)
top_3 = top_counties.head(3).copy()

top_3.insert(0, "Rank", range(1, 4))

# Save the top 3 counties to a CSV file 
TOP_3_PATH = "Final_combined_data/top_3_counties.csv"

top_3.to_csv(TOP_3_PATH, index =False)
print(f"Top 3 counties saved to {TOP_3_PATH}")