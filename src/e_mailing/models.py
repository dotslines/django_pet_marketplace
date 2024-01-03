from django.core.mail import EmailMessage
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import DateTimeStampMixin


class Email(DateTimeStampMixin):
    class STATUSES(models.TextChoices):
        created = "created", _("Email is created")
        processing = "processing", _("Sending process")
        sent = "sent", _("Email is sent")
        failed = "failed", _("Email is not sent")

    from_email = models.EmailField(_("Sender"))
    to_email = models.EmailField(_("Recipient"))
    reply_to = models.EmailField(_("Replied to"))
    subject = models.CharField(_("Subject"), max_length=250)
    body = models.TextField(_("Email body"))
    sent_timestamp = models.DateTimeField(_("Sent date and time"), null=True, blank=True)
    status = models.CharField(_("Status"), choices=STATUSES.choices, default=STATUSES.created, max_length=20)

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")
        ordering = "from_email", "to_email"

    def __str__(self) -> str:
        return f"Email from {self.from_email} to {self.to_email}: {self.status}"

    def send(self) -> bool:
        try:
            message = EmailMessage()
            message.from_email = self.from_email
            message.to = [self.to_email]
            message.reply_to = [self.reply_to]
            message.subject = self.subject
            message.body = self.body
            self.status = self.STATUSES.processing
            self.save()
            status = bool(message.send(fail_silently=False))
        except Exception as ex:  # noqa: F841
            # here ex should be captured
            status = False

        if status:
            self.status = self.STATUSES.sent
        else:
            self.status = self.STATUSES.failed

        self.save()
        return status
