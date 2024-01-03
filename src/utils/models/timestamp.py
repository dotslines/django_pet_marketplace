from django.db import models
from django.utils.translation import gettext_lazy as _


class DateTimeStampMixin(models.Model):
    """
    Date and Time stamp mixin,
    provides with 'created' and 'updated' fields.
    """

    created = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("Updated at"), auto_now=True)

    class Meta:
        abstract = True
