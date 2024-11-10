from onlyvents.models import Setting, Source, Collection, Filter
from django.contrib import admin

class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

class FilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Setting, SettingAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Filter, FilterAdmin)
