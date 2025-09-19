import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("c:/Users/anton/OneDrive/school/disney.csv", encoding='utf-8-sig', engine='python')
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", None)
df.columns = df.columns.str.replace('_', ' ', regex=True).str.lower().str.strip()

df = df.drop(columns=['release date', 'runtime minutes', 'release year', 'total gross', 'inflation adjusted gross', 'budget'])
df['genre'] = df['genre'].fillna('missing')
df['mpaa rating'] = df['mpaa rating'].fillna('missing')

le = LabelEncoder()
fit_le = le.fit_transform(df['genre'])
le_df = pd.DataFrame(fit_le, columns=['genre'], index=df.index)


num_col = df.select_dtypes(include='number').columns.tolist()

ss = StandardScaler()
ss_fit = ss.fit_transform(df[num_col])
ss_df = pd.DataFrame(ss_fit, columns=num_col, index=df.index)
df = le_df.join(ss_df)
#print(df.head().to_string())

feature = df.drop(columns=['genre'])
target = df['genre']

X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=42)

lr = LogisticRegression()
fit = lr.fit(X_train, y_train)
pre_fit = fit.predict(X_test)
#print(pre_fit)
#print("Accuracy Score: ", accuracy_score(y_test, pre_fit))
#print("Precision Score: ", precision_score(y_test, pre_fit)) #does not work bc its more than 2 values
#print("Precision Score (macro): ", precision_score(y_test, pre_fit, average='macro')) # for multi class
#print("Precision Score (weighted): ", precision_score(y_test, pre_fit, average='weighted')) # for multi class
#print("Precision Score (micro): ", precision_score(y_test, pre_fit, average='micro')) # for multi class
#print("Recall score: ", recall_score(y_test, pre_fit, average = 'micro'))
#print("Recall score: ", recall_score(y_test, pre_fit, average = 'micro'))
#print("Recall score: ", recall_score(y_test, pre_fit, average = 'weighted'))
#print("F1 score - micro: ", f1_score(y_test, pre_fit, average='micro'))
#print("F1 score - micro: ", f1_score(y_test, pre_fit, average = 'micro'))
#print("F1 score - weighted: ", f1_score(y_test, pre_fit, average = 'weighted'))

result = pd.DataFrame({'Accuracy': [accuracy_score(y_test, pre_fit)],
                       'Precision': [precision_score(y_test, pre_fit, average='weighted')],
                       'Recall': [recall_score(y_test, pre_fit, average='weighted')],
                       'F1': [f1_score(y_test, pre_fit, average='weighted')]})

print(result)
#print(df.isna().sum())
#print(df.dtypes)
#print(df.head().to_string())