from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Buyer
from accounts.models import Seller
from accounts.models import User


@admin.register(User)
class UserModelAdmin(UserAdmin):
    pass


@admin.register(Buyer)
class BuyerModelAdmin(UserAdmin):
    pass


@admin.register(Seller)
class SellerModelAdmin(UserAdmin):
    pass
