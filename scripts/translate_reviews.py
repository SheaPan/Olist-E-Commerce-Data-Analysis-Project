import pandas as pd
import numpy as np
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound, TooManyRequests
import time
import sys
import os

# -----------------------------
# CONFIG
# -----------------------------
FILE_PATH = "reviews_translation.xlsx"
BATCH_SIZE = 100           # number of rows per batch
MIN_TEXT_LENGTH = 3
SLEEP_TIME = 15            # seconds to wait on rate limit
MAX_RETRIES = 5
PORTUGUESE_COLS = ['review_comment_title', 'review_comment_message']

# -----------------------------
# INITIALIZE TRANSLATOR
# -----------------------------
try:
    translator = GoogleTranslator(source='portuguese', target='english')
except Exception as e:
    print(f"❌ ERROR: Translator initialization failed. {e}")
    sys.exit(1)

# -----------------------------
# LOAD CSV
# -----------------------------
try:
    print("📂 Loading Excel file...")
    df = pd.read_excel(FILE_PATH)
except FileNotFoundError:
    print("❌ ERROR: File not found. Check FILE_PATH.")
    sys.exit(1)
except Exception as e:
    print(f"❌ ERROR loading Excel: {e}")
    sys.exit(1)

# Normalize column names
df.columns = df.columns.str.lower()

# Replace 'none' and empty strings with NaN
df.replace('none', np.nan, inplace=True)
for col in PORTUGUESE_COLS:
    df[col] = df[col].astype(str).str.strip().replace('', np.nan)
    df.loc[df[col].str.len() < MIN_TEXT_LENGTH, col] = np.nan

# Drop rows where both columns are NaN
rows_before = len(df)
df.dropna(subset=PORTUGUESE_COLS, how='all', inplace=True)
rows_after = len(df)
print(f"✅ Cleaning complete: removed {rows_before - rows_after} invalid rows. {rows_after} rows remaining.")

# Ensure translation columns exist
for col in PORTUGUESE_COLS:
    en_col = col + "_en"
    if en_col not in df.columns:
        df[en_col] = np.nan

# -----------------------------
# TRANSLATION FUNCTION
# -----------------------------
def translate_text(text):
    if pd.isna(text) or str(text).strip() == "":
        return np.nan
    text_to_translate = str(text)
    for attempt in range(MAX_RETRIES):
        try:
            return translator.translate(text_to_translate)
        except TooManyRequests:
            print(f"⚠️ Rate limit hit. Sleeping {SLEEP_TIME*(attempt+1)}s...")
            time.sleep(SLEEP_TIME * (attempt+1))
        except TranslationNotFound:
            return np.nan
        except Exception as e:
            print(f"⚠️ General error: {e}. Retrying in {SLEEP_TIME*(attempt+1)}s...")
            time.sleep(SLEEP_TIME * (attempt+1))
    print(f"❌ Failed to translate after {MAX_RETRIES} attempts. Returning NaN.")
    return np.nan

# -----------------------------
# BATCH TRANSLATION
# -----------------------------
total_rows = len(df)
print(f"🔹 Starting translation for {total_rows} rows...")

for start in range(0, total_rows, BATCH_SIZE):
    end = min(start + BATCH_SIZE, total_rows)
    print(f"\n⏳ Translating rows {start} to {end-1}...")

    batch_indices = range(start, end)
    for col in PORTUGUESE_COLS:
        en_col = col + "_en"
        mask = df.index.isin(batch_indices) & df[col].notna() & df[en_col].isna()
        if mask.any():
            df.loc[mask, en_col] = df.loc[mask, col].apply(translate_text)

    # Save progress after each batch
    df.to_excel(FILE_PATH, index=False)
    print(f"✅ Batch {start}-{end-1} saved to Excel.")

print("\n🎉 Translation completed! File saved at:")
print(FILE_PATH)


