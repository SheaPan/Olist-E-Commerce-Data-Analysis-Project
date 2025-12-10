<a name="top"></a>

#  Table of Contents
- [ Olist E-Commerce Data Analytics Project](#-olist-e-commerce-data-analytics-project)
- [ Project Overview](#-project-overview)
- [ Repository Structure](#-repository-structure)
- [ Analysis Sections](#-analysis-sections)
  - [1️. Customer Analysis](#1️-customer-analysis)
  - [2️. Product Analysis](#2️-product-analysis)
  - [3️. Sales Analysis](#3️-sales-analysis)
  - [4️. Delivery Analysis](#4️-delivery-analysis)
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

This repository contains the end-to-end analysis of the **Olist E-commerce dataset**, a Brazilian marketplace with **98,000+ orders (2016–2018)**.

The goal of this project was to deliver:

✔ A business-focused Power BI dashboard  
✔ Insights into customers, sales, products, and delivery performance  
✔ Clean and transformed datasets  
✔ A final written report & presentation  
✔ Python-based translation of Portuguese review text  

All modelling and analysis were done in **Power BI**, with **Python used for translating, sentiment analysis, customer aggregation, and keyword extraction**.

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
| [`image`](./image) | Images of Power BI dashboard. |
| [`scripts`](scripts/README.md) | Python scripts (translation), Power Query scripts, and utility helpers. |
| [`assets`](assets/README.md) | Static assets including charts and reports. |

---

# 📊 Analysis Sections  
[Back to Top](#table-of-contents)

---

## 1️. Customer Analysis
**Focus areas:**
- Portuguese → English translation (Python)
- Sentiment analysis  
- Topic extraction (negative reviews)  
- K-means customer clustering  
- Revenue-at-risk modelling 
- Regional satisfaction 
- Satisfaction trends  

**Deliverables:**

- Overall Risk Overview:

| Metric | Value | Insight|
|--------|-------------|-------------|
| Total Customer Feedback | 98,000 | Strong customer voice, but high volume of reported issues |
| Overall Satisfaction | 0.54 (range from -1 to 1) | Apperas good, but masks significant risks |
| Revenue at Risk | 12.4% | More than 1 in 10 Brazilian Reals could be affected by negative experiences |

- Customer Risk Breakdown:

| Risk Group | % of Customers | Description|
|--------|-------------|-------------|
| High-Risk Detractors | 6.65% | Actively unhappy, giving low scores and negative comments, damaging reputation |
| At-Risk Customers | 15.62% | Silent but dissatisfied, giving low score and no comments, likely to leave |

22.27% of customers are at risk - over one in five.

- High-Stakes Market: Core Risk Focus:

Ji Paraná is a small place with only two customers, but because their orders are of very high value, they create the biggest financial risk (72.3% Risk Revenue) in the whole risk revenue amount. They need fast, personal attention.

São Paulo (SP) is the biggest market and has an average satisfaction score (0.51) that looks “okay” at first. But small issues can scale quickly across thousands of customers.

- Drivers of Dissatisfaction:

Focus should be on the two main issues — product quality and delivery/shipping — and ensure that any problems are resolved promptly when they occur.

- Satisfaction Trend Over Time:

Satisfaction improved in 2017 and remained stable for a while. There is a clear drop at the end of 2018, indicating underlying issues are already affecting customers. If these issues are not addressed promptly, they could snowball into serious revenue and reputational risks.

**Recommendation:**
- A Proactive Rescue Plan for At-Risk Customers (15.62%) - the easiest group to win back. The request is to reach out proactively, listen to concerns, fix issues quickly and personally.
- A Rapid Response Team for High-Value Orders in high-risk markets, preventing negative experiences before they happen. The request is to track high-value orders closely, resolve delivery issues in real time, and protect revenue.
- Steadily improve product quality, delivery issues and customer service to reverse the declining satisfaction. Monitor satisfaction monthly and validate improvements in real outcomes, ensuring issues are shrinking. By combining technical customer segmentation, overall risk analysis, market focus, driver identification, and trend monitoring, these actions can effectively protect revenue and rebuild customer trust.

![Customer Analysis](./image/Customer%20Analysis.jpg)

---

## 2️. Product Analysis
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

## 3️. Sales Analysis
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

## 4️. Delivery Analysis
Focus areas:
- Delivery classification (Early / On-time / Late)  
- Actual vs Estimated delivery  
- Correlation with review scores 
- State-level logistics performance  
- Delayed Outlier States  

Key findings:
- **91.96%** delivered early  
- **Roraima (RR)** had extreme delays (Average Delivery **92 days**)  
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

##  Key Findings Summary  
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
- Watches & Gifts, and Computers dominate overall revenue.  
- Freight cost increase with product weight/volume but show more variability at higher weights/volume.
- Delivery delays are mostly unrelated to product characteristics.
- Regional product preferences differ significantly across Brazil.

---

### Sales Insights  
- Sales peak during holiday and seasonal periods.  
- Credit card is the most commonly used payment method.  
- Revenue displays clear cyclical and seasonal patterns.

---

##  Recommendations  
[Back to Top](#table-of-contents)

### 1. High-Value Order Rapid Response Team  
Prioritise large, high-risk orders in slow-delivery regions.

### 2. Proactive Outreach to At-Risk Customers  
Prevent churn by recovering silent detractors early.

### 3. Improve Logistics in Chronic Delay Regions  
Focus particularly on captial city Boa Vista (Roraima State(RR)) and other outlier states.

### 4. Automated Quality Alerts for Product Issues  
Use negative sentiment spikes to detect emerging product defects early.

---

##  Tools & Technologies  
[Back to Top](#table-of-contents)

### Power BI  
- Star schema data modelling  
- Power Query transformations  
- DAX measures and calculated columns  
- Forecasting and clustering  
- Drill-through interactions and insights  

### Python (used for review translation, sentiment analysis, customer aggregation, and keyword extraction)  
- pandas, numpy  
- deep-translator  
- Batch translation with retry and rate-limit handling  
- VADER for sentiment analysis
- Aggregated customers by review score and sentiment score
- Extracted and summarised review keywords
