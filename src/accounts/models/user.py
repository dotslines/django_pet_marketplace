from typing import Any

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import BuyerManager
from accounts.managers import SellerManager


class User(AbstractUser):
    class Status(models.TextChoices):
        admin = "admin", _("Admin")
        seller = "seller", _("Seller")
        buyer = "buyer", _("Buyer")

    status = models.CharField(_("User status"), max_length=20, choices=Status.choices, default=Status.admin)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return f"{self.username or self.email}"


class Buyer(User):
    objects = BuyerManager()  # type: ignore

    class Meta:
        proxy = True

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.status = self.Status.buyer
        super().save(*args, **kwargs)


class Seller(User):
    objects = SellerManager()  # type: ignore

    class Meta:
        proxy = True

    def save(self, *args: Any, **kwargs: Any) -> None:
        self.status = self.Status.seller
        super().save(*args, **kwargs)
