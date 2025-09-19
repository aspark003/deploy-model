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


f = pd.read_csv("http.csv", encoding='utf-8-sig', engine='python')
pd.set_option('display.max_colwidth', None)
f.columns = f.columns.str.strip().str.lower()
f = f.drop(columns=['mirror_url', 'score','private','fork','allow_forking',  'disabled','has_issues','has_wiki','has_downloads','is_template','web_commit_signoff_required',
                    'created_at', 'updated_at', 'merges_url', 'archive_url', 'url', 'commits_url', 'contributors_url','forks_count', 'open_issues_count',
                    'watchers_count','keys_url','collaborators_url','hooks_url', 'issue_events_url', 'events_url', 'assignees_url',
                    'branches_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 'trees_url', 'statuses_url', 'languages_url',
                    'homepage', 'svn_url', 'clone_url', 'stargazers_url', 'subscribers_url', 'subscription_url', 'git_commits_url',
                    'forks_url', 'teams_url', 'tags_url', 'comments_url', 'issue_comment_url', 'contents_url', 'compare_url', 'downloads_url',
                    'pushed_at', 'git_url', 'ssh_url','node_id', 'issues_url', 'deployments_url','pulls_url',
                    'milestones_url', 'labels_url', 'releases_url','name', 'owner', 'html_url','default_branch', 'visibility', 'notifications_url'])

num_dtype = f.select_dtypes(include='number').columns.tolist()
bool_dtype = f.select_dtypes(include='bool').columns.tolist()
f[bool_dtype] = f[bool_dtype].astype('Int64')
obj_dtype = f.select_dtypes(include=['object', 'string']).columns.tolist()
#print(f[obj_dtype].describe().to_string()) # use describe to understand and remove unnecessary columns

def clean_obj(str_col):
    str_col = str_col.replace('^$', 'missing', regex=True)
    str_col = str_col.replace(r'[/\==\'\,\:\-\{\}\[\]\.]', ' ', regex=True).str.strip()
    str_col = str_col.replace(r'[^A-Za-z\s]', ' ', regex=True).str.strip()
    str_col = str_col.replace(r'[\t ]+', ' ', regex=True).str.strip()
    str_col = str_col.fillna('missing')
    str_col = str_col.str.strip().str.lower()
    return str_col

f[obj_dtype] = f[obj_dtype].apply(clean_obj)
sentiment = f.copy()
binn = f.copy()
#print(f.describe().to_string())

ss = StandardScaler()
fit_ss = ss.fit_transform(f[num_dtype])
scaled_f = pd.DataFrame(fit_ss, columns=num_dtype, index=f.index)
f[num_dtype] = scaled_f
#print(scaled_f)

f[obj_dtype] = f[obj_dtype].astype('category')
cat_cols = f.select_dtypes(include=['category']).columns.tolist()
#print(cat_cols)

oe = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
fit_oe = oe.fit_transform(f[cat_cols])
f[cat_cols] = pd.DataFrame(fit_oe, columns=cat_cols, index=f.index)
#print(f.head().to_string())

target = f['has_projects']
feature = f.drop(columns='has_projects')

X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=42)
random_forest = RandomForestClassifier(class_weight='balanced',random_state=42)
random_forest_fit = random_forest.fit(X_train, y_train)
target_predict = random_forest_fit.predict(X_test)
#print("Accuracy:\n",accuracy_score(y_test, target_predict)) #Verify how accurate your target is to feature

#print("Target Value:\n",target.value_counts(normalize=True)) #from 1 or 0, scores for each

#print("Classification:\n",classification_report(y_test,target_predict)) #based on the score, the target value is not very good

scaler = StandardScaler()
feature_scaled = pd.DataFrame(scaler.fit_transform(feature), columns=feature.columns, index=feature.index)

# Now split the scaled features
X_train, X_test, y_train, y_test = train_test_split(feature_scaled, target, test_size=0.2, random_state=42)

logistic_re = LogisticRegression(class_weight='balanced', max_iter=500, random_state=42)
logistic_re_fit = logistic_re.fit(X_train, y_train)
logistic_re_pre = logistic_re_fit.predict(X_test)
#print("Accuracy:\n", accuracy_score(y_test, logistic_re_pre)) #Verify how accurate your target is to feature

#print("Target Value:\n",target.value_counts(normalize=True)) #from 1 or 0, scores for each

#print("Classification:\n",classification_report(y_test,logistic_re_pre)) #based on the score, the target value is not very good


scaler = StandardScaler()
feature_scaled = pd.DataFrame(scaler.fit_transform(feature), columns=feature.columns, index=feature.index)
X_train, X_test, y_train, y_test = train_test_split(feature_scaled, target, test_size=0.2, random_state=42)

neighbor_class = KNeighborsClassifier(n_neighbors=5)
neighbor_fit = neighbor_class.fit(X_train, y_train)
neighbor_pre = neighbor_fit.predict(X_test)
#print("Accuracy:\n", accuracy_score(y_test, neighbor_pre)) #Verify how accurate your target is to feature

#print("Target:\n",target.value_counts(normalize=True)) #from 1 or 0, scores for each

#print("Classification:\n",classification_report(y_test,neighbor_pre)) #based on the score, the target value is not very good

scaler = StandardScaler()
feature_scaled = pd.DataFrame(scaler.fit_transform(feature), columns=feature.columns, index=feature.index)
X_train, X_test, y_train, y_test = train_test_split(feature_scaled, target, test_size=0.2, random_state=42)

decision_tree = DecisionTreeClassifier(class_weight='balanced', random_state=42)
decision_fit = decision_tree.fit(X_train, y_train)
decision_pre = decision_fit.predict(X_test)
#print("Accuracy:\n", accuracy_score(y_test, decision_pre)) #Verify how accurate your target is to feature

#print("Target:\n",target.value_counts(normalize=True)) #from 1 or 0, scores for each

#print("Classification:\n",classification_report(y_test,decision_pre)) #based on the score, the target value is not very good

scaler = StandardScaler()
feature_scaled = pd.DataFrame(scaler.fit_transform(feature), columns=feature.columns, index=feature.index)
X_train, X_test, y_train, y_test = train_test_split(feature_scaled, target, test_size=0.2, random_state=42)

gradient_class = GradientBoostingClassifier(random_state=42)
gradient_fit = gradient_class.fit(X_train, y_train)
gradient_pre = gradient_fit.predict(X_test)
#print("Accuracy:\n", accuracy_score(y_test, gradient_pre)) #Verify how accurate your target is to feature

#print("Target:\n",target.value_counts(normalize=True)) #from 1 or 0, scores for each

#print("Classification:\n",classification_report(y_test,gradient_pre)) #based on the score, the target value is not very good


scaler = StandardScaler()
feature_scaled = pd.DataFrame(scaler.fit_transform(feature), columns=feature.columns, index=feature.index)
X_train, X_test, y_train, y_test = train_test_split(feature_scaled, target, test_size=0.2, random_state=42)

gaussian = GaussianNB()
gaussian_fit = gaussian.fit(X_train, y_train)
gaussian_pre = gaussian.predict(X_test)
#print("Accuracy:\n", accuracy_score(y_test, gaussian_pre)) #Verify how accurate your target is to feature

#print("Target:\n",target.value_counts(normalize=True)) #from 1 or 0, scores for each

#print("Classification:\n",classification_report(y_test,gaussian_pre)) #based on the score, the target value is not very good

scaler = StandardScaler()
feature_scaled = pd.DataFrame(scaler.fit_transform(feature), columns=feature.columns, index=feature.index)

X_train, X_test, y_train, y_test = train_test_split(feature_scaled, target, test_size=0.2, random_state=42)

random_reg = RandomForestRegressor(random_state=42)
random_fit = random_reg.fit(X_train, y_train)
random_pre = random_fit.predict(X_test)

mse = mean_squared_error(y_test, random_pre)
r2 = r2_score(y_test, random_pre)
#print(f"Mean Squared Error:\n{mse:.4f}")

#print(f"R^2 Score:\n{r2:.4f}")


scaler = StandardScaler()
feature_scaled = scaler.fit_transform(feature)

kmeans = KMeans(n_clusters=3, random_state=42)

clusters = kmeans.fit_predict(feature_scaled)

feature['cluster'] = clusters

#print(feature['cluster'].value_counts())


models = {
    'Logistic Regression': LogisticRegression(class_weight='balanced', max_iter=1000, random_state=42),
    'KNN': KNeighborsClassifier(),
    'DTC': DecisionTreeClassifier(class_weight='balanced', random_state=42),
    'GBC': GradientBoostingClassifier(random_state=42),
    'GaussianNB': GaussianNB()
}

param_grids = {
    'Logistic Regression': {'C': [0.1, 1, 10]},
    'KNN': {'n_neighbors': [3, 5, 7]},
    'DTC': {'max_depth': [None, 5, 10]},
    'GBC': {'n_estimators': [50, 100], 'learning_rate': [0.1, 0.5]},
    'GaussianNB': {}  # no hyperparams to tune here
}

for name, model in models.items():
    grid = GridSearchCV(model, param_grids[name], cv=3)
    grid.fit(X_train, y_train)
    #print(f"{name} best params:\n{grid.best_params_}")

    #print(f"{name} best score:\n{grid.best_score_:.4f}\n")

sia = SentimentIntensityAnalyzer()
sentiment['vader_sentiment'] = sentiment['description'].apply(lambda x: sia.polarity_scores(str(x))['compound'])

#print(sentiment[['description', 'vader_sentiment']].head().to_string())

#print(binn.head().to_string())

bins = [-1, -0.05, 0.05, 1]
labels = ['Negative', 'Neutral', 'Positive']
sentiment['sentiment_bin'] = pd.cut(sentiment['vader_sentiment'], bins=bins, labels=labels)

#print(sentiment[['description', 'vader_sentiment', 'sentiment_bin']].head().to_string())


sentiment.to_csv("sav.csv", index=False)

#print(sentiment.head().to_string())

