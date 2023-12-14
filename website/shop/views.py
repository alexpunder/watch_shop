from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST


from .models import Watch
from .forms import AddToCart
from .cart import Cart


PRODUCTS_ON_PAGE = 2


def watch_list(request):
    template_name = 'watches/watch_list.html'
    watches = Watch.objects.filter(
        is_published=True, is_available=True
    )
    paginator = Paginator(watches, PRODUCTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cart_product_form = AddToCart()
    context = {
        'page_obj': page_obj,
        'cart_product_form': cart_product_form
    }
    return render(request, template_name, context)


def watch_detail(request, pk):
    template_name = 'watches/watch_details.html'
    product = get_object_or_404(Watch, pk=pk)
    cart_product_form = AddToCart()
    context = {
        'product': product, 'cart_product_form': cart_product_form
    }
    return render(request, template_name, context)


@require_POST
def cart_add(request, pk):
    cart = Cart(request)
    watch = get_object_or_404(Watch, pk=pk)
    form = AddToCart(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            watch=watch, update_quantity=cd['update']
        )
    return redirect('shop:cart_detail')


def cart_remove(request, pk):
    cart = Cart(request)
    watch = get_object_or_404(Watch, pk=pk)
    cart.remove(watch)
    return redirect('shop:cart_detail')


def cart_detail(request):
    template_name = 'watches/cart_detail.html'
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, template_name, context)
