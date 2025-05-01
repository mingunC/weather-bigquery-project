from google.cloud import bigquery

def query_weather_table(project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    table = f"`{project_id}.{dataset_id}.{table_id}`"

    sql = f"""
    SELECT
      DATE(timestamp) AS date,
      AVG(temperature_celsius) AS avg_temp,
      COUNT(*) AS cnt
    FROM {table}
    GROUP BY date
    ORDER BY date DESC
    LIMIT 7
    """

    job = client.query(sql)
    print("=== Last 7 days avg temp ===")
    for row in job:
        print(f"{row.date}: {row.avg_temp:.2f}°C over {row.cnt} records")

if __name__ == "__main__":
    PROJECT_ID = "your-gcp-project-id"
    DATASET_ID = "weather_data"
    TABLE_ID   = "weather_20250429"

    query_weather_table(PROJECT_ID, DATASET_ID, TABLE_ID)