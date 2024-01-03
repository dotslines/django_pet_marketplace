from typing import Any, Dict

from django.core.mail import send_mail

from orders.models import Order


class OrderCreation:
    def __init__(self, validated_data: Dict[Any, Any]) -> None:
        self.order = validated_data

    def create(self) -> None | TypeError:
        try:
            Order.objects.create(**self.order)
            self.send_email()
        except TypeError as ex:
            return ex

    def send_email(self) -> None:
        send_mail(
            "Order created.",
            f"The order ID is {self.order['id']}.",
            "noreply@market.com",
            [f"{self.order['owner'].email}"],
            fail_silently=False,
        )
