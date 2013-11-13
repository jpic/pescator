from django.contrib import admin

from .models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ('status', 'name', 'email', 'creation_datetime')
    list_filter = ('status', 'creation_datetime')
    list_display_links = ('name',)
    list_editable = ('status',)
admin.site.register(Entry, EntryAdmin)
