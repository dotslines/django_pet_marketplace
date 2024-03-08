import json

from django.conf import settings

from e_mailing.tasks import send_email
from orders.models import Order

from ..mq_producer import AMQPProducerOrderCreatedReport

report_producer = AMQPProducerOrderCreatedReport()


class OrderPostCreation:
    def __init__(self, order: Order) -> None:
        self.order = order
        self.send_mail()
        self.send_report()

    def send_report(self) -> None:
        order_data = json.dumps(
            {
                "order_id": str(self.order.id),
                "order_owner": str(self.order.owner.id),
                "order_products": self.order.products,
            }
        )
        report_producer.publish("order_created_method", order_data)

    def send_mail(self) -> None:
        owner = self.order.owner
        if owner:
            to_email = owner.email
        else:
            to_email = ""
        send_email.delay(
            subject=f"Order {self.order.id} created.",
            body=f"The order ID is {self.order.id}.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to_email=[to_email],
            reply_to="",
        )
