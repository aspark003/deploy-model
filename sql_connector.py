import mysql.connector
import pandas as pd
from sqlalchemy import create_engine
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.metrics import r2_score,mean_absolute_error, mean_squared_error
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.inspection import permutation_importance


pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_row', None)
engine = create_engine("mysql+pymysql://root:Laurapark%40%2303@localhost/service")



df = pd.read_sql("SELECT * FROM service_data", engine)

connect = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Laurapark@#03',
    database = 'service')

cursor = connect.cursor()
cursor.execute('select* from service_data')
rows = cursor.fetchall()

#for row in rows:
    #print(row)


#df.to_csv("c:/Users/anton/OneDrive/school/service_data.csv", index=False)

data = pd.read_csv("c:/Users/anton/OneDrive/school/service_data.csv", encoding='utf-8-sig', engine='python')

#print(data.head().to_string())

data.columns = data.columns.str.replace('_', ' ', regex=True).str.lower().str.strip()
#print(data.columns.tolist())
data = data.drop(columns=['diagnosis code', 'payment type', 'follow up required', 'patient id',
                          'visit date','provider id', 'treatment'])

numeric = data[['visit cost', 'lab result value','visit duration','patient age']]

ss = StandardScaler()
ss_fit = ss.fit_transform(numeric)
ss_df = pd.DataFrame(ss_fit, columns=['visit cost', 'lab result value','visit duration','patient age'],
                     index=data.index)
data = data.drop(columns=['visit cost', 'lab result value','visit duration','patient age']).join(ss_df)

feature = data.drop(columns=['service type','satisfaction score'])
target = data['satisfaction score']
service_type = data['service type']

X_train, X_test, y_train, y_test, service_train, service_test = train_test_split(feature, target, service_type, test_size=0.2, random_state=42)

le = LinearRegression()
le_fit = le.fit(X_train,y_train)
le_pre = le_fit.predict(X_test)

pred_ict = pd.DataFrame({'Service Type': service_test,
                        'Actual': y_test,
                         'Predict': le_pre})

sort_pre = pred_ict.sort_values('Actual', ascending=False)

coef_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Coefficient': le_fit.coef_
}).sort_values('Coefficient', ascending=False)

print(coef_df)

#print("\nPREDICT SCORE:\n",sort_pre.head())
#print("R2 SCORE: ", r2_score(y_test, le_pre))
#print("MEAN SQUARED: ", mean_squared_error(y_test, le_pre))
#print("MEAN ABSOLUTE: ", mean_absolute_error(y_test, le_pre))
#print(data.head().to_string())
#print(data.dtypes)

poly = PolynomialFeatures(degree=2)
train_p = poly.fit_transform(X_train)
test_p = poly.transform(X_test)

lr = LinearRegression()
lr_fit = lr.fit(train_p, y_train)
lr_pre = lr_fit.predict(test_p)

result = pd.DataFrame({'Service Type': service_test,
                        'Actual': y_test,
                         'Predict': lr_pre})
sort_poly = result.sort_values('Actual', ascending=False)
#print(sort_poly)
#print("R2 Score:\n",r2_score(y_test, lr_pre))
#print("Mean Squared:\n",mean_squared_error(y_test, lr_pre))
#print("Mean Absolute:\n",mean_absolute_error(y_test, lr_pre))

rid_ge = Ridge(alpha=1.0, fit_intercept=True)
fit_rid_ge = rid_ge.fit(X_train, y_train)
pre_fit_rid = fit_rid_ge.predict(X_test)

dis = pd.DataFrame({'Service Type': service_test,
                        'Actual': y_test,
                         'Predict': pre_fit_rid})
sort_ridge = dis.sort_values('Actual', ascending=False)

#print(sort_ridge.head())
#print("R2 Score:\n", r2_score(y_test, pre_fit_rid))
#print("Mean Squared:\n",mean_squared_error(y_test, pre_fit_rid))
#print("Mean Absolute:\n", mean_absolute_error(y_test, pre_fit_rid))

la_sso = Lasso()
la_fit = la_sso.fit(X_train, y_train)
pre_lasso = la_fit.predict(X_test)

lass_o = pd.DataFrame({'Service Type': service_test,
                        'Actual': y_test,
                         'Predict': pre_lasso})
sort_lasso = lass_o.sort_values('Actual', ascending=False)
#print(sort_lasso.head())
#print(r2_score(y_test, pre_lasso))

dt = DecisionTreeRegressor(random_state=42)
dt_fit = dt.fit(X_train, y_train)
dt_pre = dt_fit.predict(X_test)

dt_tree = pd.DataFrame({'Service Type': service_test,
                        'Actual': y_test,
                        'Predict': dt_pre})

dt_sort = dt_tree.sort_values('Actual', ascending=False)

#print(dt_sort.head())
#print(r2_score(y_test, dt_pre))

rfg = RandomForestRegressor()
rfg_fit = rfg.fit(X_train, y_train)
pre_rfg = rfg_fit.predict(X_test)
rfg_df = pd.DataFrame({'Service Type': service_test,
                        'Actual': y_test,
                        'Predict': pre_rfg})

rfg_sort = rfg_df.sort_values('Actual', ascending=False)

#print(rfg_sort.head())
#print(r2_score(y_test, pre_rfg))

mlp = MLPRegressor(hidden_layer_sizes=(50, 25), max_iter=2000, random_state=42)
mlp_fit = mlp.fit(X_train,y_train)
pre_mlp = mlp.predict(X_test)

mlp_data = pd.DataFrame({'Service Type': service_test,
                        'Actual': y_test,
                        'Predict': pre_mlp})

mlp_sort = mlp_data.sort_values('Actual', ascending=False)

#print(mlp_sort.head())
#print(r2_score(y_test, pre_mlp))

perm = permutation_importance(mlp_fit, X_test,y_test, n_repeats=10, random_state=42)

perm_df = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': perm.importances_mean
}).sort_values('Importance', ascending=False)

print(perm_df)