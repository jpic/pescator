from modeltranslation.translator import translator, TranslationOptions

from .models import Page, Block, Photo


class BlockTranslation(TranslationOptions):
    fields = ('name', 'body')
translator.register(Block, BlockTranslation)


class PhotoTranslation(TranslationOptions):
    fields = ('name',)
translator.register(Photo, PhotoTranslation)


class PageTranslation(TranslationOptions):
    fields = ('name', 'slug', 'body', 'menu_name')
translator.register(Page, PageTranslation)
