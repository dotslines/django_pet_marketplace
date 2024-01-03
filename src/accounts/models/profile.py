from django.db import models
from django.utils.translation import gettext_lazy as _


class BuyerProfile(models.Model):
    buyer = models.OneToOneField(
        "accounts.Buyer", verbose_name=_("Buyer"), on_delete=models.CASCADE, related_name="buyer_profile"
    )

    class Meta:
        verbose_name = _("Buyer Profile")
        verbose_name_plural = _("Buyer Profiles")

    def __str__(self) -> str:
        return f"{self.buyer.username}'s profile"


class SellerProfile(models.Model):
    seller = models.OneToOneField(
        "accounts.Seller", verbose_name=_("Seller"), on_delete=models.CASCADE, related_name="seller_profile"
    )

    class Meta:
        verbose_name = _("Seller Profile")
        verbose_name_plural = _("Seller Profiles")

    def __str__(self) -> str:
        return f"{self.seller.username}'s profile"
