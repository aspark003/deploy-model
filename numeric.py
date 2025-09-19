# --- Basic Numeric Cleaning ---
# convert object column to numeric, coercing invalid values to NaN
# df['number'] = pd.to_numeric(df['number'], errors='coerce')

# replace missing values (NaN) with a default (e.g., 0)
# df['number'] = df['number'].fillna(0)

# drop rows with missing values in numeric column
# df = df.dropna(subset=['number'])

# remove leading/trailing whitespace from numeric strings (object column)
# df['number'] = df['number'].astype(str).str.strip()

# convert object column with numeric strings to float (handle commas, e.g., "1,234.56")
# df['number'] = df['number'].astype(str).str.replace(r'[^\d.-]', '', regex=True).astype(float, errors='coerce')

# remove leading zeros from numeric strings (e.g., "00123" → "123")
# df['number'] = df['number'].astype(str).str.replace(r'\b0+(\d+)\b', r'\1', regex=True)

# --- Number Extraction from Object/String Columns ---
# extract signed decimal numbers (e.g., -123.45)
# df['decimal'] = df['text'].astype(str).str.extract(r'(-?\d+\.\d+)', na=False)

# extract integers (e.g., 123)
# df['integer'] = df['text'].astype(str).str.extract(r'(-?\d+)', na=False)

# extract numbers with commas (e.g., 1,234,567)
# df['with_commas'] = df['text'].astype(str).str.extract(r'(\d{1,3}(,\d{3})*)')

# extract percentages (e.g., 12.34%)
# df['percent'] = df['text'].astype(str).str.extract(r'(\d+\.?\d*%)')

# extract currency (e.g., $12.34 or €123)
# df['currency'] = df['text'].astype(str).str.extract(r'[\$€£](\d+\.?\d*)')

# extract exactly three digits
# df['three_digits'] = df['text'].astype(str).str.extract(r'(\d{3})')

# extract numbers using lookaheads (digits not followed by letters)
# df['digits_no_letters'] = df['text'].astype(str).str.extract(r'\d+(?![a-zA-Z])')

# convert extracted numbers to numeric type
# df['decimal_numeric'] = pd.to_numeric(df['decimal'], errors='coerce')
# df['integer_numeric'] = pd.to_numeric(df['integer'], errors='coerce')

# --- Rounding and Precision ---
# round to 2 decimal places (numeric column)
# df['rounded'] = df['number'].round(2)

# floor division to nearest integer
# df['floor'] = df['number'].astype(int)

# ceiling to next integer
# import math
# df['ceiling'] = df['number'].apply(math.ceil)

# truncate decimals (no rounding)
# df['truncated'] = df['number'].apply(math.trunc)

# --- Handling Outliers ---
# cap values above a threshold (e.g., 1000)
# df['capped'] = df['number'].clip(upper=1000)

# cap values below a threshold (e.g., 0)
# df['capped_lower'] = df['number'].clip(lower=0)

# remove outliers using IQR method
# Q1 = df['number'].quantile(0.25)
# Q3 = df['number'].quantile(0.75)
# IQR = Q3 - Q1
# df['no_outliers'] = df['number'].where(df['number'].between(Q1 - 1.5 * IQR, Q3 + 1.5 * IQR))

# --- Number Formatting as Strings ---
# format as 2-decimal string
# df['formatted_2dec'] = df['number'].apply(lambda x: f"{x:.2f}")

# format with comma separator (e.g., 1,234.56)
# df['formatted_commas'] = df['number'].apply(lambda x: f"{x:,.2f}")

# format with zero-padding (width 8, e.g., 001234.56)
# df['formatted_padded'] = df['number'].apply(lambda x: f"{x:08.2f}")

# format with always-shown sign (e.g., +1234.56)
# df['formatted_signed'] = df['number'].apply(lambda x: f"{x:+.2f}")

# format as percentage (e.g., 0.256 → 25.6%)
# df['formatted_percent'] = df['number'].apply(lambda x: f"{x:.1%}")

# format in scientific notation (e.g., 12345 → 1.23e+04)
# df['formatted_scientific'] = df['number'].apply(lambda x: f"{x:.2e}")

# --- Validation and Checks ---
# check if numeric column is finite (not inf or NaN)
# df['is_finite'] = df['number'].apply(lambda x: np.isfinite(x))

# check if string contains only digits (for object column)
# df['is_digits'] = df['text'].astype(str).str.isdigit()

# check if string is numeric (includes decimals, e.g., "123.45")
# df['is_numeric'] = df['text'].astype(str).str.match(r'^-?\d*\.?\d+$')

# check if number is within range (e.g., 0 to 100)
# df['in_range'] = df['number'].between(0, 100)

# --- Handling Mixed Types in Object Columns ---
# convert mixed types to numeric, replacing non-numeric with NaN
# df['cleaned_number'] = pd.to_numeric(df['text'].astype(str), errors='coerce')

# extract first number from mixed string
# df['first_number'] = df['text'].astype(str).str.extract(r'(-?\d+\.?\d*)')

# replace non-numeric strings with a default value (e.g., 0)
# df['text'] = df['text'].where(df['text'].astype(str).str.match(r'^-?\d*\.?\d+$'), 0)

# --- Domain-Specific Numeric Patterns ---
# extract Social Security Numbers (###-##-####)
# df['ssn'] = df['text'].astype(str).str.extract(r'(\d{3}-\d{2}-\d{4})')

# extract credit card numbers (####-####-####-####)
# df['cc'] = df['text'].astype(str).str.extract(r'(\d{4}-\d{4}-\d{4}-\d{4})')

# extract ZIP codes (5 digits or 5+4)
# df['zip'] = df['text'].astype(str).str.extract(r'(\d{5}(-\d{4})?)')

# extract phone numbers (US format: ###-###-####)
# df['phone'] = df['text'].astype(str).str.extract(r'(\d{3}-\d{3}-\d{4})')

# extract latitude/longitude (e.g., 40.7128, -74.0060)
# df['lat_lon'] = df['text'].astype(str).str.extract(r'(-?\d+\.\d+,\s*-?\d+\.\d+)')

# --- Performance Optimization for Large Datasets ---
# process large numeric datasets in chunks
# def process_chunk(chunk):
#     chunk['cleaned'] = pd.to_numeric(chunk['number'], errors='coerce').round(2)
#     return chunk
# chunksize = 10000
# df = pd.concat([process_chunk(chunk) for chunk in pd.read_csv('large_file.csv', chunksize=chunksize)])
