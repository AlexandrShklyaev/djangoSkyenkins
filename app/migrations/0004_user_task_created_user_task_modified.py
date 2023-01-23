# Generated by Django 4.1.5 on 2023-01-20 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_task_user_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_task',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_task',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]