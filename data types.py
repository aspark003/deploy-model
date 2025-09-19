# === Pandas dtypes Decision Tree ===

# START → What kind of data do you have?

# ├── Missing values in column?
# │   # df['col'].astype('Int64' / 'Float64' / 'boolean')
# │   # ➕ Nullable dtypes for NaN / ➖ Use normal int/float/bool if no missing
# │
# ├── Categorical (few unique repeating values)?
# │   # df['col'].astype('category')
# │   # ➕ Few fixed groups (gender, status) / ➖ Too many unique values
# │
# ├── Mostly identical or zeros?
# │   # df['col'].astype('Sparse[...]')
# │   # ➕ Many duplicates or NA → saves memory / ➖ Not dense varied data
# │
# ├── Need to confirm type?
# │   # df.dtypes
# │   # ➕ Always check after casting / ➖ Don’t skip (silent errors possible)
# │
# ├── Numbers?
# │   ├── Integers (whole numbers)?
# │   │   # df['col'].astype('int8')
# │   │   # ➕ Small range, no NaN / ➖ Out of range or missing
# │   │   # df['col'].astype('Int64')
# │   │   # ➕ Large ints with NaN / ➖ Not for decimals
# │   │   # df['col'].astype('uint8')
# │   │   # ➕ Positive only, no NaN / ➖ If negatives or missing exist
# │   │
# │   ├── Floats (decimals)?
# │   │   # df['col'].astype('float16')
# │   │   # ➕ Save memory / ➖ Loses precision
# │   │   # df['col'].astype('float64')
# │   │   # ➕ Default for regression / ➖ Large memory
# │   │   # df['col'].astype('Float64')
# │   │   # ➕ Floats with NaN / ➖ Slower if no NaN
# │   │
# │   └── Complex numbers?
# │       # df['col'].astype('complex128')
# │       # ➕ Engineering/science with imaginary / ➖ Not for regression
# │
# ├── True/False values?
# │   # df['col'].astype('bool')
# │   # ➕ Flags, no NaN / ➖ Breaks with missing
# │   # df['col'].astype('boolean')
# │   # ➕ Nullable bool / ➖ Slower if no NaN
# │
# ├── Text?
# │   # df['col'].astype('string')
# │   # ➕ Clean strings, supports NaN / ➖ Mixed types fallback to object
# │   # df['col'].astype('object')
# │   # ➕ Mixed data / ➖ Slower, more memory
# │   # df['col'].astype('S10')
# │   # ➕ Fixed ASCII length / ➖ Cuts text, no unicode
# │   # df['col'].astype('U20')
# │   # ➕ Fixed Unicode length / ➖ Cuts text
# │
# ├── Dates / Time?
# │   # df['col'].astype('datetime64[ns]')
# │   # ➕ Timestamps / ➖ If text not parseable
# │   # df['col'].astype('timedelta64[ns]')
# │   # ➕ Durations / ➖ Not for categories
# │   # df['col'].astype('period[M]')
# │   # ➕ Monthly reporting / ➖ Need exact timestamps
# │
# ├── Category or Sparse?
# │   # df['col'].astype('category')
# │   # ➕ Low unique → saves memory / ➖ Continuous numbers
# │   # df['col'].astype('Sparse[int]')
# │   # ➕ Many 0 or NA / ➖ Dense data
# │
# └── Aliases?
#     # df['col'].astype(np.int32)
#     # df['col'].astype(np.float64)
#     # df['col'].astype(int)
#     # df['col'].astype(float)
#     # ➕ Use: with NumPy or plain Python / ➖ Not pandas nullable dtypes
