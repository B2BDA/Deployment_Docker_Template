## pip3 or pip install gevent
## paste this in terminal to use asyncio's multi threaded application so that it can handle multiple tasks
# gunicorn -b 0.0.0.0:8080 --worker-class gevent wsgi:app
https://medium.com/@danieldng/use-gevent-when-your-gunicorn-worker-is-waiting-for-data-180efef96367
https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7
