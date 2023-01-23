from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ("id","user_name", "email",)
    list_filter = ()
    search_fields = ('user_name','email',)
    ordering = ('email',)
    filter_horizontal = ()
