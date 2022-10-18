from airflow.operators.bash import BashOperator
import os
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow import DAG

dag = DAG('scrapy_dag', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

# scrapy_task = BashOperator(
#     task_id='scrapy',
#     # bash_command='cd scrapers && scrapy crawl example',
#     # bash_command='scrapy crawl example',
#     dag=dag,
# )

# scrapy_task

def fuck_you():
    for i in os.listdir('.'):
        print(i)
    return os.getcwd()

fuck_you_operator = PythonOperator(task_id='fuck_you_task', python_callable=fuck_you, dag=dag)

fuck_you_operator