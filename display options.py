# === Pandas Display Options Decision Tree ===

# ── Formatting numbers ──
# pd.set_option("display.chop_threshold", 1e-10)        # Show tiny floats as 0.0
# pd.set_option("display.precision", 3)                 # Set decimal places
# pd.set_option("display.float_format", "{:.2f}".format) # Custom float format
# pd.set_option("display.colheader_justify", "right")   # Align headers
# pd.set_option("display.encoding", "utf-8")            # Fix text encoding

# ── DataFrame too wide/long ──
#   ├─ Rows too many?
#   │   pd.set_option("display.max_rows", 50)           # Limit rows shown
#   │   pd.set_option("display.min_rows", 10)           # Always show at least X rows
#   │   pd.set_option("display.show_dimensions", True)  # Show DataFrame shape
#   │   pd.set_option("display.max_info_rows", 200)     # Limit rows scanned in .info()
#   │
#   ├─ Columns too many?
#   │   pd.set_option("display.max_columns", 20)        # Limit columns shown
#   │   pd.set_option("display.max_info_columns", 100)  # Limit columns in .info()
#   │
#   ├─ Wrapping issues?
#   │   pd.set_option("display.expand_frame_repr", False) # Stop wrapping wide DataFrames
#   │   pd.set_option("display.width", 120)             # Set console width
#   │
#   └─ Values too long?
#       pd.set_option("display.max_colwidth", 100)      # Limit string length
#       pd.set_option("display.max_seq_items", 10)      # Limit items in lists
#       pd.set_option("display.large_repr", "truncate") # Truncate large DataFrames

# ── Dates & times ──
# pd.set_option("display.date_dayfirst", True)          # Show DD/MM/YYYY
# pd.set_option("display.date_yearfirst", True)         # Show YYYY/MM/DD
# pd.set_option("display.timestamp_format", "%Y-%m-%d") # Custom timestamp
# pd.set_option("display.datetime_is_numeric", True)    # Treat datetime as numeric

# ── Notebook / HTML / LaTeX ──
# pd.set_option("display.html.table_schema.enabled", True) # JSON table schema in Jupyter
# pd.set_option("display.html.table_schema.default", True) # Default schema
# pd.set_option("display.html.border", 1)               # Border width in HTML tables
# pd.set_option("display.html.use_mathjax", True)       # Render LaTeX math
# pd.set_option("display.latex.repr", True)             # Enable LaTeX output
# pd.set_option("display.latex.escape", True)           # Escape LaTeX chars
# pd.set_option("display.latex.longtable", True)        # Multi-page tables
# pd.set_option("display.latex.multicolumn", True)      # Merge headers
# pd.set_option("display.latex.multirow", True)         # Merge rows
# pd.set_option("display.notebook_repr_html", True)     # Rich HTML repr
# pd.set_option("display.notebook_repr_json", True)     # JSON repr
# pd.set_option("display.notebook_repr_text", True)     # Plain-text repr

# ── Information & diagnostics ──
# pd.set_option("display.detect_types", True)           # Auto-detect dtypes
# pd.set_option("display.memory_usage", True)           # Show memory usage
# pd.set_option("display.pprint_nest_depth", 3)         # Depth of nested printing

# ── Styler (HTML/CSS styling) ──
# pd.set_option("display.styler.render.max_elements", 5000) # Max elements before truncation
# pd.set_option("display.styler.render.max_columns", 50)    # Max columns shown
# pd.set_option("display.styler.render.max_rows", 100)      # Max rows shown
