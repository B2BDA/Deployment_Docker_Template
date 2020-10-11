## pip3 or pip install gevent
## paste this in terminal to use asyncio's multi threaded application so that it can handle multiple tasks
# gunicorn -b 0.0.0.0:8080 --worker-class gevent wsgi:app
