from django.db import models
from django.utils.translation import gettext_lazy as _


class VisibilityMixin(models.Model):
    """
    Provides an object with 'visible' status field.
    """

    visible = models.BooleanField(verbose_name=_("Visibility status"), default=True)

    class Meta:
        abstract = True
