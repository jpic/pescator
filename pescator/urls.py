from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
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
)

urlpatterns += i18n_patterns('',
    url(r'^guestbook/', include('guestbook.urls')),
    url(r'^', include('pages.urls')),
)

urlpatterns += patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
