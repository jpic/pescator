from __future__ import unicode_literals

from django.db.models import signals
from django.core.urlresolvers import reverse
from django.utils.translation import activate, get_language
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from sortedm2m.fields import SortedManyToManyField
from redactor.fields import RedactorField


@python_2_unicode_compatible
class Block(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('block title'))
    body = RedactorField(verbose_name=_('text'), null=True, blank=True)
    template = models.CharField(max_length=50, default='pages/block.html')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Photo(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('photo title'))
    image = models.ImageField(upload_to='pages/photo')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Page(models.Model):
    CAROUSEL_ABOVE_CONTENTS = 0
    CAROUSEL_UNDER_CONTENTS = 1
    CAROUSEL_ABOVE_SIDEBAR = 2
    CAROUSEL_UNDER_SIDEBAR = 3
    CAROUSEL_CHOICES = (
        (CAROUSEL_ABOVE_CONTENTS, _('Above body')),
        (CAROUSEL_UNDER_CONTENTS, _('Under body')),
        (CAROUSEL_ABOVE_SIDEBAR, _('Above sidebar')),
        (CAROUSEL_UNDER_SIDEBAR, _('Under sidebar')),
    )

    name = models.CharField(max_length=200, verbose_name=_('page title'))
    menu_name = models.CharField(max_length=100,
        verbose_name=_('menu title'), null=True, blank=True)
    menu_order = models.IntegerField(verbose_name=_('order in menu'),
        help_text=_('if this page should be first in the menu, set to 1. If'
            ' it should be second then set to 2 and so on. Leave empty if'
            ' there should be no menu link for this page.'),
        null=True, blank=True)
    footer_order = models.IntegerField(verbose_name=_('order in footer'),
        help_text=_('if this page should be first in the footer linkes, set'
            ' to 1. If it should be second then set to 2 and so on. Leave'
            ' empty if it should not appear in the footer at all.'),
        null=True, blank=True)
    slug = models.CharField(max_length=200, null=True, blank=True)
    body = RedactorField(verbose_name=_('text'))
    header_image = models.ImageField(upload_to='pages/page',
        null=True, blank=True,
        verbose_name=_('photo to use in the page header'))
    blocks = SortedManyToManyField(Block, blank=True)
    photos = SortedManyToManyField(Photo, blank=True)
    carousel_position = models.IntegerField(
        choices=CAROUSEL_CHOICES,
        default=CAROUSEL_ABOVE_CONTENTS)
    template = models.CharField(max_length=50,
        default='pages/page_detail.html')

    class Meta:
        ordering = ('menu_order', 'name',)

    def __str__(self):
        return self.name

    def make_absolute_url(self):
        return reverse('pages_page_detail', args=(self.slug,))

    def get_absolute_url(self):
        lang = get_language()

        if getattr(self, 'slug_%s' % lang, False):
            return self.make_absolute_url()
        else:
            for lang_code, lang_verbose in settings.LANGUAGES:
                if getattr(self, 'slug_%s' % lang_code, False):
                    activate(lang_code)
                    url = self.make_absolute_url()
                    activate(lang)
                    return url


def autoslug_translated(sender, instance, **kwargs):
    """ Automatically create a unique translated slug """
    qs = sender.objects.all()
    if instance.pk:
        qs = qs.exclude(pk=instance.pk)

    actual_lang = get_language()
    field_names = sender._meta.get_all_field_names()
    for lang_code, lang_verbose in settings.LANGUAGES:
        if 'slug_%s' % lang_code not in field_names:
            continue

        activate(lang_code)
        name = unicode(instance)

        if not name:
            continue

        counter = 1
        slug = slugify(name)

        while qs.filter(**{'slug_%s' % lang_code: slug}).count():
            slug = slugify(name) + unicode(counter)
            counter += 1

        setattr(instance, 'slug_%s' % lang_code, slug)

    activate(actual_lang)
signals.pre_save.connect(autoslug_translated)


def automenu_name(sender, instance, **kwargs):
    actual_lang = get_language()

    for lang_code, lang_verbose in settings.LANGUAGES:
        if not instance.menu_name:
            setattr(instance, 'menu_name_%s' % lang_code, instance.name)

    activate(actual_lang)
signals.pre_save.connect(automenu_name, sender=Page)
