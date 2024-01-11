from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import Singleton


class GeneralData(Singleton):
    """
    General site settings, data.
    """

    email = models.EmailField(_("Marketplace's contact email address."), max_length=20, blank=True, null=True)
    phone = models.CharField(_("Marketplace's contact phone number."), max_length=20, blank=True, null=True)
    telegram = models.CharField(_("Marketplace's contact telegram link."), max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _("Marketplace general data, site settings")
        verbose_name_plural = _("Marketplace general data, site settings")
