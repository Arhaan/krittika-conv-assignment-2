# Generated by Django 4.0.4 on 2022-05-17 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='img'),
        ),
    ]
