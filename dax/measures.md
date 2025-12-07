# DAX Measures & Calculated Columns Documentation

This document contains all DAX measures and calculated columns used in the **Olist E-Commerce Power BI model**.

It is organised by dataset/table for clarity.

---

## Order Items Table (`olist_order_items_dataset`)

### Measures

| Measure Name                 | DAX Formula / Expression | Description / Purpose |
|-------------------------------|------------------------|---------------------|
| Total Revenue                | `SUM('olist_order_payments_dataset'[payment_value])` | Tracks the total money received from customers according to payment data. Useful for reconciling revenue from items with actual payments. |
| Total Orders                 | `DISTINCTCOUNT('olist_order_payments_dataset'[order_id])` | Tracks order volume over time. Helps identify if growth comes from more orders or larger orders. |
| AOV (Average Order Value)    | `DIVIDE([Total Revenue], [Total Orders], 0)` | Calculates average revenue per order. Useful for understanding customer spending behavior. |
| Revenue by Category          | `SUMX('olist_order_items_dataset','olist_order_items_dataset'[item_price])` | Total revenue aggregated by product category. |
| Revenue % of Total           | `DIVIDE([Revenue by Category], [Total Revenue], 0)` | Shows each category's share of total revenue. |
| Total Freight Cost           | `SUM('olist_order_items_dataset'[freight_cost])` | Aggregates all freight costs. |
| Orders per Month (optional)  | `COUNTROWS('olist_orders_dataset')` | Counts orders per month. |

---

## Dates Table

### Calculated Table

| Table / Column | DAX Formula / Expression | Description |
|----------------|------------------------|------------|
| Dates          | `ADDCOLUMNS(CALENDAR(DATE(2016,1,1), DATE(2018,12,31)), "Year", YEAR([Date]), "Month Number", MONTH([Date]), "Month Name", FORMAT([Date], "MMMM"), "Year-Month", FORMAT([Date], "YYYY-MM"))` | Generates a full date table with year, month, and Year-Month columns for time intelligence. |

---

## Orders Table (`olist_orders_dataset`)

### Calculated Columns

| Column Name             | DAX Formula / Expression | Description / Purpose |
|-------------------------|------------------------|---------------------|
| Purchase Date           | `DATE(YEAR([order_purchase_timestamp]), MONTH([order_purchase_timestamp]), DAY([order_purchase_timestamp]))` | Extracts just the date part of the purchase timestamp. |
| Delivery Time (Day)     | `DATEDIFF([order_approved_at],[order_delivered_customer_date], DAY)` | Calculates actual delivery duration in days. |
| Delivery Time (Estimate DAY) | `DATEDIFF([order_approved_at],[order_estimated_delivery_date], DAY)` | Calculates estimated delivery duration in days. |
| Delivery Late/Early     | `[Delivery Time (Estimate DAY)] - [Delivery Time (Day)]` | Difference between estimated and actual delivery times. |
| Delivery Status         | `IF([Delivery Late/Early]>0,"Early",IF([Delivery Late/Early]=0,"On Time","Late"))` | Categorizes deliveries as Early, On Time, or Late. |

### Measures

| Measure Name                     | DAX Formula / Expression | Description / Purpose |
|----------------------------------|------------------------|---------------------|
| Average Delivery Time by Seller Location (State) | `CALCULATE(AVERAGEX('olist_order_items_dataset', RELATED('olist_orders_dataset'[Delivery Time (Day)])))` | Computes average delivery time grouped by seller location/state. |
| Average Review Score by State     | `AVERAGE('olist_order_reviews_dataset'[review_score])` | Computes mean review score per state. |
| Count of Early Deliveries         | `CALCULATE(COUNTROWS('olist_orders_dataset'), 'olist_orders_dataset'[Delivery Status]="Early")` | Counts the number of early deliveries. |
| Count of Late Deliveries          | `CALCULATE(COUNTROWS('olist_orders_dataset'), 'olist_orders_dataset'[Delivery Status]="Late")` | Counts the number of late deliveries. |
| Count of On Time Deliveries       | `CALCULATE(COUNTROWS('olist_orders_dataset'), 'olist_orders_dataset'[Delivery Status]="On Time")` | Counts the number of on-time deliveries. |

---

## Notes

- All measures and calculated columns were created in **Power BI Desktop**.  
