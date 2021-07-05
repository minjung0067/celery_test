from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .tasks import add, send_email_task

from time import sleep
from .models import *

# from mysite.celery import calc_add

def queryset_to_dict(queryset):
    ret = []
    for i in queryset:
        ret.append(i)

    return ret

def index(request):
   
    # print("\nST------------------------------------")
    # result1 = add.delay(0, 0)
    # result2 = add.delay(1, 1)
    # sleep(10)
    # result3 = add.delay(6, 6)
    # result4 = add.delay(10, 10)
    # print("END--------------------------------------\n")
    print("\nSTART------------------------------------")
    send_email_task.delay()
    print("END--------------------------------------\n")

    return HttpResponse("이메일 보냈다요!!")
