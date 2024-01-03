from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel


class Promo(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    slug = models.SlugField(_("Slug"), max_length=100)
    code = models.CharField(_("PromoCode"), max_length=30)
    owner = models.ForeignKey(
        "accounts.User", verbose_name=_("Owner of the promotion"), on_delete=models.CASCADE, related_name="promos"
    )

    class Meta:
        verbose_name = _("Promo")
        verbose_name_plural = _("Promos")
        ordering = ("name",)

    def __str__(self) -> str:
        return f"Promo: {self.name}"
