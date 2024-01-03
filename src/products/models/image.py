from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel


class Image(BaseModel):
    """
    Image
    """

    gallery = models.ForeignKey(
        "products.Gallery", verbose_name=_("Gallery"), on_delete=models.CASCADE, related_name="images"
    )
    name = models.CharField(_("Image name"), max_length=255)
    slug = models.SlugField(_("Image slug"), max_length=255)
    image = models.ImageField(_("Image url"), upload_to="")
    title = models.CharField(_("Title attribute for image tag"), max_length=255)
    alt = models.CharField(_("Alt attribute for image tag"), max_length=255)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
        ordering = ("name",)
        db_table = "products_image"

    def __str__(self) -> str:
        return f"{self.name}"
