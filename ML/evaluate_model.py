import pandas as pd 
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Silhoutte analysis 

DATA_PATH = "Final_combined_data/county_ml_results.csv"

# Read in the County ML results
df = pd.read_csv(DATA_PATH)


# Select the features used by the K-Meand model 
ml_features = [
    "Poverty_Percent",
    "Unemployment_percent",
    "Did_Not_Graduate_percent"
]

# Standarize the features 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[ml_features])

# Evaluate the existing cluster assignment 
silhouette = silhouette_score(
    X_scaled,
    df["Cluster"]
)

print(f"Silhouette Score: {silhouette:.3f}")

# Compare the Silhouette Scores for different number of clusters 

silhouette_scores = {}

for k in range(2,9):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    cluster_labels = kmeans.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, cluster_labels)
    silhouette_scores[k] = score

print("\nSilhouette Scores:")
for k, score in silhouette_scores.items():
    print(f"{k} clusters: {score:.3f}")


# Davies-Bouldin Index 

# Calculate the index 
davies_bouldin = davies_bouldin_score(
    X_scaled,
    df["Cluster"]
)

print(f"\nDavies-Bouldin Index: {davies_bouldin:.3f}")

davies_bouldin_scores = {}

for k in range(2,7):
    kmeans = KMeans(
        n_clusters = k,
        random_state = 42,
        n_init = 10
    )

    cluster_labels = kmeans.fit_predict(X_scaled)

    score = davies_bouldin_score(X_scaled, cluster_labels)
    davies_bouldin_scores[k] = score

print ("\nDavies-Bouldin Scores:")
for k, score in davies_bouldin_scores.items():
    print(f"{k} clusters: {score:.3f}")


# Calinski-Harabasz

calinski_harabasz_scores = {}

for k in range(2,7):
    kmeans = KMeans(
        n_clusters= k,
        random_state= 42,
        n_init = 10
    )

    cluster_labels = kmeans.fit_predict(X_scaled)

    score = calinski_harabasz_score(X_scaled, cluster_labels)
    calinski_harabasz_scores[k] = score

print("\nCalinski-Harabasz Scores:")
for k,score in calinski_harabasz_scores.items():
    print(f"{k} clusters: {score:.3f}")


# Evaluate wheater clusters represent diffret levels of community need 
cluster_profile = df.groupby("Cluster")[ml_features].mean()

print("\nCluster Profiles:")
print(cluster_profile)

# Review what counties are present in each cluster
for cluster in sorted(df["Cluster"].unique()):
    print(f"\nCluster {cluster}:")

    cluster_counties = df[df["Cluster"] == cluster]["County"]
    cluster_counties = cluster_counties.sort_values()

    print(cluster_counties.to_string(index = False))

# calculate cluster size 
cluster_sizes = df["Cluster"].value_counts().sort_index()

print("\nCluster Sizes:")
print(cluster_sizes)