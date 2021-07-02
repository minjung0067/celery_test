from celery import Celery

app = Celery('test', broker='pyamqp://guest:guest@localhost//')

@app.task
def add(x, y):
    return x + y
