from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from .models import Farmacia

class IndexView(TemplateView):
	template_name = 'farma/index.html'


class FarmaciaList(ListView):
      model = Farmacia


      