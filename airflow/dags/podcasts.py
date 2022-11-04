from airflow.operators.bash import BashOperator
import os
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow import DAG

dag = DAG('the_daily_podcast_dag', description='Hello World DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2017, 3, 20), catchup=False)

scrapy_task = BashOperator(
    task_id='scrapy',
    bash_command='scrapy crawl the-daily-podcast',
    cwd='scrapers',
    dag=dag,
)

scrapy_task

# convert the above code into a TaskFlow API pattern

# from airflow.decorators import dag, task
# from datetime import datetime

# @dag(description='Hello World DAG', schedule_interval='0 12 * * *', start_date=datetime(2017, 3, 20), catchup=False)
# def the_daily_podcast_dag():
#     @task()
#     def scrapy():
#         return os.system('scrapy crawl the-daily-podcast')

#     scrapy()

# the_daily_podcast_dag = the_daily_podcast_dag()


# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings


# print("starting scrapy")

# process = CrawlerProcess(get_project_settings())
# process.crawl('example')
# process.start()



# def fuck_you():
#     for i in os.listdir('.'):
#         print(i)
#     return os.getcwd()

# fuck_you_operator = PythonOperator(task_id='fuck_you_task', python_callable=fuck_you, dag=dag)

# fuck_you_operator