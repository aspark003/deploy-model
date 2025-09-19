
#########   OBJECT DATA TYPES ################
# Object dtypes → can mean categories or free text

# Nominal → OneHotEncoder / get_dummies
# How to identify:
# - Text/labels with no natural order.
# - Nominal = labels/IDs with no ranking.
# - Examples: Department (Finance, HR, IT), Doc Type (PR, MIPR, IAA).
# - Ask: “Can I rank these?” → if No, it’s Nominal.
# What to use:
# - OneHotEncoder (sklearn) → flexible, works in pipelines
# - pd.get_dummies() (pandas) → quick and easy
# - Target encoding (advanced) → replace each category with mean of target
# - Hashing trick (advanced) → good when there are many categories

# Ordinal → OrdinalEncoder (or manual mapping)
# How to identify:
# - Categories with a clear ranking or progression.
# - Examples: Job Level (Entry < Mid < Senior < Executive), Status (Incomplete < In Process < Approved).
# - Ask: “Do these categories have a natural sequence?” → if Yes, it’s Ordinal.
# What to use:
# - OrdinalEncoder (sklearn) → assigns numbers that keep order
# - Manual mapping → {'Entry':1, 'Mid':2, 'Senior':3, 'Executive':4}
# - Target encoding (alternative) → if numbers need to reflect outcome

# Boolean → simple 0/1 conversion
# How to identify:
# - Exactly two unique values (Yes/No, True/False, Approved/Not Approved).
# - Can be treated as a binary flag.
# - Ask: “Does this column only have two options?” → if Yes, it’s Boolean.
# What to use:
# - astype(int) → True=1, False=0
# - Replace mapping → {'Yes':1, 'No':0} or {'Approved':1, 'Rejected':0}
# - LabelEncoder (sklearn) → also works, but overkill

# 🔹 CountVectorizer
# - What it does: turns text into raw counts of words
# - When to use:
#   ✔ Small/simple datasets
#   ✔ When word frequency itself matters
#   ✔ Quick testing before using TF-IDF
# - When NOT to use:
#   ✘ Large text datasets (common words take over)
#   ✘ When you care about importance, not just counts
# - Options you can add:
#   stop_words='english'   → remove common words like "the, is, and"
#   ngram_range=(1,2)      → use single words and pairs of words
#   max_features=1000      → keep only the top 1000 words
#   min_df=2               → ignore words that appear in fewer than 2 documents
#   max_df=0.8             → ignore words that appear in more than 80% of documents

# 🔹 TfidfVectorizer
# - What it does: turns text into weighted scores (importance of words)
# - When to use:
#   ✔ Bigger datasets with many words
#   ✔ Finance/legal/medical/business text where meaning matters
#   ✔ When you want rare but important words to stand out
# - When NOT to use:
#   ✘ Very tiny datasets (can over-penalize)
#   ✘ If raw counts are enough (simple tasks)
# - Options you can add:
#   stop_words='english'   → remove common words like "the, is, and"
#   ngram_range=(1,2)      → use single words and pairs of words
#   max_features=1000      → keep only the top 1000 words
#   min_df=2               → ignore words that appear in fewer than 2 documents
#   max_df=0.8             → ignore words that appear in more than 80% of documents
#   use_idf=True           → use IDF weighting (default: True)
#   smooth_idf=True        → avoid zero errors (default: True)
#   norm='l2'              → normalize results (default: 'l2')



########### NUMERIC DATA TYPES #############
# Original values
# Salary: [60,000, 80,000, 100,000]   # real salaries (big numbers)
# Bonus:  [2,000, 5,000, 10,000]     # real bonuses (smaller numbers)

# Problem
# Salary → much bigger numbers (looks more important)
# Bonus → smaller numbers (looks less important)
# Computer → gets tricked into thinking Salary matters more

# StandardScaler (center around 0)
# Salary: [-1.0, 0.0, 1.0]   # small salary = -1, medium salary = 0, big salary = +1
# Bonus:  [-0.9, 0.0, 0.9]   # small bonus = -0.9, medium bonus = 0, big bonus = +0.9

# MinMaxScaler (squish into 0–1)
# Salary: [0.0, 0.5, 1.0]    # lowest salary = 0, middle salary = 0.5, highest salary = 1
# Bonus:  [0.0, 0.375, 1.0]  # lowest bonus = 0, middle bonus ≈ 0.38, highest bonus = 1

# Easy way to remember
# Salary with StandardScaler → see-saw around 0
# Bonus with StandardScaler → also see-saw around 0
# Salary with MinMaxScaler → ruler from 0 to 1
# Bonus with MinMaxScaler → also ruler from 0 to 1

############# DATES DATA TYPES #############
# Datetime dtypes → values stored as dates (e.g., 2020-01-01, 2025-09-13)
# Dates look like calendar values, not numbers the computer can use

# Problem:
# Regression cannot use raw dates directly   # the computer doesn’t understand “January 1st, 2020”
# Computer only works with numbers           # so we must turn dates into numbers

# Fix → turn dates into numeric features
# This means break the date into useful number parts

# Year → pull the year out of the date
# Example: 2020-01-01 → 2020
# When to use: if the actual year matters (e.g., budget year, fiscal year)
# When not to use: if year itself has no meaning (e.g., invoice date, where only age matters)

# Month → pull the month number
# Example: 2020-01-01 → 1
# When to use: if seasonality matters (e.g., sales higher in December)
# When not to use: if month doesn’t affect the outcome

# Day → pull the day number
# Example: 2020-01-01 → 1
# When to use: if day of month is important (e.g., salary paid on 1st vs 15th)
# When not to use: if day has no effect

# Day of week → 0=Monday, 6=Sunday
# Example: 2020-01-01 (Wednesday) → 2
# When to use: if weekdays/weekends affect outcome (e.g., expenses higher on weekends)
# When not to use: if data is not tied to weekly patterns

# Weekend flag → is it weekend? Yes=1, No=0
# Example: 2020-01-04 (Saturday) → 1
# When to use: if weekend/weekday difference matters (e.g., travel, retail sales)
# When not to use: if outcome is unrelated to weekends

# Tenure / Age of record → today – date in years or days
# Example: (2025-09-13 – 2020-01-01) → 5 years
# When to use: if “how old” something is matters (e.g., employee tenure, contract age)
# When not to use: if exact age has no effect on outcome

# Easy way to remember:
# Dates → break into pieces (year, month, day, weekday)   # cut the date into smaller number parts
# Or measure "how long ago" something happened (tenure)   # count years/days from then to now