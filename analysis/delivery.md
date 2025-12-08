# Delivery Analysis Report – Olist E-commerce Dataset

# Conclusions

### Delivery Performance
- **91.96%** of deliveries were **Early**  
- **6.58%** of deliveries were **Late**  
- **1.46%** of deliveries were **On Time**  

### Delivery Times by State
- Average delivery times across 20 states range from **9 days** (shortest) to **92 days** (longest).  
- **Shortest delivery times:** São Paulo (SP)  
- **Longest delivery times:** Boa Vista (RR)  

### Relationship Between Delivery Time, Order Value, and Reviews
- Longer deliveries are associated with **lower average review scores**.  
- **Order value** is another factor: higher-value orders tend to take longer to deliver, but their review scores are **not as negatively affected** as lower-value late orders.  
- Possible explanations:  
  - High-value items require **specialized shipping**, additional checkpoints, or handling.  
  - Larger items (cars, sofas, refrigerators) require **specialized equipment** and less automation.  
  - Customers of higher-value items may **expect longer delivery times** and are more tolerant of delays.  
- There exists a **threshold** beyond which even high-value items will negatively affect review scores if delivery takes too long.  
- Low-value items delivered late see a **more pronounced drop in review scores**.

---

# Suggestions

1. **Monitor Late Deliveries:**  
   - Although the majority of deliveries are early, **~7% are late**, with Boa Vista (RR) having the highest percentage.  
   - Investigate root causes in this state to isolate contributing factors.

2. **Average Delivery Times:**  
   - Excluding extreme cases, average delivery time is **24.9 days**.  
   - Boa Vista (RR) deliveries are **3.69 times** longer than the average, indicating significant regional delays.

3. **Consider Order Value in Delivery Management:**  
   - Higher-value items take longer but generally do not reduce review scores.  
   - Specialized handling and security measures justify longer delivery times.  
   - For lower-value items, late deliveries **strongly impact review scores**, so prioritize efficiency for these shipments.

4. **Threshold Awareness:**  
   - Ensure that even high-value orders do not exceed a delivery time threshold that negatively impacts customer satisfaction.

> **Overall Insight:**  
> Deliveries generally run efficiently, but late deliveries, particularly in specific regions or for lower-value items, have a significant impact on customer satisfaction. Optimizing delivery performance by state and order value can improve review scores and overall customer experience.
