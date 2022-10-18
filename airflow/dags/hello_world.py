from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import scrapy
import scrapy_playwright

def print_hello():
    return 'Hello world from first Airflow DAG!'

def fuck_you():
    return 'fuck you'

dag = DAG('hello_world', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

hello_operator = PythonOperator(task_id='hello_task', python_callable=print_hello, dag=dag)

fuck_you_operator = PythonOperator(task_id='fuck_you_task', python_callable=fuck_you, dag=dag)

hello_operator
fuck_you