from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline
from modeltranslation.admin import TranslationAdmin

from .models import Category, Dish


class DishInline(SortableTabularInline):
    model = Dish
    exclude = ('slug', 'slug_fr', 'slug_en', 'name', 'description',
            'description_fr', 'description_en', 'image')


class CategoryAdmin(TranslationAdmin, SortableAdmin):
    inlines = (DishInline,)
    exclude = ('slug',)
admin.site.register(Category, CategoryAdmin)


class DishAdmin(TranslationAdmin):
    exclude = ('slug',)
    list_display = ('pk', 'name_fr', 'name_en', 'description_fr', 'description_en')
    list_editable = ('name_fr', 'name_en', 'description_fr', 'description_en')
    list_display_links = ('pk',)
admin.site.register(Dish, DishAdmin)
