
from django.shortcuts import render
from django.views.generic import TemplateView, View

class IndexView(TemplateView):
	template_name = 'ejemplos/index.html'


class EjemploView(View):
	def get(self, request, ej):
		plantilla = 'ejemplos/%s.html' % (ej)
		return render(request, plantilla)



