from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Watch


PRODUCTS_ON_PAGE = 2


def watch_list(request):
    template_name = 'watches/watch_list.html'
    watches = Watch.objects.filter(
        is_published=True, is_available=True
    )
    paginator = Paginator(watches, PRODUCTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template_name, context)


def watch_detail(request, pk):
    template_name = 'watches/watch_details.html'
    product = get_object_or_404(Watch, pk=pk)
    context = {'product': product}
    return render(request, template_name, context)
