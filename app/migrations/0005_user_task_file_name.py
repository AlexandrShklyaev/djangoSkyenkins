# Generated by Django 4.1.5 on 2023-01-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user_task_created_user_task_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_task',
            name='file_name',
            field=models.CharField(default='file.py', max_length=50),
        ),
    ]
