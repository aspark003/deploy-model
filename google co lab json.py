import pandas as pd
import requests
import json
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, RandomForestRegressor
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, mean_squared_error, r2_score, mean_absolute_error
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.cluster import KMeans
import nltk
nltk.download('vader_lexicon')

http = "https://api.github.com"

repos = "https://api.github.com/search/repositories?q=python"
data = requests.get(repos)

all_items = []
for page in range(1,6):
    response = requests.get(repos, params={'q': 'python', 'per_page': 100, 'page': page})
    if response.status_code==200:
        all_items.extend(response.json().get('items', []))

http = pd.DataFrame(all_items)

pd.set_option('display.max_colwidth', None)
http.to_csv("http.csv", index=False)

#print(http.select_dtypes(include='bool').astype('int64').describe().to_string())
