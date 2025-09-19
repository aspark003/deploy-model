import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from joblib import dump, load
from flask import Flask, request, jsonify
import requests

# Load data from CSV if database is unavailable
try:
    engine = create_engine("mysql+pymysql://root:Laurapark%40%2303@localhost/sql")
    with engine.connect() as conn:
        df = pd.read_sql("SELECT * FROM wk2_movies", conn)
except Exception as e:
    print(f"Database error: {e}. Loading from CSV instead.")
    df = pd.read_csv("wk2_movies.csv")
finally:
    engine.dispose()

# Data preprocessing
df = df.drop(columns=['id', 'movie_title', 'genre', 'mpaa_rating', 'runtime_minutes', 'critic_score', 'audience_score', 'release_year'])

ss = StandardScaler()
fit_ss = ss.fit_transform(df[['total_gross', 'inflation_adjusted_gross']])
ss_df = pd.DataFrame(fit_ss, columns=['total_gross', 'inflation_adjusted_gross'], index=df.index)
file = df.drop(columns=['total_gross', 'inflation_adjusted_gross']).join(ss_df)

feature = file.drop(columns=['budget'])
target = file['budget']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=42)

# Train model and save it
le = LinearRegression()
le_fit = le.fit(X_train, y_train)

dump(le_fit, 'save.joblib') # saves by using dump, 'save' is made up name - always save the trained model

app = Flask(__name__) #creates a flask web app

linear_reg_model = load('save.joblib') # load the save 'save.joblib'

@app.route('/model_prediction', methods=['POST'])
def predict(): #predict is made up name
    data = request.json['features'] #data is made up name, using request to get the info from the trained model, using json
    train_data = np.array(data).reshape(1,-1) #train_data is made up name, np is used for number, array using np to list of numbers
    predict_model = linear_reg_model.predict(train_data)[0] #predict_model is made up name
    return jsonify({'budget': predict_model})

#print(file[['total_gross', 'inflation_adjusted_gross']])

if __name__ == '__main__':
    app.run(debug=True)


