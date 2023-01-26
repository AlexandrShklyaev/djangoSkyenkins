import time

from django.db import connections, OperationalError
from django.utils import timezone
from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # подождем пока бд раскрутится, чтоб избежать глюков
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waititng 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
        # создадим периодическое выполнение задачи
        schedule, created = IntervalSchedule.objects.get_or_create(every=30, period=IntervalSchedule.SECONDS, )
        task = PeriodicTask.objects.get(name='repeater')
        if task:
            task.delete()
            self.stdout.write('Taks recreated...')
        PeriodicTask.objects.create(
            name='repeater',
            task='repeat_tasks_make',
            interval=schedule,
            start_time=timezone.now(),
        )
