# from typing import TYPE_CHECKING

from django.contrib.auth.models import UserManager
from django.db.models.query import QuerySet

# if TYPE_CHECKING:
#     from accounts.models import User


class BuyerManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status="buyer")


class SellerManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status="seller")
