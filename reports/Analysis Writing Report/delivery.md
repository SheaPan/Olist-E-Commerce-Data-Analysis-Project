# Delivery Analysis Report – Olist E-commerce Dataset

# Conclusions

### Delivery Performance
- **91.96%** of deliveries were **Early**  
- **6.58%** of deliveries were **Late**  
- **1.46%** of deliveries were **On Time**  

### Delivery Times by State
- Average delivery times across 20 states range from **9 days** (shortest) to **92 days** (longest).
- Average across all the states excluding Roraima is **12.3 days**.  
- **Shortest delivery times:** São Paulo (SP) - **4.17 Avg Rating**
- **Longest delivery times:** Roraima (RR) - **3.58 Avg Rating**; (Boa Vista (RR) deliveries are **7.5 times** longer than the average)


![Delivery Analysis](../Power%20BI%20Dashboard%20Image/5_Delivery%20Time.jpg)
  
The above shows a visual representation of the delivery insights, including a pie chart for Delivery Performance, and a bar chart for Delivery Times by State.       Stores in states like Sao Paulo with larger customer bases and established practices have the shortest delivery times in the lower percentile; however, states      that don't got established practices, or much smaller customer bases, have a correlation with longer delivery times. 


### Relationship Between Delivery Time, Order Value, and Reviews

- Longer deliveries are associated with **lower average review scores**.  
- **Order value** is another factor: higher-value orders tend to take longer to deliver, but their review scores are **not as negatively affected** as lower-value    late orders.
- **Threshold Awareness:**  High-value orders have a lesser impact on lower review scores attributed to late delivery; however, there is a threshold where the        value of the order no longer matters if the **delivery is too late**.
  
- Possible explanations:  
  - High-value items require **specialized shipping or handling**.  
  - Larger items (cars, sofas, refrigerators) require **specialised equipment** and cannot be easily automated through delivery processes. 
  - Customers of higher-value items may **expect longer delivery times** and are more tolerant of delays.
  - More **checkpoints and authorisation** needed for higher value items, slowing down delivery.
  - Roraima (RR) has the longest average delivery times due to all but one of its stores being located in the capital city, Boa Vista. Delivery to other parts of     the city will take longer.
 
  

![Delivery Analysis](../Power%20BI%20Dashboard%20Image/6_Delivery-Reviews%20by%20State.jpg)

The larger bubbles on the bubble chart correlate to a longer delivery age, and the points along the y-axis correlate to higher and lower reviews. We can see a      relationship between average delivery times and average review scores. Notably, on the cards, we can see that the longest average delivery times do not correlate with     the lowest average review scores, so there should be further investigation into this. 
  
![Delivery Analysis](../Power%20BI%20Dashboard%20Image/7_Delivery-Reviews%20by%20Order%20Value.png)

The line graph shows the relationship between average order value, delivery status and review score. The cards beside the graph show the relationship between average order value and delivery status, which shows that the average order value of orders amongst late deliveries is higher than that of early and on-time deliveries.

---

# Suggestions 

1. - For lower-value items, late deliveries **strongly impact review scores**, so for lower-value deliveries, prioritise their shipments to deliver first.  
   - Adding more staff to work on delivery for Roraima. 
   - Changing delivery routes to a shorter one for a more effective delivery.
   - Distribute stores more evenly across the cities, so that they aren't concentrated in one area; can attend to customers in all parts of the city. 
     
2. **Threshold Awareness:**  
   - Ensure that even high-value orders do not exceed a delivery time threshold that negatively impacts customer satisfaction.

> **Overall Insight:**  
> Deliveries generally run efficiently, but late deliveries, particularly in Roraima or for lower-value items, have a significant impact on customer satisfaction. Optimising delivery processes for Roraima can help to ensure a more consistent customer satisfaction. 
