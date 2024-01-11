from django.contrib import admin
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse


class SingletonAdmin(admin.ModelAdmin):
    def changelist_view(self, request: HttpRequest, extra_context: None | dict = None) -> HttpResponse:
        """
        Open change page instead of list view page.
        Needed for singleton models.
        """
        if self.model.objects.all().count() == 1:
            obj = self.model.objects.all()[0]
            return HttpResponseRedirect(
                reverse(
                    "admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.model_name), args=(obj.id,)
                )
            )
        return super().changelist_view(request=request, extra_context=extra_context)
