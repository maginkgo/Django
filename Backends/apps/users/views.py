from django.shortcuts import render, redirect 
from django.contrib.auth import logout
from django.views.generic import View
from django.core.mail import EmailMessage

from .forms import ExtraDataForm

class ExtraDataView(View):

	def get(self, request, *args, **kargs):
		if request.user.status:
			return redirect('/')
		else:
			return render(request,'users/extra-data.html')

	def post(self,request, *args, **kargs):
		form = ExtraDataForm(request.POST)
		if form.is_valid():
			request.user.username = request.POST['username']
			request.user.email = request.POST['email']
			request.user.status = True 
			request.user.save()
			send_email(request)
			return redirect('/')
		else:
			error_username = form['username'].errors.as_text()
			error_email = form['email'].errors.as_text() 
			ctx = {'error_username': error_username, 'error_email': error_email}
			return render(request, 'users/extra-data.html', ctx)

def LogOut(request):
	logout(request)	
	return redirect('/')

def send_email(request):
	msg = EmailMessage(subject='Bienvenida',
						from_email = 'Maginkgo <maginkgo@gmail.com>',
						to = [request.user.email])

	msg.template_name = "welcome"

	msg.template_content = {
		'std_content00' : '<h1>Hola %s Bienvenido a mi Web</h1>' % request.user
	}
	
	msg.send()

	







