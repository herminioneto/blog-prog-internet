# Generated by Django 4.2.11 on 2024-04-12 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_image_post_static_postcovers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='static/postCovers',
            new_name='image',
        ),
    ]