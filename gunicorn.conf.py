workers = 2
worker_class = 'eventlet'
accesslog = 'logs/gunicorn_access.log'
access_log_format = '%(h)s %({X-Real-IP}i)s %(D)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s'
errorlog = 'logs/gunicorn_error.log'