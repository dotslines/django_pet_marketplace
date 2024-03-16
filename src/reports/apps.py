from django.apps import AppConfig
from django.conf import settings

from .mq_consumer import AMQPOrderCreatedConsumer


class ReportsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reports"

    def ready(self):
        if not settings.IS_TESTING:
            consumer = AMQPOrderCreatedConsumer()
            consumer.daemon = True
            consumer.start()
