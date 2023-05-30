from django.contrib import admin

from .models import *
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'appeal', 'stat', 'emp', 'time_create')
    list_display_links = ('id', 'organization')
    search_fields = ('organization', 'stat')
    list_filter = ('organization', 'stat', 'time_create', 'emp')

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
