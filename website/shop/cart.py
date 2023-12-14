from django.conf import settings

from .models import Watch


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, watch, quantity=1, update_quantity=False):
        watch_id = str(watch.id)
        if watch_id not in self.cart:
            self.cart[watch_id] = {
                'quantity': 0, 'price': watch.price
            }
        if update_quantity:
            self.cart[watch_id]['quantity'] = quantity
        else:
            self.cart[watch_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, watch):
        watch_id = str(watch.id)
        if watch_id in self.cart:
            del self.cart[watch_id]
            self.save()

    def __iter__(self):
        for watch_id, item in self.cart.items():
            item['watch'] = Watch.objects.get(id=int(watch_id))
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            item['price'] * item['quantity'] for item in self.cart.values()
        )

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
