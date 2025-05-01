from google.cloud import bigquery

def load_json_from_gcs_to_bq(project_id, dataset_id, table_id, gcs_uri):
    client = bigquery.Client(project=project_id)
    table_ref = client.dataset(dataset_id).table(table_id)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    load_job = client.load_table_from_uri(
        gcs_uri,
        table_ref,
        job_config=job_config
    )
    print(f"Starting job {load_job.job_id}…")
    load_job.result()
    print(f"Loaded {load_job.output_rows} rows into {project_id}.{dataset_id}.{table_id}.")

if __name__ == "__main__":
    PROJECT_ID   = "your-gcp-project-id"
    DATASET_ID   = "weather_data"
    TABLE_ID     = "weather_20250429"
    GCS_URI      = "gs://your-bucket/weather_data/processed_weather_YYYYMMDD_ld.json"

    load_json_from_gcs_to_bq(PROJECT_ID, DATASET_ID, TABLE_ID, GCS_URI)