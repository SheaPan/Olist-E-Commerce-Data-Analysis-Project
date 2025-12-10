# Olist Dataset – DAX

This file contains all DAX used in the **Olist E-Commerce datasets**.  

---
**Table - `date_table`**

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
- Rolling Avg Revenue = CALCULATE(
  AVERAGEX(
        DATESINPERIOD('Dates'[Date], MAX('Dates'[Date]), -3, MONTH),
        [Total Revenue])
  )
- Revenue StdDev = STDEVX.P(
    VALUES('Dates'[Year-Month]),
    [Total Revenue])
- Revenue Deviation = [Total Revenue] - [Rolling Avg Revenue]
- Revenue by Category = SUM('olist_order_items_dataset'[item_price])
- Revenue % of Total = DIVIDE([Revenue by Category], [Total Orders], 0)
- Profit = olist_order_items_dataset[Total Revenue] - olist_order_items_dataset[Total Freight Cost]
- Outlier Magnitude = ABS([Revenue Deviation])
- Outlier Flag =
  VAR Deviation = [Revenue Deviation]
  VAR Threshold = 1.5 * [Revenue StdDev]
  RETURN
    IF(
        ABS(Deviation) > Threshold,
        "Outlier",
        "Normal"
    )
- Is Outlier =
  IF(
    ABS([Revenue Deviation]) >
    (1.5 * STDEVX.P(VALUES('Dates'[Date]), [Total Revenue])),
    "Outlier",
    "Normal"
  )
- AvgOrderValue = DIVIDE([Total Revenue], [Total Orders], 0)
- AvgFreightPerProduct =
- AVERAGEX(
    VALUES('olist_order_items_dataset'[product_id]),
    CALCULATE(AVERAGE('olist_order_items_dataset'[freight_cost]))
  )
- Average Items per Day =
  AVERAGEX(
    'date_table',
    COALESCE([Total Items Ordered], 0)
  )

**Table - `olist_order_payments_dataset`**

**Table - `olist_orders_dataset`**

**Table - `olist_products_dataset`**

**Table - `olist_reviews_dataset`**

**Table - `olist_review_word_dataset`**
