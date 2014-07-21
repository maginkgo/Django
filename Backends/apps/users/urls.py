from django.conf.urls import patterns, include, url
from .views import ExtraDataView

urlpatterns = patterns('',
	#Ruta a la funcion de logout
	url(r'^log-out/$', 'apps.users.views.LogOut', name='logout'),
	url(r'^extra-data/$', ExtraDataView.as_view(), name='extra-data'),

)
