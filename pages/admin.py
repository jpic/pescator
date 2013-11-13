from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from modeltranslation.admin import TranslationAdmin

from .models import Block, Photo, Page


admin.site.register(Photo, TranslationAdmin)


class BlockAdmin(TranslationAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'body'),
        }),
        (_('Advanced'), {
            'fields': ('template',),
        }),
    )
admin.site.register(Block, BlockAdmin)


class PageAdmin(TranslationAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'menu_name', 'body', 'photos', 'blocks'),
        }),
        (_('Advanced'), {
            'fields': ('carousel_position', 'template', 'slug',),
        }),
    )
admin.site.register(Page, PageAdmin)
