# === Text Cleaning Workflow Tree ===

# ├── Step 1: Make column string
# │   df['text'] = df['text'].astype(str)
# │   ✅ Use: ensures mixed types (None, numbers) become strings
# │   ❌ Don’t skip: regex/string methods fail on non-strings

# ├── Step 2: Basic cleaning
# │   ├── Remove junk characters
# │   │   df['text'] = df['text'].str.replace(r'\W', ' ', regex=True)   # keep only letters/numbers/_
# │   │   df['text'] = df['text'].str.replace(r'[^\x00-\x7F]+', '', regex=True)  # non-ASCII
# │   │   df['text'] = df['text'].str.replace(r'[\U0001F000-\U0001FFFF]', '', regex=True)  # emojis
# │   │   df['text'] = df['text'].str.replace(r'<[^>]*>', '', regex=True)        # HTML tags
# │   │   df['text'] = df['text'].str.replace(r'https?://[^\s]+', '', regex=True)# URLs
# │   │   df['text'] = df['text'].str.replace(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', regex=True) # emails
# │   │
# │   ├── Fix whitespace
# │   │   df['text'] = df['text'].str.replace(r'\s+', ' ', regex=True)   # collapse multiple spaces
# │   │   df['text'] = df['text'].str.strip()                            # trim edges
# │   │   df['text'] = df['text'].str.replace(r'\n+', ' ', regex=True)   # newlines → space
# │   │   df['text'] = df['text'].str.replace(r'\t', ' ', regex=True)    # tabs → space
# │
# ├── Step 3: Case formatting
# │   df['lower']      = df['text'].str.lower()
# │   df['upper_case'] = df['text'].str.upper()
# │   df['title']      = df['text'].str.title()
# │   df['cap_first']  = df['text'].str.capitalize()
# │   ✅ Use: makes text consistent for analysis
# │
# ├── Step 4: Special regex cleanup
# │   df['text'] = df['text'].str.replace(r'\b(\w+)\s+\1\b', r'\1', regex=True)   # duplicate words
# │   df['text'] = df['text'].str.replace(r'(\w)\1{2,}', r'\1', regex=True)      # repeated chars
# │   df['text'] = df['text'].str.replace(r'\b0+(\d+)\b', r'\1', regex=True)     # leading zeros
# │
# ├── Step 5: Text extraction
# │   ├── Numbers
# │   │   df['three_digits'] = df['text'].str.extract(r'(\d{3})')
# │   │   df['percent']      = df['text'].str.extract(r'(\d+\.?\d*%)')
# │   │   df['currency']     = df['text'].str.extract(r'([\$€£]\d+\.?\d*)')
# │   │
# │   ├── IDs & Codes
# │   │   df['ssn']   = df['text'].str.extract(r'(\d{3}-\d{2}-\d{4})')
# │   │   df['cc']    = df['text'].str.extract(r'(\d{4}-\d{4}-\d{4}-\d{4})')
# │   │   df['isbn']  = df['text'].str.extract(r'(\d{3}-?\d{1,5}-?\d{1,7}-?\d{1,7}-?[\dX])')
# │   │   df['vin']   = df['text'].str.extract(r'([A-HJ-NPR-Z0-9]{17})')
# │   │
# │   ├── Contacts
# │   │   df['phone'] = df['text'].str.extract(r'(\d{3}-\d{3}-\d{4})')
# │   │   df['email'] = df['text'].str.extract(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
# │   │   df['url']   = df['text'].str.extract(r'(https?://[^\s]+)')
# │   │
# │   ├── Misc
# │   │   df['ip']       = df['text'].str.extract(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
# │   │   df['hex_color']= df['text'].str.extract(r'(#[\da-fA-F]{6})')
# │   │   df['mac']      = df['text'].str.extract(r'([0-9A-Fa-f]{2}(:[0-9A-Fa-f]{2}){5})')
# │   │   df['hashtags'] = df['text'].str.findall(r'#\w+')
# │   │   df['mentions'] = df['text'].str.findall(r'@\w+')
# │
# ├── Step 6: Validation & checks
# │   df['has_digit']  = df['text'].str.contains(r'\d', na=False)
# │   df['all_upper']  = df['text'].str.isupper()
# │   df['all_lower']  = df['text'].str.islower()
# │   df['is_numeric'] = df['text'].str.isnumeric()
# │   df['is_alpha']   = df['text'].str.isalpha()
# │   ✅ Use: helps profile data before modeling
# │
# ├── Step 7: Word-level cleanup
# │   df['no_vowels']  = df['text'].str.replace(r'[aeiouAEIOU]', '*', regex=True)
# │   df['five_letters']= df['text'].str.findall(r'\b[a-zA-Z]{5}\b')
# │   df['word_count'] = df['text'].str.split().str.len()
# │   df['first_word'] = df['text'].str.split().str[0]
# │   df['last_word']  = df['text'].str.split().str[-1]
# │
# ├── Step 8: NLP preprocessing
# │   stopwords (NLTK) → remove filler words like "the", "and"
# │   stemming (NLTK)  → cut words to base (e.g., "running" → "run")
# │   lemmatization (spaCy) → smarter base form (e.g., "better" → "good")
# │   contractions     → expand "can't" → "cannot"
# │
# └── Step 9: Missing data handling
#     df['text'] = df['text'].replace('', pd.NA)
#     df['text'] = df['text'].fillna('missing')
#     df = df.dropna(subset=['text'])
#     ✅ Always clean empties before modeling
