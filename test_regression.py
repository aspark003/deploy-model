import pandas as pd
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.linear_model import LinearRegression
from scipy import sparse
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

data = pd.read_csv("c:/Users/anton/OneDrive/school/disney.csv", encoding='utf-8-sig', engine='python')
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_rows", None)
data = data.drop(columns=['release_date','genre','mpaa_rating'])



numeric = data[['total_gross','inflation_adjusted_gross']]
ss = StandardScaler()
ss_fit = ss.fit_transform(numeric)
ss_df = pd.DataFrame(ss_fit,columns=['total_gross', 'inflation_adjusted_gross'],index=data.index)
data = data.drop(columns=['total_gross', 'inflation_adjusted_gross']).join(ss_df)

feature = data.drop(columns=['movie_title','inflation_adjusted_gross'])
target = data['total_gross']
add_title = data['movie_title']

X_train, X_test, y_train, y_test, titles_train, titles_test = train_test_split(feature, target, add_title, test_size=0.3, random_state=42)
lr = LinearRegression()
lr_fit = lr.fit(X_train, y_train)
pre = lr_fit.predict(X_test)
data = pd.DataFrame({'Movie Title': titles_test, 'Actual': y_test, 'Predict': pre})

print(data.head())
print(mean_squared_error(y_test, pre))
print(r2_score(y_test, pre))
print(mean_absolute_error(y_test, pre))




