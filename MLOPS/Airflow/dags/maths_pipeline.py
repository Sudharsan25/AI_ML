'''
1: Start with an initial number
2. Add 5 to the number
3. Multiply the result by 2
4. Subtract 3 from the result
5. Compute the square of the result
'''

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def start_number(**context):
    context["ti"].xcom_push(key='current_value', value=10)
    print("Starting number 10")

def add_five(**context):
    current_val = context['ti'].xcom_pull(key="current_value", task_ids="start_task")
    new_value = current_val + 5
    context["ti"].xcom_push(key='current_value', value=new_value)
    print("Adding 5 to the start number")

def subtract_three(**context):
    current_val = context['ti'].xcom_pull(key="current_value", task_ids="add_task")
    new_value = current_val - 3
    context["ti"].xcom_push(key='current_value', value=new_value)
    print("Subtracting 3 from the new value")

def compute_square(**context):
    current_val = context['ti'].xcom_pull(key="current_value", task_ids="sub_task")
    new_value = current_val ** 2
    context["ti"].xcom_push(key='current_value', value=new_value)
    print("Computing square of the value:",new_value)


with DAG(
    dag_id = 'maths_pipeline',
    start_date = datetime(2023,1,1),
    schedule = '@once',
    catchup = False
) as dag:
    
    start_task = PythonOperator(task_id = 'start_task', python_callable=start_number) # provide_context=True was removed from Apache 2.0 or higher
    
    add_task = PythonOperator(task_id = 'add_task', python_callable=add_five)
    
    sub_task = PythonOperator(task_id = 'sub_task', python_callable=subtract_three)
    
    square_task = PythonOperator(task_id = 'square_task', python_callable=compute_square)
    
    start_task >> add_task >> sub_task >> square_task