# Generated by Django 4.2.11 on 2024-04-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='static/postCovers',
            field=models.ImageField(null=True, upload_to='blog/static/postCovers'),
        ),
    ]
