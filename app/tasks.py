from celery import shared_task
from django_celery_beat.models import PeriodicTask

from models import User_Task, File_Statuses


@shared_task(name="repeat_order_make")
def repeat_order_make(order_id):
  u_tasks = User_Task.objects.all().filter(file_status=File_Statuses.NEW)
  for one_tsk in u_tasks:
    print('Статус получен!')
    task = PeriodicTask.objects.get(name='Repeat order {}'.format(order_id))
    task.enabled = False
    task.save()
  else:
    # Необходимая логика при повторной отправке заказа
    print('Я должна повторно оформлять заказ каждые 10 секунд')


# from django.conf import settings
# from django.core.mail import send_mail
# from celery import shared_task
# import subprocess
#
# from app.models import User_Task, File_Statuses
#
#
# def get_flake(filename):
#     l_form = "--format='" + '" row "%(row)d:" "[%(code)s]" "%(text)s' + "'"
#     cmd2 = f"flake8 .{filename} {l_form}"
#     p = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)
#     result = p.communicate()[0]
#
#     return result
#
#
# @shared_task
# def send_on_email(filename, user_email, file_name, pk):
#     obj = User_Task.objects.get(pk=pk)
#     obj.file_status = File_Statuses.IN_WORK
#     obj.save()
#
#     is_flake = get_flake(filename)
#     msg_text = 'ошибок не найдено'
#     if is_flake:
#         msg_text = 'есть ошибки'
#     is_mail = send_mail("проверка задач",
#                         'файл ' + file_name + ' проверен, ' + msg_text,
#                         settings.EMAIL_HOST_USER,
#                         [user_email],
#                         )
#     obj.file_status = File_Statuses.VERIFIED
#     obj.save()
#
#     log_file = '.' + settings.MEDIA_URL + 'file_logs/' + str(pk)
#     with open(log_file, 'a', encoding='UTF-8') as f:
#         f.write(msg_text + '\n')
#         f.write(str(is_flake.decode("utf-8")))
#         if is_mail:
#             f.write("\nотправлена информация по почте\n")
#         else:
#             f.write("\nне удалось отправить информацию по почте\n")