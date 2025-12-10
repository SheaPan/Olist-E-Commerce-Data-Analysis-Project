# Olist Dataset – DAX

This file contains all DAX used in the **Olist E-Commerce datasets**.  

---

**Table - `olist_order_item_dataset`**

New Columns:
- product_weight_g = RELATED(olist_products_dataset[product_weight_g])
- ProductVolume_cm3 = RELATED(olist_products_dataset[ProductVolume_cm3])

New Measures:
- Total Revenue = SUM('olist_order_payments_dataset'[payment_value])
- Total Orders = DISTINCTCOUNT('olist_order_payments_dataset'[order_id])
- Total Items Ordered = SUM('olist_order_items_dataset'[order_item_id])
- Total Freight Cost = SUM('olist_order_items_dataset'[freight_cost])
- Total Items Ordered = SUM('olist_order_items_dataset'[order_item_id])
- Rolling Avg Revenue = CALCULATE(AVERAGEX(
        DATESINPERIOD('Dates'[Date], MAX('Dates'[Date]), -3, MONTH),
        [Total Revenue]))
- Revenue StdDev = STDEVX.P(
    VALUES('Dates'[Year-Month]),
    [Total Revenue])
- Revenue Deviation = [Total Revenue] - [Rolling Avg Revenue]
