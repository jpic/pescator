from django.conf.urls import patterns, url
from django.views import generic

import views

urlpatterns = patterns('',
    url(r'^$', views.EntryListView.as_view(),
        name='guestbook_entry_list'),
    url(r'post/$', views.EntryCreateView.as_view(),
        name='guestbook_entry_create'),
    url(r'posted/$', generic.TemplateView.as_view(
        template_name='guestbook/posted.html'),
        name='guestbook_entry_posted'),
)
