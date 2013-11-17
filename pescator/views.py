from django.views import generic

from pages.models import Page


class HomeView(generic.RedirectView):
    def get_redirect_url(self, **kwargs):
        try:
            return Page.objects.all().order_by('pk')[0].get_absolute_url()
        except IndexError:
            return '/admin/'
