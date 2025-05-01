from google.cloud import bigquery

def query_weather_table(project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    table = f"`{project_id}.{dataset_id}.{table_id}`"

    # 1) 일별 평균/최대/최소 온도
    sql_agg = f"""
        SELECT
          DATE(timestamp) AS date,
          AVG(temperature_celsius) AS avg_temp,
          MAX(temperature_celsius) AS max_temp,
          MIN(temperature_celsius) AS min_temp
        FROM {table}
        GROUP BY date
        ORDER BY date DESC
    """

    # 2) 평균 이상만 필터링 (서브쿼리 예제)
    sql_sub = f"""
        SELECT *
        FROM {table}
        WHERE temperature_celsius >= (
          SELECT AVG(temperature_celsius)
          FROM {table}
        )
    """

    # 3) 윈도우 함수: 날씨별 온도 순위
    sql_win = f"""
        SELECT
          *,
          ROW_NUMBER() OVER (
            PARTITION BY weather_description
            ORDER BY temperature_celsius DESC
          ) AS temp_rank
        FROM {table}
    """

    for name, sql in [("AGG", sql_agg), ("SUBQUERY", sql_sub), ("WINDOW", sql_win)]:
        print(f"\n=== {name} RESULT ===")
        job = client.query(sql)
        for row in job:
            print(row)

if __name__ == "__main__":
    PROJECT_ID = "future-cat-458304-j8"
    DATASET_ID = "weather_data"
    TABLE_ID   = "weather_20250429"

    query_weather_table(PROJECT_ID, DATASET_ID, TABLE_ID)