# Generated by Django 4.1.5 on 2023-01-22 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_user_task_log_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_task',
            name='log_file',
        ),
    ]
