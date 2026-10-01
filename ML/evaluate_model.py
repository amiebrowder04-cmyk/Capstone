import pandas as pd 
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

#Silhoutte Analysis (how well the counties seperated into their assigned clusters)

DATA_PATH = "Final_combined_data/county_ml_results.csv"

#reading in the the results from the trained model 
df = pd.read_csv(DATA_PATH)

#checking the data loaded correctly 
#print(df.head())

#Selecting the features that where used by the K-Meand model 
ML_Features = [
    "Poverty_Percent",
    "Unemployment_percent",
    "Did_Not_Graduate_percent"
]

#standardizing the features 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[ML_Features])

#Evaluate the existing cluster assignment 
silhouette = silhouette_score(
    X_scaled,
    df["Cluster"]
)

print(f"Silhouette Score: {silhouette:.3f}")

#Silhouette Score: 0.421
#The counties within each cluster have some meaninful similarity 
#The clusters are reasonably distinguished from one another 
#The clusters are not completly seperate, there is some over lap 


#Davis-Bouldin Index (how simialer each cluster is to it most similar neighboring cluster)

#calculating the index 
davies_bouldin = davies_bouldin_score(
    X_scaled,
    df["Cluster"]
)

print(f"Davies-Bouldin Index: {davies_bouldin:.3f}")

#Davies-Bouldin Index: 0.758
#The clusters have a reasonable degree of seperation relative to their within-cluster variation 

# comparing the Davis-Bouldin Index for diffrent numbers of clusters 

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

#Davies-Bouldin Scores:
#2 clusters: 0.952
#3 clusters: 0.781
#4 clusters: 0.758
#5 clusters: 0.655
#6 clusters: 0.573

# Calinski-Harabasz(betwee-cluster seperation relative to within-cluster dispersion)

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

#Evaluating wheater clusters represent diffret levels ofcommunity need 

cluster_profile = df.groupby("Cluster")[ML_Features].mean()

print("\nCluster Profiles:")
print(cluster_profile)

#Reviewing what coutnies ended up in each cluster 
for cluster in sorted(df["Cluster"].unique()):
    print(f"\nCluster {cluster}:")

    cluster_counties = df[df["Cluster"] == cluster]["County"]
    cluster_counties = cluster_counties.sort_values()

    print(cluster_counties.to_string(index = False))

# calculating cluster size 
cluster_sizes = df["Cluster"].value_counts().sort_index()

print("\nCluster Sizes:")
print(cluster_sizes)