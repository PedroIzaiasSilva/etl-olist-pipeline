-- Drop table if exists
DROP TABLE IF EXISTS analytics.fact_sales;

-- Create fact table
CREATE TABLE analytics.fact_sales AS
SELECT
    oi.order_id,
    oi.order_item_id,
    o.customer_id,
    oi.product_id,
    DATE(o.order_purchase_timestamp) AS date_id,

    oi.price,
    oi.freight_value,

    p.payment_type,
    p.payment_installments,
    p.payment_value,

    CURRENT_TIMESTAMP AS created_at
FROM staging.order_items oi
JOIN staging.orders o
    ON oi.order_id = o.order_id
LEFT JOIN staging.payments p
    ON oi.order_id = p.order_id;
