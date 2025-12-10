# Olist Dataset – Tables and Columns

This folder contains all raw and cleaned datasets used in the **Olist E-Commerce Data Analytics Project**.  

Below is a reference of all tables, columns, and their usage.

---

## 1. Customer Table (`olist_customers_dataset.csv`)

| Column                | Description                                | Usage |
|-----------------------|--------------------------------------------|-------|
| customer_id           | Unique customer identifier (links to orders) | Link orders to customers |
| customer_unique_id    | Unique customer across multiple orders     | Identify repeat customers |
| customer_zip_code     | ZIP code of the customer                    | Regional segmentation, mapping |
| customer_city         | Customer city                              | Regional insights, mapping |
| customer_state        | Customer state                             | State-level analysis, regional trends |

**Used for:** Customer demographics, linking orders to locations, segmenting reviews by region.

---

## 2. Geolocation Table (`olist_geolocation_dataset.csv`)

| Column                | Description                                | Usage |
|-----------------------|--------------------------------------------|-------|
| geolocation_zipcode    | ZIP code                                   | Map locations, delivery distance analysis |
| latitude              | Geographic latitude                        | Mapping and distance calculations |
| longitude             | Geographic longitude                       | Mapping and distance calculations |
| city                  | City name                                  | Regional analysis |
| state                 | State abbreviation                         | Regional analysis |

**Used for:** Mapping customer/seller locations, delivery distance analysis, and regional product popularity.

---

## 3. Order Items Table (`olist_order_items_dataset.csv`)

| Column                 | Description                                | Usage |
|------------------------|--------------------------------------------|-------|
| order_id               | Links to orders table                      | Connect items to orders |
| order_item_id          | Item sequence number                        | Track multiple items per order |
| product_id             | Product purchased                          | Link products to orders |
| seller_id              | Seller who sold the product                | Seller-level performance |
| shipping_limit_date    | Cutoff date for seller shipping            | Delivery performance |
| item_cost              | Product price                               | Revenue calculation |
| freight_value          | Shipping cost                               | Freight analysis |
| AvgOrderValue          | Pre-calculated average order value         | Customer spending insights |
| Total Sales            | Total sales for this item                   | Revenue analysis |
| total_cost             | Total cost                                  | Profit and margin analysis |
| TotalOrders            | Number of orders for this item             | Order trend analysis |
| TotalRevenue           | Total revenue                               | Sales and revenue analysis |

**Used for:** Sales trend analysis, revenue calculation, product popularity, freight cost analysis, linking products to orders and sellers.

---

## 4. Order Payment Table (`olist_order_payments_dataset.csv`)

| Column                 | Description                                | Usage |
|------------------------|--------------------------------------------|-------|
| order_id               | Links to orders table                       | Connect payments to orders |
| payment_sequential     | Payment number for the order               | Multi-installment tracking |
| payment_type           | e.g., credit card, voucher                 | Payment behavior analysis |
| payment_installments   | Number of installments                     | Payment trend analysis |
| payment_value          | Payment amount                             | Revenue analysis |
| RevenueByPaymentType   | Revenue broken down by payment type        | Understand payment mix |
| TotalPayment           | Total payment                              | Payment reconciliation |

**Used for:** Payment trend analysis, forecasting, and revenue by payment type.

---

## 5. Order Review Table (`olist_reviews_dataset.csv`)

| Column                 | Description                                | Usage |
|------------------------|--------------------------------------------|-------|
| review_id              | Unique ID for review                        | Link review to order |
| order_id               | Links to orders table                       | Connect review to order |
| review_score           | Rating from 1–5                             | Customer satisfaction analysis |
| review_title   | Title of the review                          | Sentiment/topic analysis |
| review_message | Full review text                             | Sentiment/topic analysis |
| sentiment_score | Rating from -1 to 1               | Sentiment/topic analysis |
| sentiment_category | Postive, Negtive and Neutual                | Sentiment/topic analysis |
| cluster_category | Customer segment based on sentiment score                | Customer segment analysis |
| cluster_characteristic | Description of different customer cluster group                | Customer segment analysis |
| review_creation_date   | Date customer wrote the review               | Time trend analysis |
| review_answer_timestamp| When the review was answered                 | Customer service tracking |
| Total Reviews | Total number of reviews                 | Review reconciliation |
| Average Sentiment Score | Average of sentiment score | Sentiment/topic analysis |
| Negative Review Revenue | Revenue from negative reviews | Revenue at risk modelling |
| % Negative Revenue | Percentage of revenue from negative reviews in all revenue| Revenue at risk modelling |

**Used for:** Customer satisfaction, sentiment analysis, clustering review text, linking reviews to products/delivery/sellers.

---

## 6. Orders Table (`olist_orders_dataset.csv`)

| Column                       | Description                                | Usage |
|-------------------------------|--------------------------------------------|-------|
| order_id                     | Unique order identifier                     | Primary key for linking tables |
| customer_id                  | Links to customer table                     | Connect orders to customers |
| order_status                 | Status (delivered, shipped, cancelled, etc.)| Order fulfilment analysis |
| order_purchase_timestamp     | Time order was placed                       | Trend and seasonal analysis |
| order_approved_at            | Payment approval timestamp                  | Payment workflow analysis |
| order_delivered_carrier_date | When carrier received the package           | Delivery logistics analysis |
| order_delivered_customer_date| When customer received the order            | Delivery performance |
| order_estimated_delivery_date| Predicted delivery date                      | Compare actual vs estimated delivery |

**Used for:** Delivery performance, linking customers to products and sellers, and order timelines.

---

## 7. Product Table (`olist_products_dataset.csv`)

| Column                   | Description                                | Usage |
|---------------------------|--------------------------------------------|-------|
| product_id               | Product ID                                  | Primary key |
| product_category_name     | Product category                            | Category analysis |
| product_name_length       | Name length                                 | Data quality / descriptive analysis |
| product_description_length| Description length                           | Data quality / text analysis |
| product_photos_qty        | Number of photos                            | Product listing completeness |
| product_weight            | Weight                                      | Freight and shipping analysis |
| product_length            | Length                                      | Freight and shipping analysis |
| product_height            | Height                                      | Freight and shipping analysis |
| product_width             | Width                                       | Freight and shipping analysis |

**Used for:** Product analysis, shipping cost modelling, linking products to orders and reviews.

---

## 8. Sellers Table (`olist_sellers_dataset.csv`)

| Column          | Description             | Usage |
|-----------------|-------------------------|-------|
| seller_id       | Unique seller identifier| Primary key |
| seller_zip_code | ZIP code                | Regional insights |
| seller_city     | Seller city             | Delivery performance analysis |
| seller_state    | Seller state            | Regional sales and delivery trends |

**Used for:** Delivery performance by seller, linking products to seller location, and regional insights.

---

## 9. Product Category Translation (`product_category_name_translation.csv`)

| Column                | Description                                | Usage |
|-----------------------|--------------------------------------------|-------|
| product_category_name | Category name in Portuguese                | Original category mapping |
| product_category_name_english | Category name in English                | Standardized category name for reporting |

**Used for:** Translating product categories to English for analysis and dashboards.

---

## Notes

- All tables can be linked via primary keys (e.g., `customer_id`, `order_id`, `product_id`, `seller_id`).  


