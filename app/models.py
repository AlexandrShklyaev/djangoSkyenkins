from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models


class File_Statuses:
    NEW = "new"
    RELOAD = "reload"
    IN_WORK = "in_work"
    VERIFIED = "verified"
    choices = (
        (NEW, NEW),
        (RELOAD, RELOAD),
        (IN_WORK, IN_WORK),
        (VERIFIED, VERIFIED),
    )


class User_Task(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    user_file = models.FileField(upload_to="userfiles/", verbose_name="",
                                 validators=[FileExtensionValidator(allowed_extensions=['py', ])])
    file_name = models.CharField(max_length=50, default='file.py')
    file_status = models.CharField(max_length=8, choices=File_Statuses.choices, default=File_Statuses.NEW)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    def delete(self, *args, **kwargs):
        storage, path = self.user_file.storage, self.user_file.path
        log_file = '.' + settings.MEDIA_URL + 'file_logs/' + str(self.pk)
        open(log_file, 'w').close()

        super().delete(*args, **kwargs)
        storage.delete(path)
