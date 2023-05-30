from django.contrib import admin

from .models import *
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'field_organisation_name', 'field_text_appeal', 'stat', 'emp', 'time_create', 'field_number_phone', 'field_email', 'field_fio')
    list_display_links = ('id', 'field_organisation_name')
    search_fields = ('field_organisation_name', 'stat')
    list_filter = ('field_organisation_name', 'stat', 'time_create', 'emp')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('name', )




admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Employee, EmployeeAdmin)
