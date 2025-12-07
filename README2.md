# Olist E-Commerce Data Analytics Project  
### UK Data Analyst Bootcamp – Final Group Project (Group 2)

**Team Members & Roles**  
- **Xue** - Customer Analysis + NLP + Sentiment  
- **Lina** - Delivery Performance Analysis  
- **Rebecca** - Product Analysis  
- **Bijal** - Sales Analysis  

**Project Completion:** 9 December 2025  
**Presentation Date:** 9 December 2025  

---

# Project Overview

This repository contains the full end-to-end analysis of the **Olist E-commerce dataset**, a Brazilian marketplace with over 100,000 orders (2016–2018).  

The project goal was to deliver:  
- A business-focused Power BI dashboard  
- Insights into customers, sales, products, and delivery performance  
- Cleaned and transformed datasets  
- A final written report and presentation  
- Python-based translation of Portuguese review text  

All modeling, analysis, and visualization were performed in **Power BI**, with **Python used only for translating reviews**.

---

# Repository Structure & Folder Descriptions

| Folder | Description |
|--------|-------------|
| [`data`](data/README.md) | Raw, cleaned, and dictionary datasets for analysis. |
| [`reports`](reports/README.md) | Final outputs including Power BI dashboards, presentations, and written reports. |
| [`analysis`](analysis/README.md) | Scripts and outputs for customer, product, sales, and delivery analyses. |
| [`dax`](dax/README.md) | DAX measures, calculated columns, and data model definitions for Power BI. |
| [`scripts`](scripts/README.md) | Python scripts (translation), Power Query scripts, and utility helpers. |
| [`assets`](assets/README.md) | Static assets including charts, team photos, and logos used in dashboards or reports. |

---

# Key Findings & Recommendations

## Customer Insights ([Customer Analysis](analysis/customer/README.md))
- **22.27% of customers at risk** (silent + vocal detractors)  
- Negative reviews focus on **product defects, delivery delays, and cancellations**  
- Customer satisfaction **sharply declined in late 2018**  

## Delivery Insights ([Delivery Analysis](analysis/delivery/README.md))
- Delivery delays are the **main cause of negative reviews**  
- Some states (e.g., **Roraima – RR**) have extremely long delivery times  
- High-value orders take longer but **maintain higher satisfaction**  

## Product Insights ([Product Analysis](analysis/product/README.md))
- **Electronics & furniture** dominate revenue  
- Freight cost **correlates with weight and dimensions**  
- Regional product preferences vary significantly  

## Sales Insights ([Sales Analysis](analysis/sales/README.md))
- Sales peak during **holidays & seasonal periods**  
- **Credit card** is the most used payment method  
- Revenue shows **clear cyclic patterns**  

## Recommendations
1. **High-Value Order Rapid Response Team**  
   - Prioritize large, high-risk orders in slow-delivery regions  

2. **Proactive Outreach to At-Risk Customers**  
   - Prevent churn by recovering silent detractors early  

3. **Improve Logistics in Chronic Delay Regions**  
   - Focus on Boa Vista (RR) and other outlier states  

4. **Automated Quality Alerts for Product Issues**  
   - Use negative sentiment spikes to detect emerging product defects early  

---

# Review Translation (Python – VS Code)

- Portuguese review comments were translated to English using Python  
- Batch translation, retry logic, and error handling implemented  
- Script location: [`scripts/python/translate_reviews.py`](scripts/python/translate_reviews.py)

---

# Tools & Technologies

### Power BI
- Star schema data modeling  
- Power Query transformations  
- DAX measures & calculated columns  
- Forecasting & clustering visuals  
- Drill-through interactions  

### Python (Review Translation Only)
- `pandas`, `numpy`  
- `deep-translator`  
- Batch processing with retry and rate-limit handling  

---

# Usage Notes

1. Always use datasets from `/data/cleaned` for analysis or Power BI dashboards.  
2. Reference `/dax` for measure definitions and KPIs.  
3. Use `/scripts/python/translate_reviews.py` only if re-translation is needed.  
4. Final outputs are stored in `/reports` and visual assets in `/assets/high_res_charts`.  

---

# License
Include your license information here if applicable.
