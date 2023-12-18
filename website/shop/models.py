from django.db import models
from django.urls import reverse
from pytils.translit import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

from django_resized import ResizedImageField

from website.constants import MIN_PRICE, MAX_PRICE


class BaseForCategories(models.Model):
    name = models.CharField(
        'Название',
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text='Обязательное поле'
    )
    slug = models.SlugField(
        'Слаг',
        max_length=255,
        unique=True,
        blank=True,
        null=True,
        help_text='Формируется автоматически из верхней строки'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Watch(models.Model):
    is_published = models.BooleanField(
        'Опубликована ли запись?'
    )
    is_on_main = models.BooleanField(
        'Выводить на главной?'
    )
    is_available = models.BooleanField(
        'В наличии?'
    )
    condition = models.ForeignKey(
        'Condition',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Состояние'
    )
    brand = models.ForeignKey(
        'Brand',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Бренд'
    )
    name = models.CharField(
        'Название',
        max_length=255
    )
    description = models.TextField(
        'Описание',
        max_length=1000,
    )
    article = models.CharField(
        'Артикул',
        max_length=255
    )
    country = models.ForeignKey(
        'Country',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Страна производства'
    )
    mechanism = models.ForeignKey(
        'Mechanism',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Механизм'
    )
    water_resistance = models.ForeignKey(
        'WaterResistance',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Водозащита'
    )
    body_material = models.ForeignKey(
        'BodyMaterial',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Материал корпуса'
    )
    circlet = models.ForeignKey(
        'Circlet',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Материал браслета'
    )
    color = models.ForeignKey(
        'Color',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Цвет'
    )
    case_shape = models.ForeignKey(
        'CaseShape',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Форма корпуса'
    )
    gender = models.ForeignKey(
        'Gender',
        max_length=255,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Пол'
    )
    price = models.PositiveIntegerField(
        'Цена',
        validators=[
            MinValueValidator(
                MIN_PRICE, message=f'Цена не может быть меньше {MIN_PRICE}'
            ),
            MaxValueValidator(
                MAX_PRICE, message=f'Цена не может быть больше {MAX_PRICE}'
            )
        ]
    )

    class Meta:
        ordering = ['is_available']
        verbose_name = 'Часы'
        verbose_name_plural = 'Часы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'shop:watch_detail', kwargs={'pk': self.pk}
        )


class Brand(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Country(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Mechanism(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Тип механизма'
        verbose_name_plural = 'Типы механизмов'


class WaterResistance(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Водозащита'
        verbose_name_plural = 'Водозащита'


class BodyMaterial(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Материал корпуса'
        verbose_name_plural = 'Материалы корпуса'


class Circlet(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Тип браслета'
        verbose_name_plural = 'Типы браслетов'


class Color(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'


class CaseShape(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Форма корпуса'
        verbose_name_plural = 'Формы корпуса'


class Gender(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class WatchImage(models.Model):
    product = models.ForeignKey(
        'Watch',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Часы',
    )
    image = ResizedImageField(
        'Изображение',
        upload_to='watches_images',
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return 'Изображение часов'


class Condition(BaseForCategories):

    class Meta:
        ordering = ['-name']
        verbose_name = 'Состояние часов'
        verbose_name_plural = 'Состояние часов'
