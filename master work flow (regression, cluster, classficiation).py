# === MASTER ML WORKFLOW TREE (Regression + Classification + Clustering) ===

# ├── Step 0: Install packages
# │   pip install pandas scikit-learn category_encoders
# │
# ├── Step 1: Import tools
# │   import pandas as pd, numpy as np
# │   from sklearn.model_selection import train_test_split
# │   from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
# │   from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
# │   from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# │
# │   # Regression models
# │   from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet, SGDRegressor
# │   from sklearn.svm import SVR
# │   from sklearn.tree import DecisionTreeRegressor
# │   from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, HistGradientBoostingRegressor
# │   from sklearn.neighbors import KNeighborsRegressor
# │   from sklearn.neural_network import MLPRegressor
# │
# │   # Classification models
# │   from sklearn.linear_model import LogisticRegression, SGDClassifier, RidgeClassifier
# │   from sklearn.svm import SVC
# │   from sklearn.tree import DecisionTreeClassifier
# │   from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, HistGradientBoostingClassifier
# │   from sklearn.neighbors import KNeighborsClassifier
# │   from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
# │   from sklearn.neural_network import MLPClassifier
# │
# │   # Clustering models
# │   from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, MeanShift, SpectralClustering, Birch
# │   from sklearn.mixture import GaussianMixture
# │
# ├── Step 2: Shared Preprocessing
# │   df = pd.read_csv("file.csv")
# │   numbers → float64 (for math models)
# │   categories → category (for encoders)
# │   blanks → fill with mean/median or "missing"
# │   encode categories:
# │       Few → OneHotEncoder
# │       Ordered → OrdinalEncoder
# │       Many → TargetEncoder
# │   scale numbers if needed:
# │       StandardScaler → line models, SVM, NN
# │       MinMaxScaler → KNN
# │       RobustScaler → outliers
# │       Trees → no scaling needed
# │
# ├── Step 3A: Regression (predict numbers)
# │
# │   LinearRegression()          ✅ simple, fast   ❌ no curves
# │   Ridge()                     ✅ safer than linear ❌ still straight line
# │   Lasso()                     ✅ drops useless features ❌ may drop too much
# │   ElasticNet()                 ✅ mix Ridge+Lasso ❌ tricky tuning
# │   SGDRegressor()              ✅ huge data ❌ bad on small data
# │   SVR()                       ✅ finds curves ❌ slow on big data
# │   DecisionTreeRegressor()     ✅ easy to explain ❌ overfits fast
# │   RandomForestRegressor()     ✅ strong, works on messy data ❌ slower, harder to explain
# │   GradientBoostingRegressor() ✅ very accurate ❌ slow, needs tuning
# │   HistGradientBoostingRegressor() ✅ fast on big data ❌ hard to explain
# │   AdaBoostRegressor()         ✅ boosts weak models ❌ breaks with noisy data
# │   KNeighborsRegressor()       ✅ simple, no math training ❌ very slow on big data
# │   MLPRegressor()              ✅ learns complex patterns ❌ needs lots of data + tuning
# │
# ├── Step 3B: Classification (predict labels)
# │
# │   LogisticRegression()        ✅ yes/no problems, simple ❌ not for curvy data
# │   RidgeClassifier()           ✅ many features ❌ still linear
# │   SGDClassifier()             ✅ very big data ❌ small data, tuning needed
# │   SVC()                       ✅ clear boundaries, works on curves ❌ very slow on big data
# │   DecisionTreeClassifier()    ✅ easy to explain ❌ overfits fast
# │   RandomForestClassifier()    ✅ strong, handles messy data ❌ slower, harder to explain
# │   GradientBoostingClassifier()✅ very accurate ❌ slow, needs tuning
# │   HistGradientBoostingClassifier() ✅ fast on big data ❌ harder to explain
# │   AdaBoostClassifier()        ✅ boosts weak models ❌ bad with very noisy data
# │   KNeighborsClassifier()      ✅ simple, works with scaling ❌ very slow on big data
# │   GaussianNB()                ✅ continuous features ❌ features not independent
# │   MultinomialNB()             ✅ text, word counts ❌ no negative values
# │   BernoulliNB()               ✅ yes/no features ❌ not for continuous numbers
# │   MLPClassifier()             ✅ learns complex patterns ❌ needs lots of data + tuning
# │
# ├── Step 3C: Clustering (find groups, no labels)
# │
# │   KMeans()                    ✅ fast, common ❌ must pick k, only round shapes
# │   AgglomerativeClustering()   ✅ makes cluster tree ❌ very slow on big data
# │   DBSCAN()                    ✅ odd shapes, drops noise ❌ bad with very different sizes
# │   MeanShift()                 ✅ finds number of clusters itself ❌ slow on big data
# │   SpectralClustering()        ✅ non-linear boundaries ❌ needs k, slow
# │   Birch()                     ✅ big data, memory friendly ❌ less accurate
# │   GaussianMixture()           ✅ overlapping clusters ❌ assumes oval shapes
# │
# ├── Step 4: Train
# │   model.fit(X_train, y_train)   # regression / classification
# │   model.fit(X)                  # clustering
# │
# ├── Step 5: Predict
# │   preds = model.predict(X_test) # regression / classification
# │   labels = model.predict(X)     # clustering
# │
# └── Step 6: Evaluate
#     # Regression
#     r2_score, mean_squared_error, mean_absolute_error
#     # Classification
#     accuracy_score, precision_score, recall_score, f1_score
#     # Clustering
#     silhouette_score (how good clusters are), inertia_ (KMeans tightness)
