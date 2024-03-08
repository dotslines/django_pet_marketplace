from django.apps import AppConfig
from django.conf import settings

from .mq_consumer import OrderCreatedConsumer


class ReportsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reports"

    def ready(self):
        if not settings.IS_TESTING:
            consumer = OrderCreatedConsumer()
            consumer.daemon = True
            consumer.start()
