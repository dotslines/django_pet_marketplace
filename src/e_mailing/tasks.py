from typing import List

from celery import shared_task

from .models import Email


@shared_task
def send_email(subject: str, body: str, from_email: str, to_email: List[str]) -> None:
    mail = Email()
    mail.from_email = from_email
    mail.to_email = to_email
    mail.reply_to = to_email
    mail.subject = subject
    mail.body = body
    mail.send()
