from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('apps.home.urls')),
    url(r'^', include('apps.users.urls', namespace='users')),
    url(r'^', include('apps.farma.urls', namespace='farma')),
    url(r'^', include('apps.bible.urls', namespace='bible')),
    url(r'^', include('apps.ejemplos.urls', namespace='ejemplos')),
    url(r'^', include('apps.news.urls', namespace='news')),

    #PYTHON SOCIAL AUTH - URL provista por documentacion oficial
    url('', include('social.apps.django_app.urls', namespace='social')),

    #URL del ADMINISTRADOR, ya viene por default.
    url(r'^admin/', include(admin.site.urls)),
)
