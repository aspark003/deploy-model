# --- Interval Cleaning ---
# create intervals from two numeric columns
df['interval'] = pd.IntervalIndex.from_arrays(df['start'], df['end'], closed='left')

# convert string intervals (e.g., "[1, 2)") to Interval
def parse_interval(s):
    match = re.match(r'\[(\d+),\s*(\d+)\)', s)
    if match:
        left, right = map(int, match.groups())
        return pd.Interval(left, right, closed='left')
    return pd.NA
df['interval'] = df['text'].astype(str).apply(parse_interval)

# replace missing intervals with a default
df['interval'] = df['interval'].fillna(pd.Interval(0, 1, closed='left'))

# drop rows with missing intervals
df = df.dropna(subset=['interval'])

# extract interval bounds
df['interval_left'] = df['interval'].apply(lambda x: x.left if pd.notna(x) else pd.NA)
df['interval_right'] = df['interval'].apply(lambda x: x.right if pd.notna(x) else pd.NA)

# check if intervals are valid (left <= right)
df['is_valid_interval'] = df['interval'].apply(lambda x: x.left <= x.right if pd.notna(x) else False)

# --- Performance Optimization for Large Datasets ---
# process large interval datasets in chunks
def process_chunk(chunk):
    chunk['cleaned_interval'] = pd.IntervalIndex.from_arrays(chunk['start'], chunk['end'], closed='left')
    return chunk
chunksize = 10000
df = pd.concat([process_chunk(chunk) for chunk in pd.read_csv('large_file.csv', chunksize=chunksize)])

# --- Regex Symbols for Interval Extraction ---
\d digit, \D not digit
\s whitespace
\[ \] literal brackets
, comma separator
( … ) capture group

# --- Common Interval Patterns ---
r'\[(\d+),\s*(\d+)\)' matches [left, right) intervals
r'\((\d+),\s*(\d+)\]' matches (left, right] intervals

# --- Quick Takeaway for Intervals ---
# Use pd.IntervalIndex to create intervals from numeric bounds.
# Use regex to extract interval strings, then parse to Interval.
# Extract bounds with .left and .right.
# Handle missing values with fillna or dropna.
# Validate with custom checks for left <= right.
# Test patterns with re.compile(pattern).findall(sample_text).