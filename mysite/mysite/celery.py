from __future__ import absolute_import, unicode_literals

import os
import paho.mqtt.client as mqtt
from celery import Celery, shared_task
import time

#'셀러리' 프로그램을 위해 기본 장고 설정파일을 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

app = Celery('mysite', backend='amqp')
            #  include=['mysite.tasks']) 
# include -> worker가 시작되었을 때 포함될 모듈의 목록입니다. worker가 task를 찾도록 하기 위해 여기에 작성한 task를 등록할 필요
#  broker='amqp://',
#  backend='amqp://',   ---------    task의 상태와 결과를 추적하는데 이용, 기본적으로 결과 비활성화, @task(ignore_result=True) 옵션 설정 통해서도 비활성 가능

app.config_from_object('django.conf:settings', namespace='CELERY')
#namespace='CELERY'는 모든 셀러리 관련 설정 키는 'CELERY_' 라는 접두어를 가져야 한다고 알려줌
# name space 가 대문자로 표시된 것 : 셀러리 설정 옵션이 반드시 대문자로 지정되어야 하며, CELERY_로 시작해야 한다는 뜻 (필수 아님, 그러나 권장)


#등록된 장고 앱 설정에서 task를 자동으로 탐색
app.autodiscover_tasks()  

client = mqtt.Client()
client.username_pw_set("agent","agent")
client.connect("127.0.0.1")
client.loop_start()

#task 인스턴스를 참조해 자신의 request 정보를 쉽게 뽑아낼 수 있다
@app.task
def debug_task(self):
    print(f'Request: {self.request!r}')


# @app.task
# def calc_add(x, y):
#     client.loop_start()
    
#     print("result1:", x+y)
#     for i in range(30):
#         client.publish('test', ">> {} pub_test".format(i), 1)
#     print("end")


