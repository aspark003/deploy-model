# ================================
# Imports needed for clustering
# ================================
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder, StandardScaler, MinMaxScaler
# from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, MeanShift
# from sklearn.mixture import GaussianMixture
# from sklearn.metrics import silhouette_score

# Why clustering is used:
# Clustering → purpose is to find groups in data **without labels** (unsupervised).
# Example: Imagine you have 100 movies, but no genres. Clustering can group them by similar critic score, audience score, or budget.
# The model decides the groups for you — like “Group 1 = family movies, Group 2 = action movies,” even if you never told it.
# Use when → you don’t know the categories ahead of time, but you want to discover natural patterns in the data.




# K-Means Clustering
# Encode → convert categories (LabelEncoder, OneHotEncoder)
# Scale → ✅ StandardScaler or MinMaxScaler (important: uses distance)
# Split → 🚫 Not used (unsupervised learning, no target variable)
# Model → KMeans()
# Evaluate → Silhouette Score
# Notes: Groups data into k clusters by minimizing distance to cluster centers
# Scores: Silhouette closer to 1 = strong clusters; closer to 0 = overlapping; < 0 = wrong clustering
#   >0.7 Excellent 🚀, 0.5–0.7 Good 👍, 0.25–0.5 Fair 😐, <0.25 Poor 👎
# Use when: You expect spherical clusters and know/guess the number of clusters

# Agglomerative Clustering (Hierarchical)
# Encode → same as above
# Scale → ✅ StandardScaler or MinMaxScaler
# Split → 🚫 Not used
# Model → AgglomerativeClustering()
# Evaluate → Silhouette Score
# Notes: Merges points step by step into a hierarchy of clusters
# Scores: Same ranges as above
# Use when: You want tree-like grouping (dendrograms) or don’t want to pre-set clusters

# DBSCAN (Density-Based Spatial Clustering)
# Encode → same as above
# Scale → ✅ StandardScaler or MinMaxScaler
# Split → 🚫 Not used
# Model → DBSCAN()
# Evaluate → Silhouette Score
# Notes: Groups dense regions, marks sparse points as noise (outliers)
# Scores: Same ranges as above
# Use when: Data has irregular shapes or many outliers

# Mean Shift
# Encode → same as above
# Scale → ✅ StandardScaler or MinMaxScaler
# Split → 🚫 Not used
# Model → MeanShift()
# Evaluate → Silhouette Score
# Notes: Finds dense areas by shifting points toward cluster centers automatically
# Scores: Same ranges as above
# Use when: You don’t know the number of clusters ahead of time

# Gaussian Mixture Models (GMM)
# Encode → same as above
# Scale → ✅ StandardScaler or MinMaxScaler
# Split → 🚫 Not used
# Model → GaussianMixture()
# Evaluate → Silhouette Score, Log-Likelihood
# Notes: Uses probability; each point belongs to clusters with a probability instead of a hard label
# Scores: Silhouette Score ranges as above; higher log-likelihood = better fit
# Use when: Clusters overlap and boundaries are “soft”
