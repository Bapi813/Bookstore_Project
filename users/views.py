# users/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
#from django.core.mail import send_mail
from django.core.mail import  send_mail
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
    def index(request):
        if request.method == 'POST':
            send_mail(
            #subject
             'Hello!',
             #Message Body
            'Here is the message',
            #from
            'mailgun@brige.com',
            #list, two email
            ['bapimahalik51@hototonmail.com'],
            fail_silently=False,
            )
