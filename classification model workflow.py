# ================================
# Imports needed for classification
# ================================
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder, StandardScaler, MinMaxScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
# from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
# from sklearn.neural_network import MLPClassifier
# from sklearn.metrics import accuracy_score, precision_score ---- only works with binary(TRUE or FASLE), recall_score, f1_score
#


# Why classification is used:
# To put things into groups or categories (like yes/no, spam/not spam, dog/cat).

# When to use:
# When your target (the answer you want) is a label, not a number.
# Example: Predict if a movie will be a hit or flop, not how much money it makes.

# Rule:
# Use classification when the answer is a category. Use regression when the answer is a number.





# Logistic Regression
# Encode → convert categories (LabelEncoder, OneHotEncoder)
# Scale → ✅ StandardScaler or MinMaxScaler
# Split → train_test_split(features, target)
# Model → LogisticRegression()
# Evaluate → Accuracy, Precision, Recall, F1 Score, Error %
# Notes: Finds a linear boundary for classification
# Scores: Accuracy closer to 1 = stronger
# Multiclass → means the target has more than 2 categories (ex: genres = Action, Comedy, Drama, etc.)
# It’s multiclass because each movie belongs to ONE of many possible genres, not just yes/no

# micro → looks at all classes together as one big pool (overall performance)
# Example: If you predicted 100 movies, and 70 were correct → micro score = 70/100 = 0.70 (70%)
# Use when: You want the overall success rate, especially good if classes are imbalanced

# macro → averages precision/recall/F1 for each class equally (treats small and big classes the same)
# Example: If Class A = 50% correct, Class B = 90% correct → macro score = (0.5 + 0.9) ÷ 2 = 0.7 (70%)
# Use when: You want to treat all classes fairly, even if some are small

# weighted → averages precision/recall/F1 but gives more weight to big classes (handles imbalance)
# Example: If Class A has 90 movies with 90% accuracy, Class B has 10 movies with 50% accuracy → weighted score is closer to 0.9 than 0.5
# Use when: You want a balance between overall accuracy and class fairness, while handling imbalanced datasets

# samples → only for multi-label (when each row can have more than one label at the same time)
# Example: If a movie can be both “Comedy” and “Family,” samples checks accuracy for each label in each row, then averages them
# Use when: You have multi-label problems (like text tags, movie genres with more than one per movie)

# Accuracy (0.2758 ≈ 28%) → Out of all movies, the model guessed the correct genre only about 28% of the time.
# Precision (0.0761 ≈ 7.6%) → When the model *said* a movie was a certain genre, it was only right 7.6% of the time.
# Recall (0.2758 ≈ 28%) → Out of all movies that really were a genre, the model found them correctly 28% of the time.
# F1 (0.1193 ≈ 11.9%) → The balance between precision and recall is low (because precision is very poor).

# 👉 This means your model is guessing poorly, even though it sometimes catches the right genre.
# Likely your features (critic score + audience score) are not strong enough alone to predict genre.





# Decision Tree Classifier
# Encode → same as above
# Scale → 🚫 No scaling needed
# Split → train_test_split
# Model → DecisionTreeClassifier()
# Evaluate → Accuracy, Precision, Recall, F1 Score, Error %
# Notes: Splits data into groups using thresholds
# Scores: Accuracy closer to 1 = stronger

# Random Forest Classifier
# Encode → same as above
# Scale → 🚫 No scaling needed
# Split → train_test_split
# Model → RandomForestClassifier()
# Evaluate → Accuracy, Precision, Recall, F1 Score, Error %
# Notes: Builds many trees and averages them
# Scores: Accuracy usually higher than a single tree

# Gradient Boosting Classifier
# Encode → same as above
# Scale → 🚫 No scaling needed
# Split → train_test_split
# Model → GradientBoostingClassifier()
# Evaluate → Accuracy, Precision, Recall, F1 Score, Error %
# Notes: Sequential trees fix previous errors
# Scores: Accuracy often very high

# K-Nearest Neighbors (KNN) Classifier
# Encode → same as above
# Scale → ✅ StandardScaler or MinMaxScaler
# Split → train_test_split
# Model → KNeighborsClassifier()
# Evaluate → Accuracy, Precision, Recall, F1 Score, Error %
# Notes: Classifies based on nearest neighbors
# Scores: Accuracy depends on distance; scaling critical

# Support Vector Classifier (SVC)
# Encode → same as above
# Scale → ✅ StandardScaler or MinMaxScaler
# Split → train_test_split
# Model → SVC()
# Evaluate → Accuracy, Precision, Recall, F1 Score, Error %
# Notes: Finds best separating hyperplane
# Scores: Accuracy closer to 1 = stronger

# Naive Bayes Classifier
# Encode → same as above
# Scale → 🚫 No scaling needed
# Split → train_test_split
# Model → GaussianNB() / MultinomialNB() / BernoulliNB()
# Evaluate → Accuracy, Precision, Recall, F1 Score, Error %
# Notes: Uses probability and Bayes' theorem
# Scores: Works well with categorical or text data

# Neural Network Classifier (MLPClassifier)
# Encode → same as above
# Scale → ✅ StandardScaler or MinMaxScaler
# Split → train_test_split
# Model → MLPClassifier()
# Evaluate → Accuracy, Precision, Recall, F1 Score, Error %
# Notes: Learns complex patterns through layers
# Scores: Accuracy depends on dataset size/complexity
