import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score, silhouette_samples

# Load the county-level data 
df = pd.read_csv("Final_combined_data/final_county_analysis.csv")

# Use the same features as the KMeans model 
features = [
    "Poverty_Percent",
    "Unemployment_percent",
    "Did_Not_Graduate_percent"
]

# Standerize the features 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Run KMeans with multiple diffrent random seeds 
random_states = [0, 10, 20, 30, 42]

cluster_results = []

for seed in random_states:
    kmeans = KMeans(
        n_clusters=4,
        random_state=seed,
        n_init=10
    )

    labels = kmeans.fit_predict(X_scaled)
    cluster_results.append(labels)

# Compare each run to the first run 
baseline = cluster_results[0]

for seed, labels in zip(random_states[1:], cluster_results[1:]):
    ari = adjusted_rand_score(baseline, labels)
    print(f"Random state {seed}: ARI = {ari:.3f}")


# Check the effects of standardization 
print("\nBefore Scaling:")
print(df[features].describe().loc[["mean", "std"]])

print("\nAfter Scaling:")
print(pd.DataFrame(X_scaled, columns = features).describe().loc[["mean", "std"]])


# Identify coutnies with the lowest indavidula silhouette scores 
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

labels = kmeans.fit_predict(X_scaled)

individual_shiloette = silhouette_samples(X_scaled, labels)

silhouette_results = pd.DataFrame({
    "County": df["County"],
    "Cluster": labels,
    "Silhouette_Score": individual_shiloette
})

# Sort from lowest to highest 
silhouette_results = silhouette_results.sort_values("Silhouette_Score")

print("\nCounties with the lowest silhouette scores:")
print(silhouette_results.head(10).to_string(index = False))