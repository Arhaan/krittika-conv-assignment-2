from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    title = models.CharField(default="Title", blank=False)
    author = models.OneToOneField(User)
    content = RichTextField()
    date_created = models.DateTimeField(auto_created=True)

