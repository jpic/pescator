from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from pages.models import Page


def menu(request):
    menu = []

    for page in Page.objects.all():
        menu.append({
            'title': page.menu_name,
            'url': page.get_absolute_url(),
        })

    menu.append({
        'title': _('Guestbook'),
        'url': reverse('guestbook_entry_list'),
    })

    return {'menu': menu}
