from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel


class Gallery(BaseModel):
    """
    Gallery, collection of images.
    """

    name = models.CharField(_("Gallery name"), max_length=255)
    slug = models.SlugField(_("Gallery slug"), max_length=255)

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Galleries")
        ordering = ("name",)
        db_table = "products_gallery"

    def __str__(self) -> str:
        return f"{self.name}"
