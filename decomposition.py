# ================================
# Imports needed for decomposition
# ================================
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, MinMaxScaler
# from sklearn.decomposition import PCA, TruncatedSVD, NMF, LatentDirichletAllocation

# PCA (Principal Component Analysis)
# Encode → Use OneHotEncoder or LabelEncoder if categories, else none
# Scale → ✅ Use StandardScaler (PCA needs even scales)
# Split → 🚫 Not used (no target variable)
# Model → Use PCA() from sklearn.decomposition
# Evaluate → Explained Variance Ratio (how much info is kept)
# Notes: Turns many columns into fewer “summary columns.”
# Example: Instead of 100 test scores, PCA might find 2–3 “main skills.”
# Scores: >90% variance Excellent 🚀, 75–90% Good 👍, 50–75% Fair 😐, <50% Poor 👎
# Use when: You have too many numeric features and want to shrink them.

# Truncated SVD (Singular Value Decomposition)
# Encode → Use OneHotEncoder if categories, else none (often used with text TF-IDF, no encoder needed)
# Scale → ✅ Use StandardScaler or MinMaxScaler
# Split → 🚫 Not used
# Model → Use TruncatedSVD() from sklearn.decomposition
# Evaluate → Explained Variance Ratio
# Notes: Works like PCA but better for text data with lots of zeros.
# Example: From thousands of words, it can find 20–50 “main concepts.”
# Scores: Same ranges as PCA
# Use when: Data is very big and sparse (like bag-of-words or TF-IDF).

# NMF (Non-negative Matrix Factorization)
# Encode → Use OneHotEncoder if categories, else none (needs numeric and positive values)
# Scale → ✅ Use MinMaxScaler (keeps numbers positive)
# Split → 🚫 Not used
# Model → Use NMF() from sklearn.decomposition
# Evaluate → Reconstruction Error (smaller = better)
# Notes: Breaks data into smaller parts, no negatives allowed.
# Example: A face picture can be split into “nose,” “eyes,” “mouth.”
# Scores: Error close to 0 = Excellent 🚀, higher error = worse
# Use when: Features can’t be negative (word counts, money, pixels).

# Latent Dirichlet Allocation (LDA)
# Encode → Usually none (works with raw counts or TF-IDF directly)
# Scale → 🚫 No scaling needed
# Split → 🚫 Not used
# Model → Use LatentDirichletAllocation() from sklearn.decomposition
# Evaluate → Log-Likelihood (higher = better), Perplexity (lower = better)
# Notes: Finds hidden “topics” in text.
# Example: News articles might split into topics like “sports,” “politics,” “movies.”
# Scores: Lower perplexity = better topics; high perplexity = weak grouping
# Use when: You want to discover topics in text data.
