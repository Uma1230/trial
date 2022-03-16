from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	date = models.DateTimeField(default=datetime.now())
	description = models.TextField(default=1)
	bgimg = models.CharField(max_length=200,default=1)