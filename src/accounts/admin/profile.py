from django.contrib import admin

from accounts.models import BuyerProfile
from accounts.models import SellerProfile


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(BuyerProfile)
class BuyerProfileAdmin(admin.ModelAdmin):
    pass
