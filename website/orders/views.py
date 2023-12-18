from django.shortcuts import render, redirect

from shop.cart import Cart
from .models import OrderItem
from .forms import OrderForm


def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            if cart:
                order = form.save()
                for item in cart:
                    if item['watch'].is_available:
                        OrderItem.objects.create(
                            order=order, product=item['watch'],
                            price=item['price'], quantity=item['quantity']
                        )
                        item['watch'].is_available = False
                        item['watch'].save()
                cart.clear()
                return render(
                    request, 'watches/confirmation.html', {'order': order}
                )
            else:
                return redirect('shop:cart_detail')
    else:
        form = OrderForm()
    context = {'cart': cart, 'form': form}
    return render(request, 'watches/checkout.html', context)
