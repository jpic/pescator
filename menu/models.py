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
from adminsortable.models import Sortable, SortableForeignKey
from redactor.fields import RedactorField


@python_2_unicode_compatible
class Category(Sortable):
    name = models.CharField(max_length=100, verbose_name=_('title'))
    slug = models.CharField(max_length=200)

    class Meta(Sortable.Meta):
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Dish(Sortable):
    category = SortableForeignKey(Category, verbose_name=_('category'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    slug = models.CharField(max_length=200)
    description = RedactorField(blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='menu/dish')
    sale_price_euros = models.DecimalField(decimal_places=2, max_digits=8,
        verbose_name='price')

    class Meta(Sortable.Meta):
        verbose_name = _('dish')
        verbose_name_plural = _('dishes')

    def __str__(self):
        return self.name
