from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(default="Title", blank=False, max_length=1000) # Not allowing more than 1000 characters here
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = RichTextField()
    date_created = models.DateTimeField(auto_created=True)

