from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from website.settings import BASE_DIR


YES_OR_NO = (
    ('Нет', 'Нет'),
    ('Да', 'Да'),
)

PROCESSED = (
    ('Только поступил', 'Только поступил'),
    ('В работе', 'В работе'),
    ('Завершено', 'Завершено'),
    ('Клиент отказался', 'Клиент отказался'),
)


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
        verbose_name = 'Обращение с малой формы сайта'
        verbose_name_plural = 'Обращения с малой формы сайта'

    def __str__(self):
        return f'Обращение клиента от {self.pub_date}'


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
    year_of_purchase = models.DateField(
        'Год покупки',
        blank=True,
        null=True
    )
    packing_box = models.CharField(
        'Имеются ли упаковка и документы?',
        max_length=255,
        choices=YES_OR_NO,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Обращение с большой формы сайта'
        verbose_name_plural = 'Обращения с большой формы сайта'

    def __str__(self):
        return f'Обращение клиента от {self.pub_date}'
