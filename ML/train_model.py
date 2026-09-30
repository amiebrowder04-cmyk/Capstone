import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import wandb



DATA_PATH = "Final_combined_data/final_combined_data.csv"

#reading in the final_combined_data table  
df = pd.read_csv(DATA_PATH)

#checking to make sure it loaded 
#print(df.head())

#selecting the variable that the model will use 
ML_Features = [
    "Poverty_Percent",
    "Unemployment_percent",
    "Did_Not_Graduate_percent"
]

#setting the features to X
X = df[ML_Features]

#checking to make sure that the features loaded 
#print(X.head())

#Standarizing the features 
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

#checking diffrent clusters to determin which one will be best for our data 

from sklearn.metrics import silhouette_score
"""
silhouette_scores = {}

for k in range(2, 7):
    kmeans = KMeans(
        n_clusters = k,
        random_state = 42,
        n_init = 10
    )

    cluster_labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, cluster_labels)
    silhouette_scores[k] = score 

#printing the results
print("/n Silhouette Scores:")
for k, score in silhouette_scores.items():
    print(f"{k} clusters: {score: .3f}")

#results 
# 2 clusters:  0.358
# 3 clusters:  0.419
# 4 clusters:  0.421 (We will use 4 clusters becasue it produced the best results)
# 5 clusters:  0.409
# 6 clusters:  0.409

"""
#starting a WandB experiment run 
wandb.init(
    project = "wa-county-needs",
    config = {
        "model" : "KMeans",
        "n_cluster" : 4,
        "random_state" : 42,
        "n_init": 10
    }
)



# creating the final k-means model with 4 clusters 
kmeans = KMeans(
    n_clusters = 4,
    random_state= 42,
    n_init= 10  
)

#training the model and assigning each coutnry to a cluster
cluster_labels = kmeans.fit_predict(X_scaled)

silhouette = silhouette_score(X_scaled, cluster_labels)

#loging the silhouette in wandb
wandb.log({
    "silhouette_score": silhouette
})

#Adding the cluster assignment to the coutny data
df["Cluster"] = cluster_labels

"""
#printing the counties by cluster 
print(df[["County", "Poverty_Percent", "Unemployment_percent", "Did_Not_Graduate_percent", "Cluster"]].sort_values("Cluster"))

#Calculating the average of each of the custers

cluster_summary =df.groupby("Cluster")[ML_Features].mean()

print("\n Cluster Averages:")
print(cluster_summary)

 Cluster Averages:
         Poverty_Percent  Unemployment_percent  Did_Not_Graduate_percent
Cluster
0              19.600000              3.898227                 19.603065
1               8.608333              4.490516                  8.598521
2              12.460000              5.228410                 12.461591
3              13.712500              7.325186                 13.706426

"""
# creating the needs score 
df["Needs_Score"] = X_scaled.mean(axis = 1)

"""
# checking the results 
print(
    df[[
        "County",
        "Poverty_Percent",
        "Unemployment_percent",
        "Did_Not_Graduate_percent",
        "Needs_Score",
        "Cluster"

    ]].sort_values("Needs_Score", ascending = False).head(10)
)
"""
# saving the ML results 
OUTPUT_PATH = "Final_combined_data/county_ml_results.csv"

df.to_csv(OUTPUT_PATH, index = False)

print(f"ML results saved to {OUTPUT_PATH}")