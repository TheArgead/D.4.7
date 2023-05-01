from django.apps import AppConfig


class SimpleappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsportal'

    def ready(self):
        from . import signals  # выполнение модуля -> регистрация сигналов