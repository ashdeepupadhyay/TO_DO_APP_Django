from django.db import models 
from django.http import HttpResponse

# Create your models here.
class TODOModel(models.Model):
    date_pub = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1000)
