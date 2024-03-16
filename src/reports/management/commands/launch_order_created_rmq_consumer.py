from django.core.management.base import BaseCommand

from reports.mq_consumer import AMQPAMQPOrderCreatedConsumer


class Command(BaseCommand):
    """
    The consumer call made using a Django command in order
    to make it possible to call it as a separate processsor
    from a cli or from a shell file.
    """

    help = "Launches a consumer for order_created message."

    def handle(self, *args, **options):
        consumer = AMQPAMQPOrderCreatedConsumer()
        consumer.start()
        self.stdout.write("Started Consumer Thread")
