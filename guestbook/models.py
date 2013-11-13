from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Entry(models.Model):
    STATUS_NEW = 0
    STATUS_VALIDATED = 1

    STATUS_CHOICES = (
        (STATUS_NEW, _('New')),
        (STATUS_VALIDATED, _('Validated')),
    )

    status = models.IntegerField(choices=STATUS_CHOICES, default=STATUS_NEW)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    creation_datetime = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ('-creation_datetime',)
        verbose_name_plural = _('entries')

    def __str__(self):
        return self.name
