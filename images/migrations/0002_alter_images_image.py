# Generated by Django 3.2.7 on 2021-09-06 12:58

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='posts/default.jpg', max_length=255, upload_to=images.models.user_directory_path),
        ),
    ]
