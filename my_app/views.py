from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from .tasks import add

from .models import *

from mysite.celery import calc_add

def queryset_to_dict(queryset):
    ret = []
    for i in queryset:
        ret.append(i)

    return ret

def index(request):
   
    print("\nSTART------------------------------------")
    #add.delay(3, 10)
    calc_add.delay(0, 0)
    calc_add.delay(1, 1)
    calc_add.delay(2, 2)
    calc_add.delay(3, 3)
    print("END--------------------------------------\n")
    
    return HttpResponse("야호")
