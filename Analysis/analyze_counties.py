import pandas as pd 


DATA_Path = "../Final_combined_data/county_ml_results.csv"

#reading in the final_combined_data
df = pd.read_csv(DATA_Path)

#checking the data loaded correctly 
#print(df.head())

#standarizing the nonprofit support measure 
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df["Support_Gap_Score"] = scaler.fit_transform(
    df[["People_Per_Nonprofit"]]
)

"""
# checking to make sure that the column was renamed 
print(
    df[[
        "County",
        "Needs_Score",
        "People_Per_Nonprofit",
        "Support_Gap_Score"
    ]].head(10)
)
"""
#calculating the final county score 
df["Final_Score"] = (
    (df["Needs_Score"] * 0.50)
    + (df["Support_Gap_Score"] * 0.50)
)

#displaying counties with the highest final scores 
print(
    df[[
        "County",
        "Needs_Score",
        "Final_Score"
    ]].sort_values("Final_Score", ascending = False).head(10)
)

#saving the results 
OUTPUT_PATH = "../Final_combined_data/final_county_analysis.csv"

df.to_csv(OUTPUT_PATH, index = False)

print(f"Final county analysis saved to {OUTPUT_PATH}")