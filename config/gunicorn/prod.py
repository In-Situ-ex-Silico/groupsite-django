"""Gunicorn *production* config file"""


# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
# wsgi_app = "pythonsd.wsgi:application"
wsgi_app = "config.prod_wsgi:application"
# The granularity of Error log outputs
loglevel = "error"
# The number of worker processes for handling requests
workers = 4
# The socket to bind
bind = "0.0.0.0:8000"
# Restart workers when code changes (development only!)
reload = False
# Write access and error info to /var/log
# accesslog = errorlog = "/var/log/gunicorn/dev.log"
# accesslog = errorlog = "./runtime_files/prod.log"
# Redirect stdout/stderr to log file
capture_output = False
# PID file so you can easily fetch process ID
pidfile = "./runtime_files/prod.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = True
