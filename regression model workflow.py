# ================================
# Imports needed for regression
# ================================
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder, StandardScaler, MinMaxScaler, MaxAbsScaler, RobustScaler, PolynomialFeatures
# from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
# from sklearn.neighbors import KNeighborsRegressor
# from sklearn.svm import SVR
# from sklearn.neural_network import MLPRegressor
# from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Why regression is used:
# To predict a number or value (like price, age, income, temperature).

# When to use:
# When your target (the answer you want) is a number, not a category.
# Example: Predict how much money a movie will make, not if it is a hit or flop.

# Rule:
# Use regression when the answer is a number. Use classification when the answer is a category.



# Linear Regression
# Encode → convert categories (LabelEncoder, OneHotEncoder)
# Scale → ✅ StandardScaler (best for normal data), MinMaxScaler (if bounded range is preferred)
# Split → train_test_split(features, target)
# Model → LinearRegression()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Fits a straight line to predict a number
# Scores: R² closer to 1 = stronger; MAE ÷ Mean:
#   <10% Excellent 🚀, 10–25% Good 👍, 25–50% Fair 😐, >50% Poor 👎
# Use when: Data is numeric and roughly linear

# Polynomial Regression
# Encode → same as above
# Scale → ✅ StandardScaler (preferred), MinMaxScaler (alternative)
# Split → train_test_split
# Model → PolynomialFeatures + LinearRegression
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Extends linear regression by adding polynomial terms (x², x³, etc.)
# Scores: Same ranges as above
# Use when: Relationship between features and target is curved, not straight

# Ridge Regression
# Encode → same as above
# Scale → ✅ StandardScaler (best), MinMaxScaler (can also be used)
# Split → train_test_split
# Model → Ridge()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Linear regression with penalty on large coefficients (L2)
# Scores: Same ranges as above
# Use when: Features are correlated and you want to reduce overfitting

# Lasso Regression
# Encode → same as above
# Scale → ✅ StandardScaler (best), MinMaxScaler (alternative)
# Split → train_test_split
# Model → Lasso()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Linear regression with stronger penalty (L1) that can zero-out coefficients
# Scores: Same ranges as above
# Use when: You want both prediction and automatic feature selection

# ElasticNet Regression
# Encode → same as above
# Scale → ✅ StandardScaler (best), MinMaxScaler (alternative)
# Split → train_test_split
# Model → ElasticNet()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Mix of Ridge and Lasso penalties (L1 + L2)
# Scores: Same ranges as above
# Use when: Both correlation and feature selection matter

# Decision Tree Regressor
# Encode → same as above
# Scale → 🚫 No scaling needed (trees split directly on values)
# Split → train_test_split
# Model → DecisionTreeRegressor()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Splits data into groups, predicts a number by averaging values
# Scores: Same ranges as above
# Use when: Data is non-linear and you want interpretability

# Random Forest Regressor
# Encode → same as above
# Scale → 🚫 No scaling needed
# Split → train_test_split
# Model → RandomForestRegressor()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Builds many trees and averages them → more stable, less overfitting
# Scores: R² usually higher than a single tree; Error % same ranges
# Use when: You want stronger performance than one tree

# Gradient Boosting Regressor
# Encode → same as above
# Scale → 🚫 No scaling needed
# Split → train_test_split
# Model → GradientBoostingRegressor()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Builds trees one by one, each fixing mistakes of the previous
# Scores: Often very high R²; Error % same ranges
# Use when: You want high accuracy, even if training is slower

# K-Nearest Neighbors (KNN) Regressor
# Encode → same as above
# Scale → ✅ MinMaxScaler (best for distance), StandardScaler (works too)
# Split → train_test_split
# Model → KNeighborsRegressor()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Predicts a number by averaging nearby points
# Scores: Same ranges as above
# Use when: Relationship depends on local neighborhoods, not a formula

# Support Vector Regressor (SVR)
# Encode → same as above
# Scale → ✅ StandardScaler (preferred), MinMaxScaler (alternative)
# Split → train_test_split
# Model → SVR()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Finds a margin that best fits the data within a tolerance
# Scores: Same ranges as above
# Use when: Data has outliers or is high-dimensional

# Neural Network Regressor (MLPRegressor)
# Encode → same as above
# Scale → ✅ MinMaxScaler (preferred for neural nets), StandardScaler (works too)
# Split → train_test_split
# Model → MLPRegressor()
# Evaluate → R², MAE, MSE, MAE ÷ Mean (% error)
# Notes: Layers of nodes learn complex patterns
# Scores: Same ranges as above
# Use when: Data is large, complex, and non-linear

import pandas as pd
df = pd.read_csv("c:/Users/anton/OneDrive/school/wk2_movies.csv")

print(df.head().to_string())