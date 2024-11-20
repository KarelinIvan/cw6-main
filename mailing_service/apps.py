from django.apps import AppConfig


class MailingServiceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing_service"

    def ready(self):
        import os
        if os.getenv("RUN_MAIN", None) != "true":
            return
        from .scheduler import start
        start()
