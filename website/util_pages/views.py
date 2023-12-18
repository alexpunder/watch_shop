from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from main.bot_sending_messages import message
from .forms import ContactForm


def page_forbidden(request, exception):
    return render(request, 'util_pages/403.html', status=403)


def page_not_found(request, exception):
    return render(request, 'util_pages/404.html', status=404)


def server_error(request):
    return render(
        request, 'util_pages/500.html', status=500)


class About(TemplateView):
    template_name = 'util_pages/about.html'


def contacts(request):
    template_name = 'util_pages/contacts.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            text = form.cleaned_data['text']
            name = form.cleaned_data['name']
            message(phone, text, name=name)
            return redirect('main:popup_message')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


class Confidential(TemplateView):
    template_name = 'util_pages/confidential.html'


class Terms(TemplateView):
    template_name = 'util_pages/terms.html'


def questions(request):
    template_name = 'util_pages/questions.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            text = form.cleaned_data['text']
            name = form.cleaned_data['name']
            message(phone, text, name=name)
            return redirect('main:popup_message')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
