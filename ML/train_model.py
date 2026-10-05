import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import wandb

N_CLUSTERS = 4
RANDOM_STATE = 42
N_INIT = 10


DATA_PATH = "Final_combined_data/final_combined_data.csv"

#Read in the final_combined_data  
df = pd.read_csv(DATA_PATH)


#Select the variables for the model 
ml_features = [
    "Poverty_Percent",
    "Unemployment_percent",
    "Did_Not_Graduate_percent"
]

# Set the features to X
X = df[ml_features]


#Standarize the features 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


#Start a WandB experiment run 
wandb.init(
    project = "wa-county-needs",
    config = {
        "model" : "KMeans",
        "n_clusters" : N_CLUSTERS,
        "random_state" : RANDOM_STATE,
        "n_init": N_INIT
    }
)


# Create the final k-means model with 4 clusters 
kmeans = KMeans(
    n_clusters = N_CLUSTERS,
    random_state= RANDOM_STATE,
    n_init= N_INIT 
)

# Train the model and assigning each coutnry to a cluster
cluster_labels = kmeans.fit_predict(X_scaled)

silhouette = silhouette_score(X_scaled, cluster_labels)

#Log the silhouette in W&B
wandb.log({
    "silhouette_score": silhouette
})

#Add the cluster assignment to the  county data
df["Cluster"] = cluster_labels

# Create the needs score 
df["Needs_Score"] = X_scaled.mean(axis = 1)


# Save the results of the ML model 
OUTPUT_PATH = "Final_combined_data/county_ml_results.csv"

df.to_csv(OUTPUT_PATH, index = False)

print(f"ML results saved to {OUTPUT_PATH}")

#Close the W&B run 
wandb.finish()
