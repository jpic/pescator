from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Entry
from .forms import EntryCreateForm


class EntryCreateView(generic.CreateView):
    model = Entry
    form_class = EntryCreateForm
    success_url = reverse_lazy('guestbook_entry_posted')


class EntryListView(generic.ListView):
    queryset = Entry.objects.filter(status=Entry.STATUS_VALIDATED)

    def get_context_data(self, **kwargs):
        c = super(EntryListView, self).get_context_data(**kwargs)
        c['form'] = EntryCreateForm()
        return c
