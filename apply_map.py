# axis=0   # column-wise (default)
# axis=1   # row-wise

# === DataFrame-wide methods ===
# df.apply(func)                        # Apply to each column (default) or row (axis=1)
# df.apply(func, axis=1)                 # Apply to each row
# df.map(func)                           # Elementwise on all cells (pandas 2.1+)
# df.applymap(func)                       # ⚠️ Deprecated; use df.map()
# df.aggregate(func)                     # Aggregate columns with one/many funcs
# df.apply(lambda col: col.max()-col.min())         # Lambda: range per column
# df.apply(lambda row: row['a']+row['b'], axis=1)   # Lambda: sum columns row-wise
# df.map(lambda x: x*2)                               # Lambda: double each value

# === Series (single column) methods ===
# s.apply(func)                          # Apply function to each value
# s.map(func)                             # Fast map via function/dict/Series
# s.transform(func)                        # Apply function; keep same shape
# s.replace(to_replace, value)             # Replace values or regex
# s.where(cond, other)                     # Keep if cond True else other
# s.mask(cond, other)                      # Replace if cond True
# s.apply(lambda x: x**2)                  # Lambda: square values
# s.apply(lambda x: np.log1p(x) if x>0 else 0)  # Lambda: conditional log
# s.map(lambda x: str(x).upper())          # Lambda: uppercase text
# s.map(lambda x: x.strip() if isinstance(x,str) else x)  # Lambda: strip spaces
# s.transform(lambda x: (x - x.mean())/x.std())          # Lambda: z-score

# === Grouped data methods ===
# df.groupby(keys).apply(func)             # Apply per group; return DataFrame/Series
# df.groupby(keys).transform(func)         # Apply per group; keep same shape
# df.groupby(keys).agg(func)               # Aggregate per group
# df.groupby('g').apply(lambda g: g['v'].mean())     # Lambda: mean per group
# df.groupby('g').transform(lambda x: x - x.mean())  # Lambda: mean-center
# df.groupby(['a','b']).agg(lambda x: x.max()-x.min()) # Lambda: group range

# === Rolling / Expanding window methods ===
# s.rolling(w).apply(func)                 # Apply over moving window
# s.expanding().apply(func)                # Apply cumulatively
# s.rolling(3).apply(lambda x: x.mean())   # Lambda: 3-period mean
# s.expanding().apply(lambda x: x.std())   # Lambda: expanding std

# === Vectorized accessor methods ===
# s.str.*                                   # String ops (replace, extract, etc.)
# s.str.replace(r'\d+', lambda m: f"[{m.group()}]")  # Lambda: regex replace
# s.dt.*                                    # Date/time ops (year, month, etc.)
# s.dt.apply(lambda d: d.year)              # Lambda: extract year
# s.cat.*                                   # Categorical ops (codes, rename)
# s.cat.rename_categories(lambda c: c.upper())  # Lambda: uppercase categories

# === Type casting ===
# s.astype(dtype)                           # Convert Series dtype (e.g. float64, category)
