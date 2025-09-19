#Core building blocks
#Anchors & boundaries
#Quantifiers
#Character classes
#Groups & lookarounds

# === Regex + Pandas Cleaning Decision Tree ===

# START → What do you need to match/clean?

# ├── Empty / Missing?
# │   # df[col].replace(r'^\s*$', np.nan, regex=True)
# │   # ➕ Empty/whitespace → NaN / ➖ If no blanks exist
# │
# ├── Numbers?
# │   ├── Integers?
# │   │   # df[col].replace(r'-?\d+', 'INT', regex=True)
# │   │   # ➕ Integers (±) / ➖ Misses decimals
# │   │
# │   ├── Decimals?
# │   │   # df[col].replace(r'-?\d*\.\d+', 'DEC', regex=True)
# │   │   # ➕ Decimals / ➖ Not integers
# │   │
# │   ├── Any number?
# │   │   # df[col].replace(r'\d+(\.\d+)?', 'NUM', regex=True)
# │   │   # ➕ Int or decimal / ➖ If must separate types
# │   │
# │   ├── Percentages?
# │   │   # df[col].replace(r'-?\d+(\.\d+)?%', 'PCT', regex=True)
# │   │   # ➕ % values / ➖ Plain numbers
# │   │
# │   ├── With commas?
# │   │   # df[col].replace(r'\d{1,3}(,\d{3})*', 'COMMA_NUM', regex=True)
# │   │   # ➕ 1,234 / ➖ Plain digits
# │   │
# │   ├── Currency?
# │   │   # df[col].replace(r'[\$€£]\d+(\.\d+)?', 'CUR', regex=True)
# │   │   # ➕ $12.34 / ➖ No symbol
# │   │
# │   └── Lat/Lon?
# │       # df[col].replace(r'-?\d+\.\d+,\s*-?\d+\.\d+', 'LATLON', regex=True)
# │       # ➕ Latitude/Longitude / ➖ Other coord formats
# │
# ├── Dates / IDs?
# │   ├── Date YYYY-MM-DD?
# │   │   # df[col].replace(r'\d{4}-\d{2}-\d{2}', 'DATE', regex=True)
# │   │   # ➕ ISO date / ➖ US style
# │   │
# │   ├── Date MM/DD/YYYY?
# │   │   # df[col].replace(r'\d{2}/\d{2}/\d{4}', 'DATE', regex=True)
# │   │   # ➕ US date / ➖ ISO
# │   │
# │   ├── US SSN?
# │   │   # df[col].replace(r'\d{3}-\d{2}-\d{4}', 'SSN', regex=True)
# │   │   # ➕ SSN / ➖ Other IDs
# │   │
# │   ├── Credit Card?
# │   │   # df[col].replace(r'\d{4}-\d{4}-\d{4}-\d{4}', 'CC', regex=True)
# │   │   # ➕ ####-####-####-#### / ➖ Other separators
# │   │
# │   ├── US ZIP?
# │   │   # df[col].replace(r'\d{5}(-\d{4})?', 'ZIP', regex=True)
# │   │   # ➕ 5/9 digit ZIP / ➖ Non-US
# │   │
# │   └── US Phone?
# │       # df[col].replace(r'\d{3}-\d{3}-\d{4}', 'PHONE', regex=True)
# │       # ➕ US phone / ➖ International
# │
# ├── Anchors / Boundaries?
# │   # ^           # ➕ Start of string / ➖ Not mid-string
# │   # $           # ➕ End of string / ➖ Not mid-string
# │   # \b          # ➕ Word boundary / ➖ Inside words
# │   # \B          # ➕ Non-boundary / ➖ At edges
# │
# ├── Characters?
# │   # .           # ➕ Any char / ➖ Too broad
# │   # \w          # ➕ Word char (a-z,0-9,_) / ➖ Not space/symbol
# │   # \W          # ➕ Non-word / ➖ Alphanumeric
# │   # \s          # ➕ Whitespace / ➖ Visible chars
# │   # \S          # ➕ Non-whitespace / ➖ Spaces
# │   # [abc]       # ➕ a or b or c / ➖ Sequences
# │   # [^abc]      # ➕ Not a/b/c / ➖ Exact needed
# │   # [0-9]       # ➕ Digit / ➖ Use \d instead
# │   # [A-Za-z]    # ➕ Letters / ➖ Locale missed
# │
# ├── Quantifiers?
# │   # *           # ➕ 0+ times / ➖ Need ≥1
# │   # +           # ➕ 1+ times / ➖ If 0 allowed
# │   # ?           # ➕ Optional (0/1) / ➖ Repeats
# │   # {n}         # ➕ Exactly n / ➖ Not flexible
# │   # {n,}        # ➕ At least n / ➖ Too broad
# │   # {n,m}       # ➕ Between n and m / ➖ Open ended
# │
# └── Groups / Lookarounds?
#     # (abc)       # ➕ Capture group / ➖ If not extracting
#     # (?:abc)     # ➕ Non-capture / ➖ If capture needed
#     # (?=abc)     # ➕ Positive lookahead / ➖ Doesn’t consume
#     # (?!abc)     # ➕ Negative lookahead / ➖ If abc must match
#     # (?<=abc)    # ➕ Positive lookbehind / ➖ Long lookbehind issues
#     # (?<!abc)    # ➕ Negative lookbehind / ➖ If abc should appear
