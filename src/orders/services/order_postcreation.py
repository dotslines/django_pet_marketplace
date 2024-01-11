from django.conf import settings

from e_mailing.tasks import send_email
from orders.models import Order


class OrderPostCreation:
    def __init__(self, order: Order) -> None:
        self.order = order
        self.send_mail()

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
        )
