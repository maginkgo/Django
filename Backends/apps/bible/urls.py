from django.conf.urls import patterns, include, url
from .views import IndexView

urlpatterns = patterns('',
	url(r'^bible/$', IndexView.as_view()),
)
