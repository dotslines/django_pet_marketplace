from django.contrib import admin

from products.models import Gallery
from products.models import Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = "name", "slug", "visible"
    list_editable = ("visible",)
    list_filter = "created", "updated"
    search_fields = "name", "slug"
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = "created", "updated"
    inlines = (ImageInline,)
    change_form_template = "products/admin/change_form.html"
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
