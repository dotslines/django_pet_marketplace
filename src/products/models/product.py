from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import BaseModel


class Product(BaseModel):
    """
    Product model.
    """

    owner = models.ForeignKey(
        "accounts.User", verbose_name=_("Owner of product"), on_delete=models.CASCADE, related_name="products"
    )
    category = models.ForeignKey(
        "products.Category",
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    brand = models.ForeignKey(
        "products.Brand",
        verbose_name=_("Brand"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )
    gallery = models.ForeignKey(
        "products.Gallery",
        verbose_name=_("Gallery of images of a product"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="products",
    )

    name = models.CharField(_("Product name"), max_length=255)
    slug = models.SlugField(_("Product slug"), max_length=255)
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    sku = models.CharField(_("SKU"), max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("name",)
        db_table = "products_product"

    def __str__(self) -> str:
        return f"{self.name}"
