from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from datetime import datetime

## Define first task
def preprocess():
    print("Pre-processing incoming data")

## Define second task
def train_model():
    print("Training model....")

## Define third task
def evaluate_model():
    print("Evaluate model....")

# Define DAG
with DAG(
    'custom_pipeline',
    start_date = datetime(2025,1,1),
    schedule = '@weekly', # < ---- Changed from schedule_interval from Airflow 2.0 or higher,
    catchup = False,
) as dag:
    
    # Define tasks using PythonOperator
    # Note: In Airflow 2.0 or higher, you can use the @
    # preprocess_ = PythonOperator(task_id="preprocess_task", python_callable = preprocess)
    # train = PythonOperator(task_id="training_task", python_callable = train_model)
    # evaluate = PythonOperator(task_id="evaluate_task", python_callable = evaluate_model)
    

    @task
    def preprocess_():
        return "Pre-processing data..."
    
    @task
    def train():
        return "Training model..."
    
    @task
    def evaluate():
        return "Evaluating model..."
    
    ## set dependencies 
    preprocessed = preprocess_()
    trained = train()
    evaluated = evaluate()
