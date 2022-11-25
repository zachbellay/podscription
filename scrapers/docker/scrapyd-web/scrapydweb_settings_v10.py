# uncompyle6 version 3.8.0
# Python bytecode 3.6 (3379)
# Decompiled from: Python 3.7.1 (default, Nov 24 2022, 23:38:57) 
# [GCC 11.3.0]
# Embedded file name: /app/scrapydweb_settings_v10.py
# Compiled at: 2022-11-20 22:21:07
# Size of source mod 2**32: 17821 bytes
"""
How ScrapydWeb works:
BROWSER <<<>>> SCRAPYDWEB_BIND:SCRAPYDWEB_PORT <<<>>> your SCRAPYD_SERVERS

GitHub: https://github.com/my8100/scrapydweb
DOCS: https://github.com/my8100/files/blob/master/scrapydweb/README.md
文档：https://github.com/my8100/files/blob/master/scrapydweb/README_CN.md
"""
import os
SCRAPYDWEB_BIND = '0.0.0.0'
SCRAPYDWEB_PORT = 5000
ENABLE_AUTH = False
USERNAME = ''
PASSWORD = ''
scrapyd_servers = os.environ.get('SCRAPYD_SERVERS', '')
SCRAPYD_SERVERS = [
 scrapyd_servers,
 ('username', 'password', 'localhost', '6801', 'group')]
LOCAL_SCRAPYD_SERVER = ''
LOCAL_SCRAPYD_LOGS_DIR = ''
ENABLE_LOGPARSER = False
ENABLE_HTTPS = False
CERTIFICATE_FILEPATH = ''
PRIVATEKEY_FILEPATH = ''
SCRAPY_PROJECTS_DIR = os.environ.get('SCRAPY_PROJECTS_DIR', '')
SCRAPYD_LOG_EXTENSIONS = [
 '.log', '.log.gz', '.txt']
SCRAPYD_SERVERS_PUBLIC_URLS = None
BACKUP_STATS_JSON_FILE = True
JOBS_SNAPSHOT_INTERVAL = 300
SCHEDULE_EXPAND_SETTINGS_ARGUMENTS = False
SCHEDULE_CUSTOM_USER_AGENT = 'Mozilla/5.0'
SCHEDULE_USER_AGENT = None
SCHEDULE_ROBOTSTXT_OBEY = None
SCHEDULE_COOKIES_ENABLED = None
SCHEDULE_CONCURRENT_REQUESTS = None
SCHEDULE_DOWNLOAD_DELAY = None
SCHEDULE_ADDITIONAL = '-d setting=CLOSESPIDER_TIMEOUT=60\r\n-d setting=CLOSESPIDER_PAGECOUNT=10\r\n-d arg1=val1'
SHOW_SCRAPYD_ITEMS = True
SHOW_JOBS_JOB_COLUMN = True
JOBS_FINISHED_JOBS_LIMIT = 0
JOBS_RELOAD_INTERVAL = 300
DAEMONSTATUS_REFRESH_INTERVAL = 10
SLACK_TOKEN = os.environ.get('SLACK_TOKEN', '')
SLACK_CHANNEL = 'general'
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
TELEGRAM_CHAT_ID = int(os.environ.get('TELEGRAM_CHAT_ID', 0))
EMAIL_SUBJECT = 'Email from #scrapydweb'
EMAIL_USERNAME = ''
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD', '')
EMAIL_SENDER = ''
EMAIL_RECIPIENTS = [
 EMAIL_SENDER]
SMTP_SERVER = ''
SMTP_PORT = 0
SMTP_OVER_SSL = False
SMTP_CONNECTION_TIMEOUT = 30
ENABLE_MONITOR = False
POLL_ROUND_INTERVAL = 300
POLL_REQUEST_INTERVAL = 10
ENABLE_SLACK_ALERT = False
ENABLE_TELEGRAM_ALERT = False
ENABLE_EMAIL_ALERT = False
ALERT_WORKING_DAYS = []
ALERT_WORKING_HOURS = []
ON_JOB_RUNNING_INTERVAL = 0
ON_JOB_FINISHED = False
LOG_CRITICAL_THRESHOLD = 0
LOG_CRITICAL_TRIGGER_STOP = False
LOG_CRITICAL_TRIGGER_FORCESTOP = False
LOG_ERROR_THRESHOLD = 0
LOG_ERROR_TRIGGER_STOP = False
LOG_ERROR_TRIGGER_FORCESTOP = False
LOG_WARNING_THRESHOLD = 0
LOG_WARNING_TRIGGER_STOP = False
LOG_WARNING_TRIGGER_FORCESTOP = False
LOG_REDIRECT_THRESHOLD = 0
LOG_REDIRECT_TRIGGER_STOP = False
LOG_REDIRECT_TRIGGER_FORCESTOP = False
LOG_RETRY_THRESHOLD = 0
LOG_RETRY_TRIGGER_STOP = False
LOG_RETRY_TRIGGER_FORCESTOP = False
LOG_IGNORE_THRESHOLD = 0
LOG_IGNORE_TRIGGER_STOP = False
LOG_IGNORE_TRIGGER_FORCESTOP = False
DEBUG = False
VERBOSE = False
DATA_PATH = os.environ.get('DATA_PATH', '')
DATABASE_URL = os.environ.get('DATABASE_URL', '')