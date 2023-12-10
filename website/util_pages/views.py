from django.shortcuts import render
from django.views.generic import TemplateView

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
            pass
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


class Questions(TemplateView):
    template_name = 'util_pages/questions.html'
