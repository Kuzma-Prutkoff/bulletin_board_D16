from django.apps import AppConfig


class BuBoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bu_bo_app'

    def ready(self):
        from . import signals
