
from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(2023,12,19),
'email': ['stanley7425@gmail.com'],
'retries': 1,
'retry_delay': timedelta(minutes=1)
}

@dag(
    'Testing_Dag2',
    default_args=default_args,
    description='decorators method'
)
def test_flow():
    @task(task_id="my_1st_func",python_callable=my_1st_func)
    def my_1st_func():
        print(1)

    @task(task_id="my_2nd_func",python_callable=my_2nd_func)
    def my_2nd_func():
        print(2)

    @task(task_id="my_3rd_func",python_callable=my_3rd_func)
    def my_3rd_func():
        print(3)

    my_1st_func() >> [my_2nd_func,my_3rd_func]

test_flow()