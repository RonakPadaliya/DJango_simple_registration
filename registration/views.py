from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .models import User

from django.conf import settings
from django.core.mail import send_mail
from twilio.rest import Client
import random
from django.contrib import messages

def registration(request): 
    return render(request,'registration.html')

def verify(request):

    def generate():
        otp=random.randint(1000,9999)
        request.session['otp']=otp
        return otp

    if request.method == 'POST':
        request.session['name']=request.POST.get('name')
        request.session['email']=request.POST.get('email')
        request.session['mob']=request.POST.get('mob')

        account_sid = 'AC19f4e085897fc8da018843137183b9de'
        auth_token = 'ef40474c8eb5db3449e5bb2635324f8d'

        client = Client(account_sid, auth_token)
        key=generate()
        client.api.account.messages.create(
            to="+91" + request.POST.get('mob'),
            from_="+16314964114",
            body=key)
        return render(request,'verify.html')
    return redirect("/registration")

def create(request):
    if request.method == 'POST':
        otp=int(request.POST.get('otp'))
        if otp == request.session.get('otp'):
            name=request.session.get('name')
            email=request.session.get('email')
            mob=request.session.get('mob')
            u=User(name=name,email=email,mob=mob)
            u.save()
            subject = 'Registration Status'
            message = f'Hi {name}, thank you for registering.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request,"Registration Successfully !")
        else:
            messages.error(request,"OTP is incorrenct !")

        del request.session['name']
        del request.session['email']
        del request.session['mob']
        del request.session['otp']
    return redirect("/registration")