from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

import autocomplete_light
autocomplete_light.autodiscover()

import views

urlpatterns = patterns('',
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^guestbook/', include('guestbook.urls')),
    url(r'^', include('pages.urls')),
    url(r'^$', views.HomeView.as_view(), name='home'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
