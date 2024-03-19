from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(2023,12,19),
'email': ['stanley7425@gmail.com'],
'retries': 1,
'retry_delay': timedelta(minutes=1)

}
    
def my_1st_func():
    print(1)

def my_2nd_func():
    print(2)

def my_3rd_func():
    print(12345123)

with DAG(
    'Testing_Dag',
    default_args=default_args,
    description='my first dag'

) as DAG:

    first_function_execute = PythonOperator(
        task_id="my_1st_func",
        python_callable=my_1st_func
    )

    second_function_execute = PythonOperator(
        task_id="my_2nd_func",
        python_callable=my_2nd_func
    )

    third_function_execute = PythonOperator(
        task_id="my_3rd_func",
        python_callable=my_3rd_func
    )

    first_function_execute >> [second_function_execute, third_function_execute]
