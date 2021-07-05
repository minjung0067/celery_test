from django.db import models


class TestModel(models.Model):
    col1 = models.CharField(max_length=128)
    col2 = models.CharField(max_length=128)
    col3 = models.CharField(max_length=128)
    col4 = models.CharField(max_length=128)
    col5 = models.CharField(max_length=128)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
class Qna(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_send = models.BooleanField(default=False)

    class Meta:
        db_table = 'qna'