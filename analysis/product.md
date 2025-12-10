# Product Analysis Report – Olist E-commerce Dataset

# Olist Product Analysis

This analysis covers Olist's 72 product categories over the period **October 2016 – September 2018**. It examines revenue, popularity, customer reviews, freight costs, and delivery performance to provide actionable insights.

---

## 1. Top Product Categories

### Revenue Leaders
Across the full sales period, the highest revenue categories are:

| Category              | Revenue  |
|-----------------------|----------|
| Watches & Gifts       | 225,704  |
| Computer Accessories  | 167,224  |
| Health & Beauty       | 163,084  |

**Quarterly Revenue Dynamics**

- **Watches & Gifts** and **Computer Accessories** perform strongly in every quarter.  
- **Health & Beauty** consistently ranks in the top 3 during **Q2, Q3, and Q4**.  
- **Sports & Leisure** rises into the top 3 in **Q1**, replacing Health & Beauty, indicating early-year seasonal demand, or new-year up-lift in customer spend on fitness-related products.

### Popularity Leaders (Units Sold)
Most frequently purchased categories:

- Health & Beauty   
- Sports & Leisure
- Computer Accessories

**Quarterly patterns:**  

- **Computer Accessories** lead in **Q1 and Q4**.  
- **Health & Beauty** leads in **Q2 and Q3**.  

**Key Insight:**  

- Popularity does not always align with revenue.  
- High-revenue categories often sell fewer but higher-priced items (e.g., Watches & Gifts).  
- High-popularity categories sometimes sell high volumes of lower-priced products (e.g., Health & Beauty).

---

## 2. Customer Reviews

- Most product categories (**96%**) have average review scores above **3/5**, showing broad customer satisfaction.  
- Underperforming categories include:  

| Category               | Average Score |
|------------------------|---------------|
| DVDs/Blu-ray           | 1             |
| Male Fashion Clothing  | 2.25          |
| Construction Tools     | 3             |

**Recommendation:**  
Target underperforming categories with:

- Product quality checks  
- Seller audits  
- Packaging improvements  
- Enhanced product information (e.g., sizing guidance)

---

## 3. Freight Cost Drivers

- Freight costs increase with **product weight and volume**, as expected.  
- Variability arises for **larger/heavier items**. So two products with very similar higher weight or size can have very different shipping charges. Outliers may be influenced by:  

  - Shipping distance  
  - Packaging behavior  
  - Carrier pricing rules  
  - Seller-specific logistics practices  

**Recommendation:**  

- Standardize packaging guidelines  
- Review pricing rules for bulky items  
- Investigate extreme outliers to remove inefficiencies

---

## 4. Delivery Delays

- Most deliveries are **on time or early**.  
- **Moderate delays** (under ~14 days) happen across all product types and have little relation to weight or size. Operational or supplier issues may play a role.  
- **Long delays** (over 14 days) -	Occur more rarely among bulky items. And mostly affect smaller, lightweight items, - but with a small sample size, it’s harder to draw meaningful conclusions.

Overall, delivery delays are largely unrelated to physical product characteristics.

**Recommendation:**  

- Monitor delivery delays at the **seller/region level**, not by product type  
- Implement **early-warning analytics** for unusual fulfillment times

---

## Overall Conclusions

- **Revenue Drivers:** Watches & Gifts, Computer Accessories, Health & Beauty  
- **Popularity Leaders (Units Sold):** Health & Beauty, Sports & Leisure, Computer Accessories 
- **Seasonal Patterns:** Sports & Leisure revenue peaks in Q1; Computer Accessories units sold are highest in Q1 and Q4  
- **Customer Satisfaction:** Dissatisfaction concentrated in a small set of categories  
- **Freight Costs:** Increase with weight/volume but show operational variability at higher weights/volume  
- **Delivery Delays:** Mostly unrelated to product characteristics; better monitored by seller/region

---

