
from django.db import models
from denorm import *

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

