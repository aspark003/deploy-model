import pandas as pd
import json
import requests

url = "https://api.usaspending.gov/api/v2/references/toptier_agencies/"

get_url = requests.get(url)
respond = get_url.json()

gov = respond['results']
df = pd.DataFrame(gov)
df.to_csv("c:/Users/anton/OneDrive/school/top_tier.csv", index=False)

#print(df.to_string())
