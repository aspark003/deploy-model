# === Categorical Cleaning Workflow (Tree Style) ===

# ├── Step 1: Convert to category
# │   df['cat'] = df['text'].astype('category')
# │   ✅ Saves memory, faster lookups
# │   ❌ Still keeps all unique values unless restricted
# │
# ├── Step 2: Restrict categories
# │   categories = ['low','medium','high']
# │   df['cat'] = df['text'].astype(str).str.lower()
# │                .apply(lambda x: x if x in categories else pd.NA).astype('category')
# │   ✅ Keeps only allowed categories
# │   ❌ Drops anything not in list
# │
# ├── Step 3: Handle missing values
# │   df['cat'] = df['cat'].fillna('unknown')
# │   ✅ Replace NaN with "unknown"
# │   ❌ Adds new label you may not want
# │
# │   OR
# │   df = df.dropna(subset=['cat'])
# │   ✅ Remove missing rows completely
# │   ❌ Lose data
# │
# ├── Step 4: Clean categories
# │   df['cat'] = df['cat'].cat.remove_unused_categories()
# │   ✅ Drops leftover categories not in use
# │
# │   df['cat'] = df['cat'].cat.rename_categories(lambda x: x.lower())
# │   ✅ Standardize category names (e.g., lowercase)
# │
# ├── Step 5: Map or recode
# │   cat_map = {'low':'L','medium':'M','high':'H'}
# │   df['cat_mapped'] = df['cat'].map(cat_map).astype('category')
# │   ✅ Rename or simplify categories
# │
# ├── Step 6: Extract from text (regex)
# │   df['cat_extracted'] = df['text'].str.extract(r'(low|medium|high)', flags=re.IGNORECASE)
# │   df['cat_extracted'] = df['cat_extracted'].astype('category')
# │   ✅ Pull out category words from messy text
# │
# ├── Step 7: Order categories (ordinal)
# │   df['cat_ordered'] = df['cat'].cat.set_categories(['low','medium','high'], ordered=True)
# │   ✅ Keep natural order for ML models
# │   ❌ Wrong if categories are not ordered
# │
# ├── Step 8: Convert to numeric codes
# │   df['cat_codes'] = df['cat'].cat.codes
# │   ✅ Useful for ML models (fast)
# │   ❌ Codes depend on category order
# │
# ├── Step 9: Validate
# │   df['is_valid_cat'] = df['cat'].isin(categories)
# │   ✅ True/False check for allowed categories
# │
# ├── Step 10: Big data optimization
# │   def process_chunk(chunk):
# │       chunk['cleaned_cat'] = chunk['text'].astype(str).str.lower()
# │                              .apply(lambda x: x if x in categories else 'unknown').astype('category')
# │       return chunk
# │   chunksize = 10000
# │   df = pd.concat([process_chunk(chunk) for chunk in pd.read_csv('large_file.csv', chunksize=chunksize)])
# │   ✅ Process in pieces, saves memory
# │
# ├── Regex quick guide
# │   \w+   word characters
# │   [A-Za-z]+ letters only
# │   ^/$   start/end of string
# │   |     OR (low|medium|high)
# │   \b    word boundary
# │
# └── Takeaway
#     • Use astype('category') to save memory
#     • Fill or drop missing depending on goal
#     • Restrict categories explicitly for cleaner data
#     • Map, order, or extract as needed for ML
#     • Use cat.codes when numeric input is required
