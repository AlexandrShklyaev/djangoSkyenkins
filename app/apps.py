from django.apps import AppConfig as app_conf


class AppConfig(app_conf):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
