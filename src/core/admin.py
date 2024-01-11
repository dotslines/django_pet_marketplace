from django.contrib import admin

from utils.admin import SingletonAdmin

from .models import GeneralData


@admin.register(GeneralData)
class GeneralDataAdmin(SingletonAdmin):
    change_form_template = 'admin/change_form_no_deletion.html'
