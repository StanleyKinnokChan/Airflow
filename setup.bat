pip install apache-airflow==2.7.3 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.3/constraints-3.8.txt"
airflow db init  
airflow webserver -p 8080