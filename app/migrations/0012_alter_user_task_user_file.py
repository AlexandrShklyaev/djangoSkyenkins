# Generated by Django 4.1.5 on 2023-01-24 13:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_user_task_author_alter_user_task_user_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_task',
            name='user_file',
            field=models.FileField(upload_to='userfiles/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['py'])], verbose_name='файл'),
        ),
    ]
