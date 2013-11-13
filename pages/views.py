from django.views import generic
from django import shortcuts

from .models import Page


class PageDetailView(generic.DetailView):
    model = Page
    template_name_field = 'template'

    def get_context_data(self, **kwargs):
        c = super(PageDetailView, self).get_context_data(**kwargs)

        c['photos'] = self.object.photos.all()
        c['blocks'] = self.object.blocks.all()

        return c
