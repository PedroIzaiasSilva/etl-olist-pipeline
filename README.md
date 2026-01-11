# End-to-End Batch ETL Pipeline — Olist Dataset

## Overview

This project implements an end-to-end batch ETL (Extract, Transform, Load) pipeline
using the **Olist Brazilian E-commerce Dataset**.

The objective is to apply data engineering best practices to ingest raw data,
transform it into structured layers, and persist analytical datasets into a
relational database for business analysis.

This project reflects my transition from Data Analyst to Data Engineer, with a strong
focus on data architecture, modular pipelines, reproducibility, and containerized
execution.

---

## Dataset

- **Source**: Olist Brazilian E-commerce Dataset (Kaggle)
- **Link**: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains information about orders, customers, products, sellers,
payments, and deliveries from a large Brazilian e-commerce marketplace.

---

## Data Architecture

The pipeline follows a layered data architecture commonly adopted in data engineering
projects:

- **Raw**: Original source data with no transformations
- **Staging**: Cleaned, standardized, and validated data
- **Analytics**: Business-ready dimensional and fact tables

### Architecture Diagram

```
                ┌───────────────┐
                │   Kaggle CSVs │
                └───────┬───────┘
                        │
                        ▼
                ┌────────────────┐
                │      RAW       │
                │  data/raw/     │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │    STAGING     │
                │ data/staging/ │
                │ cleaned data  │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────────┐
                │    ANALYTICS       │
                │ data/analytics/   │
                │ fact & dimensions │
                └───────┬────────────┘
                        │
                        ▼
                ┌────────────────────┐
                │   PostgreSQL DW    │
                │  analytics schema │
                └────────────────────┘
```

---

## Tech Stack

- **Python** — ETL logic and data transformations
- **PostgreSQL** — Data Warehouse and analytics layer
- **Docker** — Containerized execution
- **Docker Compose** — Service orchestration

---

## Project Structure

```text
.
├── data/
│   ├── raw/
│   ├── staging/
│   └── analytics/
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── docker/
│   └── postgres/
│       └── init.sql
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## ETL Flow

### 1. Extract
- Reads CSV datasets from the raw layer
- Applies schema validation and basic consistency checks

### 2. Transform
- Data cleaning and normalization
- Standardization of column names and data types
- Creation of analytical datasets (dimensions and fact tables)

### 3. Load
- Loads analytics tables into PostgreSQL
- Organizes data using an analytical schema
- Ensures reproducible database initialization

---

## Analytics Layer

The analytics schema follows a dimensional modeling approach:

- **dim_products**
- **dim_customers**
- **dim_date**
- **fact_sales**

This structure enables efficient analytical queries and reporting.

---

## Example Analytical Queries

### Total Revenue by Year

```sql
SELECT
    d.year,
    SUM(f.payment_value) AS total_revenue
FROM analytics.fact_sales f
JOIN analytics.dim_date d
    ON f.date_id = d.date_id
GROUP BY d.year
ORDER BY d.year;
```

### Top 10 Products by Revenue

```sql
SELECT
    p.product_category_name,
    SUM(f.payment_value) AS revenue
FROM analytics.fact_sales f
JOIN analytics.dim_products p
    ON f.product_id = p.product_id
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;
```

### Average Freight Cost per Payment Type

```sql
SELECT
    f.payment_type,
    AVG(f.freight_value) AS avg_freight_cost
FROM analytics.fact_sales f
GROUP BY f.payment_type
ORDER BY avg_freight_cost DESC;
```

---

## How to Run

### Prerequisites

- Docker
- Docker Compose

### Steps

```bash
git clone <repository-url>
cd <repository-name>
docker-compose up
```

---

## Environment Variables

Sensitive configurations are managed using a `.env` file, excluded from version control.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=analytics
DB_USER=user
DB_PASSWORD=password
```

---

## Notes

- Large datasets are not versioned in the repository
- Directory structure is preserved using `.gitkeep`
- Database initialization runs automatically via Docker entrypoint scripts
- Focus on clarity, reproducibility, and analytics-ready data

---

## Author

Pedro Izaías  
Data Analyst | Aspiring Data Engineer
