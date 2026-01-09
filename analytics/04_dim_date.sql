-- Drop table if exists
DROP TABLE IF EXISTS analytics.dim_date;

-- Create date dimension
CREATE TABLE analytics.dim_date AS
SELECT DISTINCT
    DATE(order_purchase_timestamp) AS date_id,
    EXTRACT(YEAR FROM order_purchase_timestamp) AS year,
    EXTRACT(MONTH FROM order_purchase_timestamp) AS month,
    EXTRACT(DAY FROM order_purchase_timestamp) AS day,
    EXTRACT(WEEK FROM order_purchase_timestamp) AS week,
    EXTRACT(DOW FROM order_purchase_timestamp) AS day_of_week,
    TO_CHAR(order_purchase_timestamp, 'Month') AS month_name,
    CASE
        WHEN EXTRACT(DOW FROM order_purchase_timestamp) IN(0,6)
        THEN TRUE
        ELSE FALSE
    END AS is_weekend,
    CURRENT_TIMESTAMP AS created_at
FROM staging.orders
WHERE order_purchase_timestamp IS NOT NULL;