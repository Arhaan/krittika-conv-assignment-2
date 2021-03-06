from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

CATEGORIES=(
        ("General", "General"),
        ("Night", "Night Sky"),
        ("Thoery", "Theoretical"),
    )
class Post(models.Model):
    

    title = models.CharField(default="Title", blank=False, max_length=1000) # Not allowing more than 1000 characters here
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, default="General")
    photo = models.ImageField(upload_to='img', default="default.jpg")


    

