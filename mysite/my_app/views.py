from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .tasks import add, send_email_task, go_to_sleep

from time import sleep
from .models import *

# from mysite.celery import calc_add

def queryset_to_dict(queryset):
    ret = []
    for i in queryset:
        ret.append(i)

    return ret

def main(request):
   
    # print("\nST------------------------------------")
    # result1 = add.delay(0, 0)
    # result2 = add.delay(1, 1) 
    # sleep(10)
    # result3 = add.delay(6, 6)
    # result4 = add.delay(10, 10)
    # print("END--------------------------------------\n")
    print("\nSTART------------------------------------")
    send_email_task.delay()
    #인증 필요
    print("END--------------------------------------\n")

    return HttpResponse("두근..두근")


def show_progress(request): 
    task = go_to_sleep.delay(2)
    return render(request, 'show_progress.html',  context={'task_id': task.task_id})
