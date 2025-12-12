# Customer Analysis – Olist E-commerce Dataset

## Introduction
This project analyses a real-world dataset of **98,000 customer feedback entries** to understand customer experience, identify high-risk groups, and provide actionable recommendations. The goal is to combine technical analysis with business insights to guide strategic actions.

---

## Understanding Customer Segments: Cluster Analysis (Technical Foundation)

To gain a deeper understanding of customers, we performed a **cluster analysis** combining customer ratings and comment sentiment.

**Technical Approach:**
- Pre-processed customer comments for sentiment analysis.
- Created a combined metric using numerical ratings + sentiment scores.
- Segmented customers into meaningful groups, revealing patterns beyond simple satisfaction scores.

**Summary of Segments:**
- **Enthusiastic Advocates:** Highly satisfied and vocal; potential source for testimonials or positive insights.
- **Positive Patrons:** Generally happy; small improvements could further strengthen loyalty.
- **At-Risk Customers:** Low satisfaction, low emotional intensity; high risk of quietly leaving.
- **High-Risk Detractors:** Actively dissatisfied; urgent attention needed.

**Key Insight:**  
Segmentation provides a foundation for identifying high-risk customers and potential advocates, helping focus business actions more effectively while demonstrating how sentiment analysis adds depth to traditional scores.

---
**Customer Analysis Dashboard**

![Customer Analysis](../assets/Customer%20Analysis.jpg)

---

## 1. Overall Risk Overview

### Key Signals from the Dataset
| Metric | Value | Insight |
|--------|-------|--------|
| Total Customer Feedback | 98,000 | Strong customer voice, but high volume of reported issues |
| Overall Satisfaction Index | 0.54 | Appears good, but masks significant risks |
| Revenue at Risk | 13.2% | More than 1 in 10 people could be affected by negative experiences |

### Customer Risk Breakdown
| Risk Group | % of Customers | Description |
|------------|----------------|------------|
| High-Risk Detractors | 6.65% | Actively unhappy, damaging reputation |
| At-Risk Customers | 15.62% | Silent but dissatisfied, likely to leave |

> **Insight:** 22.27% of customers are at risk — over one in five. Underlying issues are already affecting customers, and if left unaddressed, could escalate.

---

## 2. High-Stakes Market: Core Risk Focus

- **Ji Paraná:** Only two customers, but extremely high-value orders. Represents **72.3% of risk revenue** — requires fast, personal attention.
- **São Paulo (SP):** Largest market with an average satisfaction score of 0.51. Small issues here can scale quickly across thousands of customers.

**Insight:**  
An immediate, high-touch recovery effort is needed in Ji Paraná, while SP requires sustained, structural improvements to lift satisfaction and secure long-term revenue.

---

## 3. Drivers of Dissatisfaction

Analysis of high-risk customers reveals three main themes:

| Topic | Insight |
|-------|--------|
| Product Quality | Indicates potential long-term quality control or supplier issues |
| Delivery & Shipping | Negative experiences occur quickly, especially for expensive orders |
| Order & Billing / Customer Service | Contributes to dissatisfaction and requires attention |

> **Focus:** Address product quality and delivery/shipping issues promptly.

---

## 4. Satisfaction Trend Over Time

- Satisfaction improved in 2017 and remained stable for a while.
- A clear drop at the end of 2018 indicates underlying issues are affecting customers.
- If unaddressed, these issues could snowball into serious revenue and reputational risks.

---

## Recommended Actions

Based on insights from segmentation and risk analysis:

1. **Rapid Response Team for High-Value Orders**
   - **Target:** Highest-risk market (Ji Paraná)
   - **Goal:** Prevent negative experiences before they happen
   - **Actions:** Track high-value orders closely, resolve delivery issues in real time, protect revenue

2. **Proactive Rescue Plan for At-Risk Customers (15.62%)**
   - **Target:** Silent but unhappy customers
   - **Actions:** Reach out proactively, listen to concerns, fix issues quickly and personally

3. **Turn the Declining Satisfaction Trend Around**
   - **Goal:** Show steady improvement over the next three months
   - **Actions:** Monitor satisfaction monthly, validate improvements in real outcomes, ensure issues are shrinking

> **Summary:** Combining technical segmentation, risk analysis, market focus, and trend monitoring can effectively protect revenue and rebuild customer trust.
