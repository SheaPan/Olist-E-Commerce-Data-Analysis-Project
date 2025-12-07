<a name="top"></a>

#  Table of Contents
- [ Olist E-Commerce Data Analytics Project](#-olist-e-commerce-data-analytics-project)
- [ Project Overview](#-project-overview)
- [ Repository Structure](#-repository-structure)
- [ Analysis Sections](#-analysis-sections)
  - [1️. Customer Analysis (Xue)](#1️-customer-analysis-xue)
  - [2️. Product Analysis (Rebecca)](#2️-product-analysis-rebecca)
  - [3️. Sales Analysis (Bijal)](#3️-sales-analysis-bijal)
  - [4️. Delivery Analysis (Lina)](#4️-delivery-analysis-lina)
- [ Review Translation (Python – VS Code)](#-review-translation-python--vs-code)
- [ Key Findings Summary](#-key-findings-summary)
  - [ Customer Insights](#-customer-insights)
  - [ Delivery Insights](#-delivery-insights)
  - [ Product Insights](#-product-insights)
  - [ Sales Insights](#-sales-insights)
- [ Recommendations](#-recommendations)
- [ Tools & Technologies](#-tools--technologies)

---

#  Olist E-Commerce Data Analytics Project  
### **UK Data Analyst Bootcamp – Final Group Project (Group 2)**  
[Back to Top](#table-of-contents)

**Team Members & Roles**
- **Xue** – Customer Analysis + NLP + Sentiment  
- **Lina** – Delivery Performance Analysis  
- **Rebecca** – Product Analysis  
- **Bijal** – Sales Analysis  

**Project Completion:** 9 December 2025  
**Presentation Date:** 9 December 2025  

---

#  Project Overview  
[Back to Top](#table-of-contents)

This repository contains the end-to-end analysis of the **Olist E-commerce dataset**, a Brazilian marketplace with **100,000+ orders (2016–2018)**.

The goal of this project was to deliver:

✔ A business-focused Power BI dashboard  
✔ Insights into customers, sales, products, delivery performance  
✔ Clean and transformed datasets  
✔ A final written report & presentation  
✔ Python-based translation of Portuguese review text  

All modelling and analysis were done in **Power BI**, with **Python used only for translating review text**.

---

#  Repository Structure & Folder Descriptions 
[Back to Top](#table-of-contents)

---

| Folder | Description |
|--------|-------------|
| [`data`](data/README.md) | Raw, cleaned, and dictionary datasets for analysis. |
| [`reports`](reports/README.md) | Final outputs including Power BI dashboards, presentations, and written reports. |
| [`analysis`](analysis/README.md) | Scripts and outputs for customer, product, sales, and delivery analyses. |
| [`dax`](dax/README.md) | DAX measures, calculated columns, and data model definitions for Power BI. |
| [`scripts`](scripts/README.md) | Python scripts (translation), Power Query scripts, and utility helpers. |
| [`assets`](assets/README.md) | Static assets including charts and reports. |

---

#  Analysis Sections  
[Back to Top](#table-of-contents)

---

## 1️. Customer Analysis (Xue)  
Focus areas:
- Portuguese → English translation (Python)
- Sentiment analysis  
- Topic extraction (negative reviews)  
- K-means customer clustering  
- Revenue-at-risk modelling  
- Satisfaction trends  
- Regional heatmaps  

Deliverables:
- Word clouds  
- Sentiment distributions  
- High-risk customer list  
- PCA cluster plot  

---

## 2️. Product Analysis (Rebecca)  
Focus areas:
- Category performance  
- Freight vs weight/dimensions  
- Regional preferences  
- Seasonal trends  
- Product features influencing reviews  

Deliverables:
- Category revenue charts  
- Freight cost modelling  
- Regional demand heatmaps  

---

## 3️. Sales Analysis (Bijal)  
Focus areas:
- Monthly & yearly revenue  
- Power BI forecasting  
- Payment behaviour trends  
- AOV (Average Order Value)  
- Customer retention + cohort analysis  

Deliverables:
- Forecast visualisations  
- Payment method analysis  
- Revenue cycle charts  

---

## 4️. Delivery Analysis (Lina)  
Focus areas:
- Delivery classification (Early / On-time / Late)  
- Actual vs Estimated delivery  
- Review score correlation  
- State-level logistics performance  
- Delay outlier states  

Key findings:
- **91.96%** delivered early  
- **Boa Vista (RR)** had extreme delays (up to **92 days**)  
- Long delivery strongly correlates with low reviews  
- High-value orders take longer but reviews remain stable  

---

#  Review Translation (Python – VS Code)  
[Back to Top](#table-of-contents)

Power BI cannot translate 50k+ text rows, handle API limits, or resume safely after failures.

Python enabled:
- Robust text cleaning  
- Deep-translator (Google backend)  
- Batch translation (500 rows)  
- Resume-safe workflow  
- Retry & rate-limit handling  

Script location: [translate_reviews.py](scripts/translate_reviews.py)
```python
# (Full script included in (scripts/translate_reviews.py)
# Translates Portuguese reviews to English with retry logic and batching.
```

## Key Findings Summary  
[Back to Top](#table-of-contents)

### Customer Insights  
- 22.27% of customers are at risk.  
- Negative reviews focus on defects, delays, and cancellations.  
- Satisfaction declined sharply in late 2018.

---

### Delivery Insights  
- Delivery delays are the main cause of negative reviews.  
- Certain states (such as Roraima – RR) have extremely long delivery times.  
- High-value orders take longer to deliver but maintain higher satisfaction.

---

### Product Insights  
- Electronics and furniture dominate overall revenue.  
- Freight cost is strongly correlated with product weight and dimensions.  
- Regional product preferences differ significantly across Brazil.

---

### Sales Insights  
- Sales peak during holiday and seasonal periods.  
- Credit card is the most commonly used payment method.  
- Revenue displays clear cyclical and seasonal patterns.

---

## Recommendations  
[Back to Top](#table-of-contents)

### 1. High-Value Order Rapid Response Team  
Prioritise large, high-risk orders in slow-delivery regions.

### 2. Proactive Outreach to At-Risk Customers  
Prevent churn by recovering silent detractors early.

### 3. Improve Logistics in Chronic Delay Regions  
Focus particularly on Boa Vista (RR) and other outlier states.

### 4. Automated Quality Alerts for Product Issues  
Use negative sentiment spikes to detect emerging product defects early.

---

## Tools & Technologies  
[Back to Top](#table-of-contents)

### Power BI  
- Star schema data modelling  
- Power Query transformations  
- DAX measures and calculated columns  
- Forecasting and clustering  
- Drill-through interactions and insights  

### Python (used for review translation only)  
- pandas, numpy  
- deep-translator  
- Batch translation  
- Retry and rate-limit handling
