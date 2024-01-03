from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel


class Brand(BaseModel):
    """
    Brand model
    """

    name = models.CharField(_("Brand name"), max_length=255)
    slug = models.SlugField(_("Brand slug"), max_length=255)

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        ordering = ("name",)
        db_table = "products_brand"

    def __str__(self) -> str:
        return f"{self.name}"
