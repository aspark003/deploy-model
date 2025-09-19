import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("c:/Users/anton/OneDrive/school/disney.csv", encoding='utf-8-sig', engine='python')
df.columns = df.columns.str.replace('_', ' ', regex=True).str.lower().str.strip()
df = df.drop(columns=['release date', 'total gross', 'inflation adjusted gross', 'runtime minutes', 'movie title', 'budget'])

df['genre'] = df['genre'].fillna('missing')
df['mpaa rating'] = df['mpaa rating'].fillna('missing')

le = LabelEncoder()
fit_le = le.fit_transform(df['genre'])
le_df = pd.DataFrame(fit_le, columns=['genre'], index=df.index)

fit_mpaa = le.fit_transform(df['mpaa rating'])
mpaa_df = pd.DataFrame(fit_mpaa, columns=['mpaa rating'], index=df.index)


display = le_df.join(mpaa_df)
#print(display.head().to_string())

n_col = df.select_dtypes(include='number').columns.tolist()
ss = StandardScaler()
ss_fit = ss.fit_transform(df[n_col])
ss_df = pd.DataFrame(ss_fit, columns=n_col, index=df.index)
final = display.join(ss_df)
#print(final.head().to_string())

c = final.corr()
#print(c.to_string())

km = KMeans(n_clusters= 10, random_state=42)

km_fit = km.fit(final)

df['Cluster'] = km.labels_

print(df.head(10).to_string())
print(silhouette_score(final, km.labels_))
# Group by cluster and show the average values
cluster_summary = df.groupby('Cluster')[['critic score', 'audience score', 'release year']].mean()

print(cluster_summary)

#print(le_df.head().to_string())
#print(df.head().to_string())