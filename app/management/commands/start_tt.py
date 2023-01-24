

from django.utils import timezone
from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        schedule, created = IntervalSchedule.objects.get_or_create(every=30, period=IntervalSchedule.SECONDS, )
        PeriodicTask.objects.create(
                                    name='repeater',
                                    task='repeat_tasks_make',
                                    interval=schedule,
                                    start_time=timezone.now(),
        )

