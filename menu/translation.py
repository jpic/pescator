from modeltranslation.translator import translator, TranslationOptions

from .models import Category, Dish


class CategoryTranslation(TranslationOptions):
    fields = ('name', 'slug')
translator.register(Category, CategoryTranslation)


class DishTranslation(TranslationOptions):
    fields = ('name', 'slug', 'description')
translator.register(Dish, DishTranslation)
