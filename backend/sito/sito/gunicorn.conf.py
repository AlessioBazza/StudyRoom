import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'eventlet'
accesslog = '/tmp/gunicorn.access.log'
errorlog = '/tmp/gunicorn.error.log'
pidfile = '/tmp/gunicorn.pid'
