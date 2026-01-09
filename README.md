# End-to-End Batch ETL Pipeline — Olist Dataset

## Overview

This project implements an end-to-end batch ETL (Extract, Transform, Load) pipeline
using the Olist public dataset.

The objective is to apply data engineering best practices to ingest raw data,
transform it into structured layers, and persist analytical datasets into a
relational database.

This project reflects my transition from Data Analyst to Data Engineer, with a strong
focus on data architecture, modular pipelines, reproducibility, and containerized
execution.

---

## Data Architecture

The pipeline follows a layered data architecture commonly adopted in data engineering
projects:

- **Raw**: Original source data with no transformations
- **Staging**: Cleaned, standardized, and validated data
- **Analytics**: Business-ready datasets optimized for analytical use cases

```
Raw → Staging → Analytics → Database
```

---

## Tech Stack

- **Python** — ETL logic and data transformations
- **PostgreSQL** — Data persistence layer
- **Docker** — Containerized execution
- **Docker Compose** — Pipeline orchestration

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

1. **Extract**
   - Reads source datasets from the raw layer
   - Performs basic ingestion and validation

2. **Transform**
   - Cleans and standardizes data
   - Applies transformations for downstream consumption
   - Writes processed data into staging and analytics layers

3. **Load**
   - Loads analytical datasets into a PostgreSQL database
   - Initializes schemas and tables using SQL scripts

---

## How to Run

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone the repository

```bash
git clone <repository-url>
cd <repository-name>
```

2. Run the ETL pipeline

```bash
docker-compose up
```

---

## Environment Variables

Sensitive configurations are managed using a `.env` file, which is intentionally
excluded from version control.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=analytics
DB_USER=user
DB_PASSWORD=password
```

---

## Notes

- Large datasets and generated files are excluded from the repository
- Folder structure is versioned using `.gitkeep` files
- Database initialization is handled via Docker entrypoint scripts
- The project prioritizes code quality, clarity, and scalable architecture

---

## Future Improvements

- Add data quality checks and validation rules
- Introduce logging and monitoring
- Integrate workflow orchestration (e.g., Apache Airflow)
- Add unit tests for ETL logic
- Extend the pipeline for incremental loads

---

## Author

Pedro Izaías  
Data Analyst | Aspiring Data Engineer