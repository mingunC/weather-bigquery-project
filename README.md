# weather-bigquery-project

> **Fully automated** weather data ETL & reporting pipeline:
> 1) OpenWeather API → GCS  
> 2) GCS → BigQuery  
> 3) BigQuery SQL Analysis → CSV report  
> 4) Automatically execute daily with the GitHub Actions scheduler 

---

## Repository Structure
```text
## weather-bigquery-project/
├── .github/
│   └── workflows/
│       └── bq_pipeline.yml      # GitHub Actions 워크플로우
├── data/
│   └── processed/               # 7일 리포트 CSV
├── scripts/
│   ├── fetch_weather_data.py    # 1. API → raw JSON
│   ├── transform_weather_data.py# 2. JSON → DataFrame → newline-JSON
│   ├── upload_to_gcs.py         # 3. GCS 업로드
│   ├── load_data_to_bigquery.py # 4. BigQuery 적재
│   ├── query_bigquery_data.py   # 5. 집계/윈도우 SQL 예제
│   └── query_last7days.py       # 6. 7일 리포트 CSV 생성
├── .gitignore
└── README.md
```

## Prerequisites
Python 3.9
Service Account Key (JSON)
GCP Project, BigQuery API, GCS Bucket
GitHub Repository & GCP_SA_KEY Secret

## Install packages in the local virtual environment
pip install \
  google-cloud-bigquery \
  pandas \

## Local execution example
1) Collect weather data → GCS
  python scripts/fetch_weather_data.py
  python scripts/transform_weather_data.py
  python scripts/upload_to_gcs.py

2) Load into BigQuery
  python scripts/load_data_to_bigquery.py
3) SQL analysis script
  python scripts/query_bigquery_data.py
4) Generate 7-day report (CSV)  
  python scripts/query_last7days.py
   → data/processed/last7days_YYYYMMDD.csv

## GitHub Actions Automation
As configured in /.github/workflows/bq_pipeline.yml, the following steps (1-4) will be executed sequentially:

Daily at 06:00 UTC
Manually (via Workflow Dispatch)


