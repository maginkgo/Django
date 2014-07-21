from django.conf.urls import patterns, include, url
from .views import IndexView

urlpatterns = patterns('',
	url(r'^news/$', IndexView.as_view()),
)
