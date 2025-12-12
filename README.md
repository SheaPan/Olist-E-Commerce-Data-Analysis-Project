# 🛒 Olist E-Commerce Data Analytics Project 

Group Name: Byte Me

Date: December 2025

Duration: 3 days

---
# 📝 Project Overview  

This repository contains an **end-to-end analysis** of the Olist E-commerce Dataset, sourced from Brazil’s largest online marketplace integrator.
Olist connects small sellers across the country to major digital sales channels through a unified platform. When a customer places an order, the seller is notified, prepares the package, and ships it via Olist’s logistics partners. After delivery—or once the expected delivery date has passed—the customer is invited to complete a short review survey.

This operational flow generates a large, detailed dataset that spans:

- Orders and order status
- Payments and pricing
- Product characteristics
- Delivery timelines and logistics performance
- Customer locations and demographics
- Customer ratings and written reviews

The full dataset includes over **99,000 orders between 2016 and 2018**, providing a rich foundation for uncovering business patterns.
Our analysis focuses on **sales trends, product insights, delivery performance,** and **customer feedback** to help Olist increase revenue, optimise operations, and uphold customer satisfaction.

## 🛠️ Project Instructions

This project aims to analyse the Olist E-commerce Dataset to extract **actionable insights** across four major business dimensions: **customer satisfaction, product performance, sales behaviour, and delivery efficiency**.

**The workflow combines:**

- Exploratory Data Analysis (EDA)
- Predictive modelling
- Power BI dashboards for interactive visualisation
- Python for tasks including translation, sentiment analysis, customer-level aggregation, keyword extraction, and automated data processing.

**Key Objectives:**

1. Evaluate customer sentiment and behaviour.
2. Identify product popularity, pricing, and regional trends.
3. Analyse sales patterns and forecast future revenue.
4. Assess delivery performance and its impact on customer satisfaction.

## 🔗 Database Schema, Table Structure & Entity Relationship Overview




## 📁 Folder Structure

- [ Olist E-Commerce Data Analytics Project](#-olist-e-commerce-data-analytics-project)
- [ Analysis Sections](#-analysis-sections)
  - [1️. Sales Analysis](#1️-sales-analysis)
  - [2️. Product Analysis](#2️-product-analysis)
  - [3️. Delivery Analysis](#3️-delivery-analysis)
  - [4️. Customer Analysis](#4️-customer-analysis)
- [ Review Translation (Python – VS Code)](#-review-translation-python--vs-code)
- [ Key Findings Summary](#-key-findings-summary)
  - [ Sales Insights](#-sales-insights)
  - [ Product Insights](#-product-insights)
  - [ Delivery Insights](#-delivery-insights)
  - [ Customer Insights](#-customer-insights)
- [ Recommendations](#-recommendations)
- [ Tools & Technologies](#-tools--technologies)

---

| Folder | Description |
|--------|-------------|
| [`data`](data/README.md) | Raw datasets for analysis. |
| [`reports`](reports/README.md) | Final outputs including Power BI dashboards, presentations, and written reports. |
| [`analysis`](analysis/README.md) | Scripts and outputs for customer, product, sales, and delivery analyses. |
| [`dax`](dax/README.md) | DAX measures, calculated columns, and data model definitions for Power BI. |
| [`scripts`](scripts/README.md) | Python scripts (translation), Power Query scripts, and utility helpers. |
| [`assets`](assets/README.md) | Static assets including charts and reports. |

---

## 📊 Analysis Sections  

### 1️. Sales Analysis
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

Insights:
- Sales peak during holiday and seasonal periods.  
- Credit card is the most commonly used payment method.  
- Revenue displays clear cyclical and seasonal patterns.

Sales Analysis location: [Analysis Writing Report/sales.md](Analysis%20Writing%20Report/sales.md) 

### 2️. Product Analysis
Focus areas:
- Category performance and seasonal trends  
- Customer review scores by product category
- Freight vs weight/dimensions
- Delivery delays vs weight/dimensions

Deliverables:
- Category revenue & popularity charts
- Customer review score analysis
- Freight cost and delivery delays modelling in relation to product dimensions

Insights:
- Watches & Gifts, and Computers dominate overall revenue.  
- Freight cost increases with product weight/volume, but shows more variability at higher weights/volumes.
- Delivery delays are mostly unrelated to product characteristics.

Product Analysis location: [analysis/Product.md](analysis/sales.md) 

### 3️. - Delivery Analysis
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
- High-value orders take longer, but reviews remain stable

Insights:
- Delivery delays are the main cause of negative reviews.  
- Certain states (such as Roraima – RR) have extremely long delivery times.  
- High-value orders take longer to deliver but maintain higher satisfaction.

Delivery Analysis location: [analysis/Delivery.md](analysis/sales.md) 

### 4️. Customer Analysis
**Focus areas:**
- Portuguese → English translation (Python)
- Sentiment analysis  
- Topic extraction (negative reviews)  
- K-means customer clustering  
- Revenue-at-risk modelling 
- Regional satisfaction 
- Satisfaction trends  

**Deliverables:**
- Customer segments analysis pie chart
- Regional satisfaction analysis scatter chart
- Customer review topics and keywords treemap
- satisfaction trend line chart

Insights:
- 22.27% of customers are at risk.
- The smallest market and the largest market are both in danger.
- Negative reviews focus on product quality, delivery delays, and cancellations.  
- Satisfaction declined sharply in late 2018.

Customer Analysis location: [analysis/sales.md](analysis/sales.md) 

###  Recommendations  

1. High-Value Order Rapid Response Team  
Prioritise large, high-risk orders in slow-delivery regions.

2. Proactive Outreach to At-Risk Customers  
Prevent churn by recovering silent detractors early.

3. Improve Logistics in Chronic Delay Regions  
Focus particularly on captial city, Boa Vista (Roraima State(RR)), and other outlier states.

4. Automated Quality Alerts for Product Issues  
Use negative sentiment spikes to detect emerging product defects early.


## 🔧 Tools & Technologies  
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
