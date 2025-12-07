#  Olist E-Commerce Data Analytics Project  
### **UK Data Analyst Bootcamp – Final Group Project (Group 2)**

**Team Members & Roles**
- **Xue** - Customer Analysis + NLP + Sentiment  
- **Lina** - Delivery Performance Analysis  
- **Rebecca** - Product Analysis  
- **Bijal** - Sales Analysis  

**Project Completion:** 9 December 2025  
**Presentation Date:** 9 December 2025  

---

#  Project Overview  

This repository contains the full end-to-end analysis of the **Olist E-commerce dataset** — a Brazilian marketplace with **100,000+ orders (2016–2018)**.

The goal of this project was to deliver:

✔ A complete, business-focused Power BI dashboard  
✔ Deep insights into customers, sales, products, and delivery performance  
✔ Clean and transformed datasets  
✔ A final written report and presentation  
✔ Python-based translation of Portuguese text for review analysis  

All modelling, analysis, and visualisation were performed in **Power BI**, with **Python used only to translate review text** for later sentiment and clustering analysis.

---

#  Repository Structure  

/data
/raw → Original datasets
/cleaned → Cleaned & transformed datasets
/dictionary → Data schema & definitions

/reports
/PowerBI → Final Power BI (.pbix) file
/presentation → Final slide deck
/written_report → Written documentation

/analysis
/customer → NLP, sentiment, segmentation
/product → Category, freight, seasonal patterns
/sales → Revenue, forecasting, payment trends
/delivery → Delivery status modelling + review correlation

/dax → All DAX measures, columns, model schema
/scripts
/python → Translation code (performed in VS Code)
/powerquery → Power Query M-scripts
/utils → Supporting helpers

/assets
/high_res_charts → Exported Power BI visuals
/team_photos
/logos

README.md
.gitignore


---

#  Analysis Sections

## 1️. Customer Analysis (Xue)  
Focus areas:
- Portuguese → English translation (via Python)
- Sentiment analysis for all reviews  
- Topic extraction for negative comments  
- K-means clustering (customer groups)  
- Revenue-at-risk modeling  
- Customer satisfaction trends  
- Regional satisfaction heatmaps  

Deliverables:
- Word clouds  
- Sentiment distributions  
- High-risk customer identification  
- PCA cluster visualisation  
- Full reasoning in `/analysis/customer/`

---

## 2️. Product Analysis (Rebecca)  
Focus areas:
- Product category performance  
- Freight value vs. weight & dimensions  
- Regional product preferences  
- Seasonal & category-level trends  
- Product attributes impacting review score  

Deliverables:
- Category revenue insights  
- Freight cost modelling  
- Regional demand heatmaps  
- Complaint topics tied to product attributes  

---

## 3️. Sales Analysis (Bijal)  
Focus areas:
- Monthly & yearly revenue trends  
- Time-series forecasting (Power BI)  
- Payment method behaviour  
- Average order value analysis  
- Customer retention & cohort analysis  

Deliverables:
- Forecast visuals  
- AOV trends  
- Sales breakdown by payment type  

---

## 4. Delivery Analysis (Lina)  
Focus areas:
- Delivery status classification (Early / On-time / Late)  
- Delivery time calculation (actual vs estimated)  
- Review score impact  
- State-by-state logistics performance  
- High-delay outlier locations  

Key findings:
- **91.96%** of orders were delivered **early**  
- **Boa Vista (RR)** had the longest delivery times (up to **92 days**)  
- Delays are strongly linked to low review scores  
- Higher-value items take longer but customers tolerate delays better  

---

# Review Translation (Python – VS Code)

Although Power BI was used for the majority of the analysis, review comments were in **Portuguese** and required translation before performing sentiment analysis.

We used **Visual Studio Code + Python** to translate all review titles and messages.

Script location:  
/scripts/python/translate_reviews.py


### Why Python Was Needed  
Power BI cannot:
- Translate 50k+ text rows reliably  
- Handle API limits  
- Batch process text  
- Resume translation after interruption  

Python provided:
- Robust text cleaning  
- Deep-Translator (Google backend)  
- Batch translation (500 rows at a time)  
- Resume-safe workflow  
- Automated error handling  

Below is the exact script used (also stored in the repo):

### 🔧 translate_reviews.py  
```python
# (Full script included in scripts/python/translate_reviews.py)
# Translates Portuguese reviews to English with retry logic and batching.


---

### Why Python Was Needed  
Power BI cannot:
- Translate 50k+ text rows reliably  
- Handle API limits  
- Batch process text  
- Resume translation after interruption  

Python provided:
- Robust text cleaning  
- Deep-Translator (Google backend)  
- Batch translation (500 rows at a time)  
- Resume-safe workflow  
- Automated error handling  

Below is the exact script used (also stored in the repo):

### translate_reviews.py  
```python
# (Full script included in scripts/python/translate_reviews.py)
# Translates Portuguese reviews to English with retry logic and batching.

##  Key Findings Summary  

###  Customer Insights  
- **22.27% of customers are at risk** (silent + vocal detractors).  
- Negative reviews focus on **product defects, delivery delays, and cancellations**.  
- Customer satisfaction **sharply declined in late 2018**.

---

###  Delivery Insights  
- **Delivery delay** is the main driver of negative reviews.  
- Certain states (e.g., **Roraima – RR**) exhibit extremely long delivery times.  
- High-value orders take longer but **customers tolerate delays better**.

---

###  Product Insights  
- **Electronics and furniture** categories dominate overall revenue.  
- Freight cost is **strongly correlated** with product weight and dimensions.  
- **Regional preferences** for product categories vary significantly across Brazil.

---

###  Sales Insights  
- Sales peak during **holidays and seasonal events**.  
- **Credit card payments** dominate transaction volume.  
- Revenue displays **clear cyclical patterns** across months and years.

---

##  Recommendations  

### 1. **Create a High-Value Order Rapid Response Team**  
Focus on preventing dissatisfaction, especially in high-delay regions.

### 2. **Proactive Outreach to At-Risk Customers**  
Recover silent detractors before churn impacts revenue.

### 3. **Strengthen Logistics in Chronic Delay Regions**  
Boa Vista (RR) and other outlier states require targeted optimisation.

### 4. **Automated Quality Alerts for Product Issues**  
Use sentiment spikes to flag emerging product-related problems early.

---

##  Tools & Technologies  

### **Power BI**
- Star schema data modelling  
- Power Query transformations  
- DAX measures & calculated columns  
- AI visuals (clustering, forecasting)  
- Drill-through interactions and tooltips  

### **Python (Used Only for Review Translation)**
- `pandas`, `numpy`  
- `deep-translator` (Google backend)  
- Batch processing  
- Retry & rate-limit handling  

