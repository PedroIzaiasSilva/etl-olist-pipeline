-- Drop table if exists
DROP TABLE IF EXISTS analytics.dim_products;

-- Create dimension table
CREATE TABLE analytics.dim_products AS
SELECT
    product_id,
    product_category_name,
    product_weight_g,
    product_length_cm,
    product_height_cm,
    product_width_cm,
    CURRENT_TIMESTAMP AS created_at
FROM staging.products;