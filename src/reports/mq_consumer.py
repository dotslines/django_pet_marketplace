import threading

import pika

from django.conf import settings


class AMQPAMQPOrderCreatedConsumer(threading.Thread):
    EXCHANGE = settings.RMQ_ORDER_EXCHANGE
    QUEUE_NAME = settings.RMQ_ORDER_CREATED_QUEUE
    ROUTING_KEY = settings.RMQ_ORDER_CREATED_ROUTING_KEY
    THREADS = 5

    def __init__(self):
        threading.Thread.__init__(self)
        parameters = pika.ConnectionParameters(host=settings.RMQ_HOST)
        connection = pika.BlockingConnection(parameters)
        self.prepare_channel(connection)

    def prepare_channel(self, connection: pika.BlockingConnection) -> None:
        self.channel = connection.channel()
        self.channel.exchange_declare(exchange=self.EXCHANGE, exchange_type="direct")
        result = self.channel.queue_declare(queue="", auto_delete=False, exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(queue=queue_name, exchange=self.EXCHANGE, routing_key=self.ROUTING_KEY)
        self.channel.basic_qos(prefetch_count=self.THREADS * 10)
        self.channel.basic_consume(queue=queue_name, on_message_callback=self.callback)

    def callback(self, channel, method, properties, body):
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def run(self):
        self.channel.start_consuming()
