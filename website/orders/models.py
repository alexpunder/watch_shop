from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from shop.models import Watch


class Order(models.Model):
    created = models.DateTimeField(
        'Дата размещения',
        auto_now_add=True
    )
    first_name = models.CharField(
        'Имя',
        max_length=50
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=50
    )
    phone_number = PhoneNumberField(
        'Номер телефона'
    )
    email = models.EmailField(
        'Почта',
        max_length=255
    )
    adress = models.CharField(
        'Адрес',
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        date = self.created.strftime('%d.%m.%Y %H:%M')
        return f'Заказ номер {self.id} от {date}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Watch,
        on_delete=models.CASCADE,
        related_name='order_items'
    )
    price = models.PositiveIntegerField(
        'Цена'
    )
    quantity = models.PositiveSmallIntegerField(
        'Количество'
    )

    class Meta:
        ordering = ['product__id']
        verbose_name = 'Часы в заказе'
        verbose_name_plural = 'Часы в заказе'

    def __str__(self):
        return f'Часы в заказе #{self.id}'

    def get_cost(self):
        return self.price * self.quantity
