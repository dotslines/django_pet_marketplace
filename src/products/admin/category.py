from django.contrib import admin

from products.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "visible"
    list_editable = ("visible",)
    list_filter = "created", "updated"
    search_fields = "name", "slug"
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = "created", "updated"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "visible",
                    "name",
                    "slug",
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
