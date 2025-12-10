# Olist Dataset – DAX

This file contains all DAX used in the **Olist E-Commerce datasets**.  

---
**Table - `date_table`**

Table:
- date_table = calendarauto()

New Columns:
- Year = YEAR('date_table'[Date])
- Quarter = 'date_table'[Year] & " Q"
    & IF(
        MONTH('date_table'[Date]) <= 3,
        1,
        IF(
            MONTH('date_table'[Date]) <= 6,
            2,
            IF(
                MONTH('date_table'[Date]) <= 9,
                3,
                4
            )
        )
    )
- Month = FORMAT('date_table'[Date], "yyyy MMM")
- MonthKey = (YEAR('date_table'[Date]) * 100) + MONTH('date_table'[Date])

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
- YoY % Growth = DIVIDE(
    [Total Revenue] - [YoY Revenue],
    [YoY Revenue],
    0)

**Table - `olist_order_payments_dataset`**

New Measures:
- TotalPayment = SUM('olist_order_payments_dataset'[payment_value])
- Total Sales = SUM('olist_order_payments_dataset'[payment_value])
- Sales Amt = SUM('olist_order_payments_dataset'[payment_value])
- Revenue by Item = SUM('olist_order_items_dataset'[item_price])
- Average Daily Sales =
  DIVIDE(
    [Total Sales],
    DISTINCTCOUNT('date_table'[Date])
  )

**Table - `olist_orders_dataset`**

New Columns:
- Purchase Date = DATE(
    YEAR([order_purchase_timestamp]),
    MONTH([order_purchase_timestamp]),
    DAY([order_purchase_timestamp])
  )
- DeliveryDelayDays = DATEDIFF(
    'olist_orders_dataset'[order_estimated_delivery_date],
    'olist_orders_dataset'[order_delivered_customer_date],
    DAY)
- Delivery Time (Estimate DAY) = DATEDIFF('olist_orders_dataset'[order_approved_at], 'olist_orders_dataset'[order_estimated_delivery_date], DAY) 
- Delivery Time (Day) = DATEDIFF('olist_orders_dataset'[order_approved_at],'olist_orders_dataset'[order_delivered_customer_date], DAY)
- Delivery Status =
  IF('olist_orders_dataset'[Delivery Late/Early] > 0, "Early",
  IF('olist_orders_dataset'[Delivery Late/Early] = 0, "On Time", "Late")) 
- Delivery Late/Early = 'olist_orders_dataset'[Delivery Time (Estimate DAY)] - 'olist_orders_dataset'[Delivery Time (Day)]

New Measures:
- YoY Revenue = CALCULATE(
    [Total Revenue],
    DATEADD('Dates'[Date], -1, YEAR))
- Count of On Time Deliveries = CALCULATE(COUNTROWS('olist_orders_dataset'),'olist_orders_dataset'[Delivery Status] = "On Time")
- Count of Late Deliveries = CALCULATE(COUNTROWS('olist_orders_dataset'), 'olist_orders_dataset'[Delivery Status] = "Late")
- Count of Early Deliveries = CALCULATE(COUNTROWS('olist_orders_dataset'),'olist_orders_dataset'[Delivery Status] = "Early")
- Avg Delivery Time = AVERAGEX(
    'olist_orders_dataset',DATEDIFF(
        'olist_orders_dataset'[order_approved_at],
        'olist_orders_dataset'[order_delivered_customer_date],
        DAY)
  )
- Average Review Score by State = AVERAGE( 'olist_reviews_dataset'[review_score])
- Average Delivery Time by Seller Location(State) = CALCULATE (
  AVERAGEX ('olist_order_items_dataset', RELATED ('olist_orders_dataset'[Delivery Time (Day)])
  ))


**Table - `olist_products_dataset`**

New Columns:
- ProductDensity_g_per_cm3 = DIVIDE(
    olist_products_dataset[product_weight_g],
    olist_products_dataset[ProductVolume_cm3],
    BLANK()
  )
- ProductVolume_cm3 =
  olist_products_dataset[product_height_cm] *
  olist_products_dataset[product_width_cm] *
  olist_products_dataset[product_length_cm]

New Measure: 
- Product_category_count = DISTINCTCOUNT(olist_products_dataset[product_category_name])

**Table - `olist_reviews_dataset`**

New Measure:
- Total Reviews = DISTINCTCOUNT(olist_reviews_dataset[review_id])
- Negative Review Revenue = CALCULATE(
    'olist_order_items_dataset'[Total Revenue],
    FILTER(
        'olist_reviews_dataset',
        'olist_reviews_dataset'[sentiment_category] = "Negative"
    ))
- Average Sentiment Score = AVERAGE(olist_reviews_dataset[sentiment_score])
- % Negative Revenue = DIVIDE(
    [Negative Review Revenue],
    [Total Revenue],
    0)

**Table - `olist_review_word_dataset`**
