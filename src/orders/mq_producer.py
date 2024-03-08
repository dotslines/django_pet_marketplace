import json

import pika

from django.conf import settings


class AMQPProducerOrderCreatedReport:
    EXCHANGE = settings.RMQ_ORDER_EXCHANGE
    ROUTING_KEY = settings.RMQ_ORDER_CREATED_ROUTING_KEY

    def __init__(self) -> None:
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(settings.RMQ_HOST, heartbeat=600, blocked_connection_timeout=300)
        )
        self.channel = self.connection.channel()

    def publish(self, method: str, body: str) -> None:
        properties = pika.BasicProperties(method)
        self.channel.basic_publish(
            exchange=self.EXCHANGE, routing_key=self.ROUTING_KEY, body=json.dumps(body), properties=properties
        )
