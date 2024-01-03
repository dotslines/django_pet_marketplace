from django.contrib import admin

from .models import Promo


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = "id", "name", "owner", "code", "visible"
    list_editable = ("visible",)
    list_filter = "created", "updated"
    search_fields = "id", "name", "owner"
    readonly_fields = "id", "created", "updated"
    prepopulated_fields = {"slug": ("name",)}
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "visible",
                    "name",
                    "slug",
                    "owner",
                    "code",
                )
            },
        ),
        (
            "DateTime Stamps",
            {
                "fields": (
                    "created",
                    "updated",
                ),
                "classes": ("collapse",),
            },
        ),
    )
