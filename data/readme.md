# Data Folder

This folder contains all raw and cleaned datasets used in the Olist E-commerce Data Analytics Project.

## Subfolders

### `/raw`
- Contains original datasets as provided by Olist.
- Files should **not be modified**.
- Examples: `orders.csv`, `products.csv`.

### `/cleaned`
- Contains cleaned and transformed datasets used for analysis.
- These are generated after preprocessing steps (e.g., removing NaNs, standardizing column names).
- Examples: `orders_cleaned.csv`, `products_cleaned.csv`.

### `/dictionary`
- Contains schema, data dictionaries, and definitions for each dataset.
- Helps understand each column and its meaning.

## Notes
- Always keep the raw folder unchanged to ensure reproducibility.
- Use cleaned datasets for analysis and Power BI imports.
