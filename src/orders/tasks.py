from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta

from celery import shared_task

from django.conf import settings

from e_mailing.tasks import send_email

from .models import Order


def get_orders_count(last_day: date) -> int:
    gte = datetime.combine(date.today(), time.min) - timedelta(days=1)
    lte = datetime.combine(date.today(), time.max) - timedelta(days=1)
    lastday_orders_count = Order.objects.filter(created__gte=gte, created__lte=lte).count()
    return lastday_orders_count


@shared_task(ignore_result=True)
def send_amount_of_new_orders_to_manager() -> None:
    last_day = date.today() - timedelta(days=1)
    lastday_orders_count = get_orders_count(last_day)
    send_email.delay(
        subject=f"Orders per day: {last_day.year}/{last_day.month}/{last_day.day}.",
        body=f"The orders count for last day is {lastday_orders_count}.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_email=["change_this@temporary.com"],
    )
