-- Drop table if exists (idempotente)
DROP TABLE IF EXISTS analytics.dim_customers;

-- Create dimension table
CREATE TABLE analytics.dim_customers AS
SELECT
    customer_id,
    customer_unique_id,
    customer_zip_code_prefix,
    customer_city,
    customer_state,
    CURRENT_TIMESTAMP AS created_at
FROM staging.customers;