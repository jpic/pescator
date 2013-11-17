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
            'fields': ('name', 'menu_name', 'menu_order', 'footer_order',
                'header_image', 'body', 'photos', 'blocks'),
        }),
        (_('Advanced'), {
            'fields': ('carousel_position', 'template', 'slug',),
        }),
    )
    list_display = ('name', 'menu_name', 'menu_order', 'footer_order')
    list_editable = ('menu_order', 'footer_order')
admin.site.register(Page, PageAdmin)
