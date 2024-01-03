import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from utils.models import BaseModel


class Order(BaseModel):
    id = models.UUIDField(_("Primary key/ID"), primary_key=True, default=uuid.uuid4, max_length=50, unique=True)
    owner = models.ForeignKey(
        User, verbose_name=_("Buyer"), related_name="orders", on_delete=models.SET_NULL, blank=True, null=True
    )
    products = models.JSONField(_("Ordered products"))
    promos = models.JSONField(_("Promos used in order"), blank=True, null=True)

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ("id",)

    def __str__(self) -> str:
        return f"order ID: {self.id}"
