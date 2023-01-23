from django.contrib import admin
from app.models import User_Task


@admin.register(User_Task)
class UserTask(admin.ModelAdmin):
    list_display = ("author", "user_file", "file_status", "created", "modified",)
    list_filter = ()
    search_fields = ("author", "file_status", "created", "modified",)
    ordering = ('author',)
    filter_horizontal = ()
