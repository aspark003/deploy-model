# --- Complex Type Cleaning ---
# parse JSON-like strings to dictionaries
import json
def parse_json(s):
    try:
        return json.loads(s)
    except:
        return {}
df['dict'] = df['text'].astype(str).apply(parse_json)

# extract specific key from dictionaries
df['dict_key'] = df['dict'].apply(lambda x: x.get('key', pd.NA) if isinstance(x, dict) else pd.NA)

# parse list-like strings (e.g., "[1, 2, 3]")
import ast
def parse_list(s):
    try:
        return ast.literal_eval(s) if isinstance(s, str) else s
    except:
        return []
df['list'] = df['text'].apply(parse_list)

# extract first element from lists
df['list_first'] = df['list'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else pd.NA)

# convert list to string representation
df['list_str'] = df['list'].apply(lambda x: str(x) if isinstance(x, list) else '')

# extract JSON-like strings (e.g., {"key": "value"})
df['json_str'] = df['text'].astype(str).str.extract(r'(\{.*?\})')

# validate JSON strings
def is_valid_json(s):
    try:
        json.loads(s)
        return True
    except:
        return False
df['is_valid_json'] = df['text'].astype(str).apply(is_valid_json)

# flatten nested lists (requires custom function)
def flatten_list(lst):
    return [item for sublist in lst for item in (sublist if isinstance(sublist, list) else [sublist])]
df['flattened'] = df['list'].apply(flatten_list)

# remove empty lists or dictionaries
df['list'] = df['list'].apply(lambda x: x if isinstance(x, list) and len(x) > 0 else pd.NA)
df['dict'] = df['dict'].apply(lambda x: x if isinstance(x, dict) and len(x) > 0 else pd.NA)

# --- Performance Optimization for Large Datasets ---
# process large complex datasets in chunks
def process_chunk(chunk):
    chunk['cleaned_dict'] = chunk['text'].astype(str).apply(lambda x: json.loads(x) if is_valid_json(x) else {})
    return chunk
chunksize = 10000
df = pd.concat([process_chunk(chunk) for chunk in pd.read_csv('large_file.csv', chunksize=chunksize)])

# --- Regex Symbols for Complex Type Extraction ---
\{ \} literal curly braces
\[ \] literal square brackets
" quotation marks
\s whitespace
, comma separator
: key-value separator
( … ) capture group
.* any characters (non-greedy with .*?)

# --- Common Complex Type Patterns ---
r'(\{.*?\})' matches JSON-like dictionaries
r'(\[.*?\])' matches list-like strings
r'"(\w+)":\s*"([^"]*)"' matches key-value pairs in JSON

# --- Quick Takeaway for Complex Types ---
# Use json.loads or ast.literal_eval to parse JSON or list strings.
# Extract elements with dictionary .get() or list indexing.
# Validate with try-except to handle malformed data.
# Handle missing or empty structures with fillna or conditional checks.
# Flatten nested structures with custom functions.
# Test patterns with re.compile(pattern).findall(sample_text).