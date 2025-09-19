# === Step 1: Basic Shape ===
# print(df.shape)                    # how many rows × columns
# print(df.columns)                  # names of all columns
# print(df.index)                    # row index info

# === Step 2: Data Types & Info ===
# print(df.dtypes)                   # column data types
# print(df.info())                   # summary of dtypes + non-null counts
# print(df.memory_usage(deep=True))  # memory usage (deep for text too)

# === Step 3: Quick Peek at Data ===
# print(df.head())                   # first 5 rows
# print(df.tail())                   # last 5 rows
# print(df.sample(5))                # random 5 rows

# === Step 4: Missing Values ===
# print(df.isna().sum())             # number of missing values per column
# print(df.isnull().sum())           # same as isna()
# print(df.notna().sum())            # non-missing values per column
# print(df.isna().mean())            # % of missing values per column

# === Step 5: Uniques & Categories ===
# print(df.nunique())                          # unique counts per column
# print(df['col'].value_counts())              # frequency counts for one column
# print(df['col'].value_counts(dropna=False))  # include NaN in counts

# === Step 6: Summary Stats ===
# print(df.describe())                # summary stats (numeric only)
# print(df.describe(include='object'))# summary stats (categorical/text)
# print(df.describe(include='all'))   # all columns

# === Step 7: Correlations (numeric only) ===
# print(df.corr(numeric_only=True))   # correlation matrix
# print(df.cov(numeric_only=True))    # covariance matrix

# === Step 8: Sorting & Grouping ===
# print(df.sort_index().head())       # sort by row index
# print(df.sort_values('col').head()) # sort by column
# print(df.groupby('col').size())     # group counts
# print(df.groupby('col').mean())     # group averages

# === Step 9: Data Selection ===
# print(df.select_dtypes(include='number').head())    # numeric columns
# print(df.select_dtypes(include='object').head())    # text columns
# print(df.select_dtypes(include='category').head())  # category columns

# === Step 10: Export / Convert ===
# print(df.to_dict())                 # DataFrame → dictionary
# print(df.to_json())                 # DataFrame → JSON
# print(df.to_csv(index=False))       # DataFrame → CSV string
