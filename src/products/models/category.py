from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel


class Category(BaseModel):
    """
    Category model.
    """

    name = models.CharField(_("Category name"), max_length=255)
    slug = models.SlugField(_("Category slug"), max_length=255)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ("name",)
        db_table = "products_category"

    def __str__(self) -> str:
        return f"{self.name}"
