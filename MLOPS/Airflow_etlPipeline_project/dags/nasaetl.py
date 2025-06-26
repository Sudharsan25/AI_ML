from airflow import DAG
from airflow.providers.http.operators.http import HttpOperator
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
import json

## Define the DAG

with DAG(
    dag_id = "nasa_etl_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule = "@weekly",
    catchup = False,
) as dag:
    
    ## Step 1: Create a table if it does not exist in Postgres
    @task
    def create_table_postgres():
        ## Initalize Postgres Hook
        postgres_hook = PostgresHook(postgres_conn_id='postgres_connection')

        ## Define SQL query
        create_table_query = """
        CREATE TABLE IF NOT EXISTS nasa_apod_data(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE,
            media_type VARCHAR(50)
        );
        """

        ## Execute the query
        postgres_hook.run(create_table_query)
        
        
    ## Step 2: Extract the NASA API data (APOD)
    extract_apod_data = HttpOperator(
        task_id = 'extract_nasa_apod_data',
        http_conn_id = 'nasa_api', # <- connection id defined in Airflow for Nasa API
        endpoint = 'planetary/apod',
        method = 'GET',
        data = {"api_key":"{{conn.nasa_api.extra_dejson.api_key}}"}, 
        response_filter = lambda response:response.json(), # <- convert response to JSON format
    )
    ## Step 3: Transform the data (Extract necessary fields)
    @task
    def transform_nasa_apod_data(response):
        nasa_apod_data = {
            'title': response.get('title',""),
            'explanation': response.get('explanation',""),
            'url': response.get('url', ""),
            'date': response.get('date',""),
            'media_type': response.get('media_type', "")
            
        }

        return nasa_apod_data
    ## Step 4: Load the data into Postgres
    @task
    def load_nasa_apod_data_to_postgres(nasa_apod_data):
        postgres_hook = PostgresHook(postgres_conn_id='postgres_connection')

        insert_query = """
        INSERT INTO nasa_apod_data (title, explanation, url, date, media_type)
        VALUES (%s, %s, %s, %s, %s)
        """

        postgres_hook.run(insert_query, parameters=(
            nasa_apod_data['title'],
            nasa_apod_data['explanation'],
            nasa_apod_data['url'],
            nasa_apod_data['date'],
            nasa_apod_data['media_type']
        ) )
    ## Step 5: Veryify the data with DBViewer

    ## Step 6: Define task dependencies
    create_table_task_instance = create_table_postgres()

    create_table_task_instance >> extract_apod_data

    transformed_nasa_apod_data_result = transform_nasa_apod_data(
        extract_apod_data.output
    )
    
    load_nasa_apod_data_to_postgres(
        transformed_nasa_apod_data_result
    )

