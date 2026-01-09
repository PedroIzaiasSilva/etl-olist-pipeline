-- Creation of the analysis scheme
CREATE SCHEMA IF NOT EXISTS analytics;

GRANT USAGE ON SCHEMA analytics TO etl_user;
GRANT create on SCHEMA analytics to etl_user;