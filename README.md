# ETL Pipeline -- Olist Dataset

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline using
the Olist public dataset. The goal is to ingest raw data, apply
transformations, and organize it into structured data layers following
data engineering best practices.

The project is designed to be modular, scalable, and reproducible using
containerized execution.

------------------------------------------------------------------------

## Data Architecture

The pipeline follows a layered data architecture commonly used in data
engineering projects:

-   **Raw**: Original source data with no transformations
-   **Staging**: Cleaned, standardized, and validated data
-   **Analytics**: Business-ready datasets optimized for analysis

```{=html}
<!-- -->
```
    raw → staging → analytics

------------------------------------------------------------------------

## Tech Stack

-   Python
-   Docker
-   Docker Compose

------------------------------------------------------------------------

## Project Structure

``` text
.
├── data/
│   ├── raw/
│   ├── staging/
│   └── analytics/
│
├── etl/
│   ├── extract.py
│   └── transform.py
│
├── docker/
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

## ETL Flow

1.  **Extract**
    -   Reads source files from the raw layer
    -   Performs basic validation and ingestion
2.  **Transform**
    -   Cleans and standardizes data
    -   Applies transformations for downstream usage
    -   Writes processed data into staging and analytics layers

------------------------------------------------------------------------

## How to Run

### Prerequisites

-   Docker
-   Docker Compose

### Steps

1.  Clone the repository

``` bash
git clone <repository-url>
cd <repository-name>
```

2.  Run the pipeline

``` bash
docker-compose up
```

------------------------------------------------------------------------

## Environment Variables

Sensitive configurations are managed using a `.env` file, which is
intentionally excluded from version control.

Example:

``` env
DB_HOST=localhost
DB_USER=user
DB_PASSWORD=password
```

------------------------------------------------------------------------

## Notes

-   Large datasets and generated files are excluded from the repository
-   Folder structure is versioned using `.gitkeep` files
-   The project focuses on code quality and architectural clarity

------------------------------------------------------------------------

## Future Improvements

-   Add a load layer to persist data into a database or data warehouse
-   Implement data quality checks
-   Add logging and monitoring
-   Integrate workflow orchestration (e.g., Airflow)
-   Add unit tests for transformations

------------------------------------------------------------------------

## Author

Pedro Izaías
