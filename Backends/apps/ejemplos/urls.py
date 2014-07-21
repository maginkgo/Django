from django.conf.urls import patterns, include, url
from .views import IndexView, EjemploView

urlpatterns = patterns('',
	url(r'^ejemplos/$', IndexView.as_view()),
	url(r'^ejemplos/(?P<ej>[a-z]+)/$', EjemploView.as_view()),
)

