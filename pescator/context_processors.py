from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from pages.models import Page


def menu(request):
    menu = []

    pages = Page.objects.exclude(menu_order=None).order_by('menu_order')
    for page in pages:
        menu.append({
            'name': page.menu_name,
            'title': page.name,
            'url': page.get_absolute_url(),
        })

    menu.append({
        'name': _('Guestbook'),
        'url': reverse('guestbook_entry_list'),
    })

    return {'menu': menu}


def footer(request):
    footer = []

    pages = Page.objects.exclude(footer_order=None).order_by('footer_order')
    for page in pages:
        footer.append({
            'name': page.menu_name,
            'title': page.name,
            'url': page.get_absolute_url(),
        })

    return {'footer': footer}
