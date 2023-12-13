from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

from website.settings import BASE_DIR
from website.constants import YES_OR_NO, PROCESSED


class Base(models.Model):
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    processed = models.CharField(
        'Обработан ли запрос?',
        max_length=255,
        default='Только поступил',
        choices=PROCESSED
    )
    phone_number = PhoneNumberField(
        'Номер телефона',
        default=''
    )
    description = models.CharField(
        'Описание',
        max_length=255,
        blank=True,
        null=True
    )
    image = models.ImageField(
        'Изображение',
        upload_to=(BASE_DIR / 'media'),
        blank=True,
        null=True
    )


class Message(Base):

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Малая форма'
        verbose_name_plural = 'Малая форма'

    def __str__(self):
        date = self.pub_date.strftime('%d.%m.%Y %H:%M')
        return f'Обращение клиента от {date}'


class ExtendMessage(Base):
    first_name = models.CharField(
        'Имя',
        max_length=30
    )
    email = models.EmailField(
        'Электронная почта',
        blank=True,
        null=True
    )
    watch_mark = models.CharField(
        'Марка часов',
        max_length=255,
    )
    watch_model = models.CharField(
        'Модель часов и/или референс',
        max_length=255,
        blank=True,
        null=True
    )
    year_of_purchase = models.SmallIntegerField(
        'Год покупки',
        blank=True,
        null=True,
        validators=[
            MinValueValidator(
                1900,
                message='Год не может быть меньше 1900-ого.'
            ),
            MaxValueValidator(
                timezone.now().year + 1,
                message='Год не может быть больше текущего.'
            )
        ]
    )
    packing_box = models.CharField(
        'Имеются ли упаковка и документы?',
        max_length=255,
        choices=YES_OR_NO,
        default='Нет',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Расширенная форма'
        verbose_name_plural = 'Расширенная форма'

    def __str__(self):
        date = self.pub_date.strftime('%d.%m.%Y %H:%M')
        return f'Обращение клиента от {date}'
