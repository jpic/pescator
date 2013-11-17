from django.views import generic
from django.utils.translation import activate, get_language
from django.conf import settings

from .models import Page


class PageDetailView(generic.DetailView):
    model = Page
    template_name_field = 'template'

    def get_context_data(self, **kwargs):
        c = super(PageDetailView, self).get_context_data(**kwargs)

        c['photos'] = self.object.photos.all()
        c['blocks'] = self.object.blocks.all()

        current_lang = get_language()
        c['other_languages'] = {}
        for code, lang in settings.LANGUAGES:
            activate(code)

            c['other_languages'][code] = {
                'url': self.object.get_absolute_url(),
                'language': lang,
                'name': unicode(self.object),
            }

        activate(current_lang)

        return c
