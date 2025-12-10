# Delivery Analysis Report – Olist E-commerce Dataset

# Conclusions

### Delivery Performance
- **91.96%** of deliveries were **Early**  
- **6.58%** of deliveries were **Late**  
- **1.46%** of deliveries were **On Time**  

### Delivery Times by State
- Average delivery times across 20 states range from **9 days** (shortest) to **92 days** (longest).
- Average across all the states excluding Roraima is 12.3 days. 
- **Shortest delivery times:** São Paulo (SP) - 4.12 Avg Rating
- **Longest delivery times:** Roraima (RR) - 3.58 Avg Rating

  <img width="1300" height="730" alt="Delivery Time" src="https://github.com/user-attachments/assets/fe2e8d8f-2775-479f-871f-6e3ab6a9ace7" />
  
 Above shows a visual representation, of the delivery insights, including a pie chart for Delviery Performance, and a bar chart for Delivery Times by State.         Stores in states like Sao Paulo with larger customer bases and established practices have the shortest delivery times in the lower percentile, however, states that haven't got established practices, or much smaller customer bases have a correlation with longer delivery times. 


### Relationship Between Delivery Time, Order Value, and Reviews
- Longer deliveries are associated with **lower average review scores**.  
- **Order value** is another factor: higher-value orders tend to take longer to deliver, but their review scores are **not as negatively affected** as lower-value late orders.  
- Possible explanations:  
  - High-value items require **specialized shipping**, additional checkpoints, or handling.  
  - Larger items (cars, sofas, refrigerators) require **specialized equipment** and less automation.  
  - Customers of higher-value items may **expect longer delivery times** and are more tolerant of delays.  
- There exists a **threshold** beyond which even high-value items will negatively affect review scores if delivery takes too long.  
- Low-value items delivered late see a **more pronounced drop in review scores**.

  <img width="1287" height="720" alt="Reviews by State" src="https://github.com/user-attachments/assets/b9311bfc-3148-4ada-b66c-b71ab3c4f5f5" />

  The larger bubbles on the bubble chart correlate to a longer delivery age, and the points along the y axis correlate to higher and lower reviews. We can see a      relationship between average delivery times and average review scores. 
  
  <img width="1307" height="732" alt="Reviews by Order Value" src="https://github.com/user-attachments/assets/5ee53802-a964-46f2-acfc-a7397d08f23d" />

  The line graph shows the relationship between average order value, delivery status and review score. The cards beside the graph show the relationship between avergae order value and delviery status, whichs shows that and the average of value of orders amongst late deliveries is higher than those of early and on time deliveries.

---

# Suggestions

1. **Monitor Late Deliveries:**  
   - Although the majority of deliveries are early, **~7% are late**, with captial city Boa Vista (Roraima) having the highest percentage.  
   - Investigate root causes in this state to isolate contributing factors.

2. **Average Delivery Times:**  
   - Excluding extreme cases, average delivery time is **12.3 days**.  
   - Boa Vista (RR) deliveries are **7.5 times** longer than the average, indicating significant regional delays.

3. **Consider Order Value in Delivery Management:**  
   - Higher-value items take longer but generally do not reduce review scores.  
   - Specialized handling and security measures justify longer delivery times.  
   - For lower-value items, late deliveries **strongly impact review scores**, so prioritize efficiency for these shipments.
   - Adding more staff to work on delivery for Roraima
   - Changing delivery routes for a more effective delivery. 
     

4. **Threshold Awareness:**  
   - Ensure that even high-value orders do not exceed a delivery time threshold that negatively impacts customer satisfaction.

> **Overall Insight:**  
> Deliveries generally run efficiently, but late deliveries, particularly in specific regions or for lower-value items, have a significant impact on customer satisfaction. Optimizing delivery performance by state and order value can improve review scores and overall customer experience.
