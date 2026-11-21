# 🚀 Python Data Engineering Lab: End-to-End ETL Pipelines

![Python](https://img.shields.io/badge/Python-3.13.5-blue?logo=python&logoColor=white)
![Polars](https://img.shields.io/badge/Polars-2.0.0-CD792C?logo=polars&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0.6-150458?logo=pandas&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791?logo=postgresql&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-3.3.2-017CEE?logo=apacheairflow&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-4.2.0-E25A1C?logo=apachespark&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

A comprehensive, hands-on **Data Engineering** repository demonstrating how to build production-style ETL pipelines using modern Python tools. This project covers the entire data lifecycle—from synthetic data generation and high-performance transformations to database loading, resilient API ingestion, automated testing, and workflow orchestration.

---

## 📌 Key Highlights

* **Synthetic Data Generation:** Reproducible order and product datasets generated via `make_data.py` using fixed seeds to simulate real-world edge cases (missing values, duplicates, schema mismatches).
* **Multi-Format Storage & Benchmarking:** Reading, writing, and optimizing storage across **CSV, JSON, JSON Lines (JSONL), and Apache Parquet** using PyArrow.
* **High-Performance Transformations:** Data cleaning, validation, and aggregation using **Pandas** alongside performance benchmarking against **Polars**.
* **Relational Database Integration:** Programmatic SQL execution, schema management, and transactional loading with **SQLite** and **PostgreSQL** (`psycopg`).
* **Resilient API Ingestion:** Consuming paginated REST APIs with structured logging, external configuration management, and exponential backoff retry logic against simulated API failures.
* **Pipeline Testing & Orchestration:** Unit and data-quality testing with **Pytest**, scheduling via **Cron**, workflow orchestration with **Apache Airflow**, and distributed processing fundamentals with **PySpark**.
* **Capstone Mini-Project:** An idempotent, end-to-end weather data pipeline fetching live metrics from the **Open-Meteo API**, validating schemas, and loading into Parquet and SQLite.

---

## 🛠️ Tech Stack & Versions

| Category | Tools & Versions |
| :--- | :--- |
| **Language & Env** | Python `3.13.5`, `uv` `0.13`, VS Code |
| **Data Processing** | `pandas` `3.0.6`, `polars` `2.0.0`, `PyArrow` `26.0.0`, `PySpark` `4.2.0` (Java 21) |
| **Databases** | `SQLite` `3.46`, `PostgreSQL` `17`, `psycopg` `3.3.6` |
| **APIs & Networking** | `requests` `2.34.2` |
| **Testing & Orchestration** | `pytest` `9.1.1`, `Apache Airflow` `3.3.2`, Linux `cron` |

---

## 📂 Repository Structure

```text
python-data-engineering-lab/
├── 01_data_generation_and_formats/   # Synthetic order generator (make_data.py) & CSV/JSONL/Parquet I/O
├── 02_transformations/               # Data cleaning, validation, and Pandas vs. Polars speed benchmarks
├── 03_databases/                     # SQLite & PostgreSQL ingestion, querying, and connection management
├── 04_api_ingestion_and_retries/     # Paginated REST API client, structured logging, configs & retry logic
├── 05_orchestration_and_spark/       # Cron jobs, Apache Airflow DAGs, and PySpark transformations
├── weather_etl_project/              # Capstone Project: Idempotent Open-Meteo ETL pipeline + Pytest suite
├── pyproject.toml                    # Project dependencies managed via uv
└── README.md                         # Project documentation
