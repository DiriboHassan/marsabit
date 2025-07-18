from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactSubmission
from django.contrib import messages
from marsabitweb.models import Copyright, Hero, HeroOthers, Introduction

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            ContactSubmission.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            messages.success(request, 'Your message has been saved!')
            return redirect('contact:contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    copyrights = Copyright.objects.all()
    heros = Hero.objects.all()
    intros = Introduction.objects.all()


    return render(request, 'contact.html', {'form': form, 'copyrights':copyrights, 'heros':heros, 'intros':intros})