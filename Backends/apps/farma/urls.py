from django.conf.urls import patterns, include, url
from .views import IndexView, FarmaciaList


urlpatterns = patterns('',
	url(r'^farma/$', IndexView.as_view()),
	url(r'^farmacias/', FarmaciaList.as_view(), name='lista_farmacias'),
)
		
