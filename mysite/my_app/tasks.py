from celery import Celery, shared_task
from time import sleep
from django.core.mail import send_mail
from celery_progress.backend import ProgressRecorder

app = Celery('mysite')

@app.task
def add(x, y):
    return x + y

@app.task
def send_email_task():
    # sleep(10)

    send_mail('Celery Task Worked!',
    '이걸 본다면. 셀러리 tast가 worked 했다는 거야 !!!',
    'minjung1694@gmail.com',
    ['wakax74999@nnacell.com'])

    return None

@shared_task(bind=True)
def go_to_sleep(self, duration):
    progress_recorder = ProgressRecorder(self)
    for i in range(5):
        sleep(duration)
        progress_recorder.set_progress(i + 1, 5, f'On iteration {i}')
    return ('대단해 !')

