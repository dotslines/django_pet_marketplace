from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "sku", "price", "visible"
    list_editable = ("visible",)
    list_filter = "created", "updated"
    date_hierarchy = "created"
    search_fields = "name", "slug", "sku"
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = "created", "updated"
    list_select_related = "brand", "category", "owner"
    change_form_template = "admin/change_form.html"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "owner",
                    "visible",
                    "brand",
                    "category",
                    "name",
                    "slug",
                    "sku",
                    "price",
                    "gallery",
                )
            },
        ),
        (
            "DateTime Stamps",
            {
                "fields": (
                    "created",
                    "updated",
                )
            },
        ),
    )
