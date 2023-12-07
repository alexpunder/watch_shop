from django.shortcuts import render
from django.views.generic import TemplateView


def page_forbidden(request, exception):
    return render(request, 'util_pages/403.html', status=403)


def page_not_found(request, exception):
    return render(request, 'util_pages/404.html', status=404)


def server_error(request):
    return render(
        request, 'util_pages/500.html', status=500)


class About(TemplateView):
    template_name = 'util_pages/about.html'


class Contacts(TemplateView):
    template_name = 'util_pages/contacts.html'


class Confidential(TemplateView):
    template_name = 'util_pages/confidential.html'


class Terms(TemplateView):
    template_name = 'util_pages/terms.html'


class Questions(TemplateView):
    template_name = 'util_pages/questions.html'
