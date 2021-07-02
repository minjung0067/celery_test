from __future__ import absolute_import, unicode_literals

#이 구문은 shared_task를 위해 장고가 시작될 때 app이 항상 임포트 되도록 하는 역할
#이렇게 하면 장고가 시작될 때 @shared_task 데코레이터가 사용할 앱을 자동으로 로드시켜 줌
from .celery import app as celery_app

__all__ = ('celery_app', )
