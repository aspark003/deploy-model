import pandas as pd

pd.set_option("display.max_colwidth", None)
f = pd.read_csv("toptier_agencies.csv", encoding='utf-8-sig', engine='python')
f = f.drop(columns=['active_fy', 'active_fq', 'current_total_budget_authority_amount'])


print(f.describe(include='all').to_string())