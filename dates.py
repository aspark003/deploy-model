# --- Basic Date Cleaning ---
# convert object column to datetime, coercing invalid values to NaT
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# replace missing values (NaT) with a default date (e.g., 1970-01-01)
df['date'] = df['date'].fillna(pd.Timestamp('1970-01-01'))

# drop rows with missing dates
df = df.dropna(subset=['date'])

# remove leading/trailing whitespace from date strings (object column)
df['date'] = df['date'].astype(str).str.strip()

# --- Date Extraction from Object/String Columns ---
# extract dates in YYYY-MM-DD format
df['yyyy_mm_dd'] = df['text'].astype(str).str.extract(r'(\d{4}-\d{2}-\d{2})')

# extract dates in MM/DD/YYYY format
df['mm_dd_yyyy'] = df['text'].astype(str).str.extract(r'(\d{2}/\d{2}/\d{4})')

# extract dates in DD-MMM-YYYY format (e.g., 15-Jan-2023)
df['dd_mmm_yyyy'] = df['text'].astype(str).str.extract(r'(\d{2}-[A-Za-z]{3}-\d{4})')

# extract dates in Month DD, YYYY format (e.g., January 15, 2023)
df['month_dd_yyyy'] = df['text'].astype(str).str.extract(r'([A-Za-z]+ \d{1,2}, \d{4})')

# extract ISO 8601 datetime (e.g., 2023-01-15T12:34:56)
df['iso_datetime'] = df['text'].astype(str).str.extract(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})')

# extract timestamps in logs (e.g., [2023-01-15 12:34:56])
df['log_timestamp'] = df['text'].astype(str).str.extract(r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]')

# extract time only (HH:MM or HH:MM:SS)
df['time'] = df['text'].astype(str).str.extract(r'(\d{2}:\d{2}(?::\d{2})?)')

# convert extracted date strings to datetime
df['yyyy_mm_dd_dt'] = pd.to_datetime(df['yyyy_mm_dd'], errors='coerce')
df['mm_dd_yyyy_dt'] = pd.to_datetime(df['mm_dd_yyyy'], format='%m/%d/%Y', errors='coerce')
df['dd_mmm_yyyy_dt'] = pd.to_datetime(df['dd_mmm_yyyy'], format='%d-%b-%Y', errors='coerce')
df['month_dd_yyyy_dt'] = pd.to_datetime(df['month_dd_yyyy'], format='%B %d, %Y', errors='coerce')
df['iso_datetime_dt'] = pd.to_datetime(df['iso_datetime'], errors='coerce')
df['log_timestamp_dt'] = pd.to_datetime(df['log_timestamp'], errors='coerce')

# --- Standardizing Date Formats ---
# standardize to YYYY-MM-DD string format
df['standardized'] = df['date'].dt.strftime('%Y-%m-%d')

# standardize to ISO 8601 format (YYYY-MM-DDTHH:MM:SS)
df['iso_format'] = df['date'].dt.strftime('%Y-%m-%dT%H:%M:%S')

# standardize to MM/DD/YYYY string format
df['us_format'] = df['date'].dt.strftime('%m/%d/%Y')

# standardize to DD-MMM-YYYY string format
df['short_format'] = df['date'].dt.strftime('%d-%b-%Y')

# --- Extracting Date Components ---
# extract year
df['year'] = df['date'].dt.year

# extract month (numeric)
df['month'] = df['date'].dt.month

# extract month name (full)
df['month_name'] = df['date'].dt.strftime('%B')

# extract month name (abbreviated)
df['month_short'] = df['date'].dt.strftime('%b')

# extract day
df['day'] = df['date'].dt.day

# extract day of week (numeric: 0=Sunday, 6=Saturday)
df['day_of_week'] = df['date'].dt.dayofweek

# extract day of week (name)
df['day_name'] = df['date'].dt.strftime('%A')

# extract hour (for datetime)
df['hour'] = df['date'].dt.hour

# extract minute
df['minute'] = df['date'].dt.minute

# extract second
df['second'] = df['date'].dt.second

# --- Handling Invalid or Inconsistent Dates ---
# replace invalid dates with NaT (already handled by pd.to_datetime(errors='coerce'))

# check for valid dates
df['is_valid_date'] = df['date'].notna()

# replace dates outside a range (e.g., before 1900 or after today)
today = pd.Timestamp.now()
df['date'] = df['date'].where(df['date'].between(pd.Timestamp('1900-01-01'), today), pd.NaT)

# --- Date Arithmetic ---
# add days to dates
df['plus_7_days'] = df['date'] + pd.Timedelta(days=7)

# subtract days from dates
df['minus_7_days'] = df['date'] - pd.Timedelta(days=7)

# calculate difference between dates (in days)
df['days_diff'] = (df['date'] - pd.Timestamp('2023-01-01')).dt.days

# extract days since epoch (1970-01-01)
df['days_since_epoch'] = (df['date'] - pd.Timestamp('1970-01-01')).dt.days

# --- Handling Missing Data in Date Columns ---
# replace empty strings with NaT (for object columns)
df['date'] = df['date'].replace('', pd.NaT)

# fill missing dates with a default
df['date'] = df['date'].fillna(pd.Timestamp('1970-01-01'))

# forward fill missing dates
df['date'] = df['date'].ffill()

# backward fill missing dates
df['date'] = df['date'].bfill()

# --- Domain-Specific Date Patterns ---
# extract dates in European format (DD/MM/YYYY)
df['dd_mm_yyyy'] = df['text'].astype(str).str.extract(r'(\d{2}/\d{2}/\d{4})')
df['dd_mm_yyyy_dt'] = pd.to_datetime(df['dd_mm_yyyy'], format='%d/%m/%Y', errors='coerce')

# extract dates in MMM DD YYYY format (e.g., Jan 15 2023)
df['mmm_dd_yyyy'] = df['text'].astype(str).str.extract(r'([A-Za-z]{3} \d{1,2} \d{4})')
df['mmm_dd_yyyy_dt'] = pd.to_datetime(df['mmm_dd_yyyy'], format='%b %d %Y', errors='coerce')

# extract fiscal quarters (e.g., Q1 2023)
df['quarter'] = df['text'].astype(str).str.extract(r'(Q[1-4] \d{4})')

# extract Unix timestamps (e.g., 1697059200)
df['unix_timestamp'] = df['text'].astype(str).str.extract(r'(\d{10,})')
df['unix_datetime'] = pd.to_datetime(df['unix_timestamp'], unit='s', errors='coerce')

# --- Performance Optimization for Large Datasets ---
# process large date datasets in chunks
def process_chunk(chunk):
    chunk['cleaned_date'] = pd.to_datetime(chunk['date'], errors='coerce').dt.strftime('%Y-%m-%d')
    return chunk
chunksize = 10000
df = pd.concat([process_chunk(chunk) for chunk in pd.read_csv('large_file.csv', chunksize=chunksize)])

n regex symbols for dates

\d digit, \D not digit
\s whitespace; \S not whitespace
* zero or more, + one or more, ? zero or one
{n} exactly n times, {n,} n or more, {n,m} between n and m
^ start of string, $ end of string
\b word boundary, \B not boundary
( … ) capture group, (?: … ) non-capture group
[A-Za-z] letters, [A-Z] uppercase, [a-z] lowercase
escape special chars with \: \. \+ \* \? \| \( \) \[ \] \{ \} \\

Common date patterns

\d{4}-\d{2}-\d{2} YYYY-MM-DD
\d{2}/\d{2}/\d{4} MM/DD/YYYY or DD/MM/YYYY
\d{2}-[A-Za-z]{3}-\d{4} DD-MMM-YYYY
[A-Za-z]+ \d{1,2}, \d{4} Month DD, YYYY
[A-Za-z]{3} \d{1,2} \d{4} MMM DD YYYY
\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2} ISO 8601 datetime
\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] log timestamp
\d{2}:\d{2}(?::\d{2})? HH:MM or HH:MM:SS
Q[1-4] \d{4} fiscal quarter (e.g., Q1 2023)
\d{10,} Unix timestamp (seconds)

Common datetime format codes (for dt.strftime)

%Y 4-digit year (e.g., 2023)
%y 2-digit year (e.g., 23)
%m 2-digit month (e.g., 01)
%d 2-digit day (e.g., 15)
%B full month name (e.g., January)
%b abbreviated month name (e.g., Jan)
%A full weekday name (e.g., Monday)
%a abbreviated weekday name (e.g., Mon)
%H 24-hour (00-23)
%I 12-hour (01-12)
%M minute (00-59)
%S second (00-59)
%p AM/PM
%z UTC offset (e.g., +0000)
%Z timezone name

Quick takeaway

Use pd.to_datetime(errors='coerce') to convert object columns to datetime, handling invalid formats.
Use str.extract with regex to extract dates from strings in various formats.
Use dt.strftime to standardize date formats (e.g., %Y-%m-%d).
Extract date components (year, month, day) with dt.year, dt.month, etc.
Handle missing data with fillna, ffill, or dropna for robust date columns.
Validate dates with notna() or range checks to ensure data quality.
Test regex patterns with re.compile(pattern).findall(sample_text) to verify matches.
For large datasets, use chunking (pd.read_csv(chunksize)) to manage memory.
Specify exact format in pd.to_datetime(format=...) for faster parsing.
For ambiguous formats (e.g., MM/DD vs DD/MM), use dayfirst=True or format=.