# --- Period Cleaning ---
# convert datetime to period (e.g., monthly frequency)
df['period'] = df['date'].dt.to_period(freq='M')

# convert string to period (e.g., "2023-01" → period[M])
df['period'] = pd.to_period(df['text'].astype(str), freq='M', errors='coerce')

# replace missing periods (NaT) with a default period
df['period'] = df['period'].fillna(pd.Period('1970-01', freq='M'))

# drop rows with missing periods
df = df.dropna(subset=['period'])

# extract periods from strings (e.g., "2023-01")
df['period_str'] = df['text'].astype(str).str.extract(r'(\d{4}-\d{2})')

# convert extracted strings to period
df['period_extracted'] = pd.to_period(df['period_str'], freq='M', errors='coerce')

# change period frequency (e.g., monthly to yearly)
df['period_yearly'] = df['period'].dt.to_period(freq='Y')

# extract period components (e.g., year, month)
df['period_year'] = df['period'].dt.year
df['period_month'] = df['period'].dt.month

# check if period is within range
df['in_range'] = df['period'].between(pd.Period('1900-01', freq='M'), pd.Period.now(freq='M'))

# --- Performance Optimization for Large Datasets ---
# process large period datasets in chunks
def process_chunk(chunk):
    chunk['cleaned_period'] = pd.to_period(chunk['text'].astype(str), freq='M', errors='coerce')
    return chunk
chunksize = 10000
df = pd.concat([process_chunk(chunk) for chunk in pd.read_csv('large_file.csv', chunksize=chunksize)])

# --- Regex Symbols for Period Extraction ---
\d digit, \D not digit
\s whitespace; \S not whitespace
- separator
^ start of string, $ end of string
( … ) capture group

# --- Common Period Patterns ---
r'(\d{4}-\d{2})' matches YYYY-MM
r'(\d{4})' matches YYYY for yearly periods
r'(\d{4}-Q[1-4])' matches YYYY-QN for quarterly periods

# --- Quick Takeaway for Periods ---
# Use pd.to_period(freq=...) to convert strings or datetimes to periods.
# Use regex to extract period-like strings (e.g., YYYY-MM).
# Extract components with dt.year, dt.month, etc.
# Handle missing values with fillna or dropna.
# Specify frequency (e.g., 'M', 'Y', 'Q') for consistency.
# Test patterns with re.compile(pattern).findall(sample_text).