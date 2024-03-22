import logging
import logging.handlers
from logging.handlers import WatchedFileHandler
import os,sys
import multiprocessing

bind = '0.0.0.0:8000'
chdir = '/canteen'  
timeout = 60
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
worker_class =  "gevent"
loglevel = 'info'
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
accesslog = "/canteen/gunicorn.log"
errorlog = "/canteen/gunicorn_error.log"

cwd = os.getcwd()
sys.path.append(cwd)
