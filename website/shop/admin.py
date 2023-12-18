from django.contrib import admin

from .models import (
    Watch, Brand, Country, Mechanism, WaterResistance, BodyMaterial, Circlet,
    Color, CaseShape, Gender, WatchImage, Condition
)


class ProductImageInline(admin.TabularInline):
    model = WatchImage
    extra = 1


class BaseForCategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'slug'
    )
    list_display_links = (
        'name', 'slug'
    )
    search_fields = (
        'name', 'slug'
    )
    list_filter = (
        'name',
    )


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = (
        'is_available', 'is_published', 'is_on_main',
        'condition', 'brand', 'name', 'price',
        'article', 'country', 'mechanism', 'water_resistance',
        'body_material', 'circlet', 'color', 'case_shape', 'gender',
    )
    list_display_links = (
        'brand',
        'name', 'article', 'country', 'mechanism', 'water_resistance',
        'body_material', 'circlet', 'color', 'case_shape', 'gender'
    )
    list_filter = (
        'is_available', 'is_published', 'is_on_main', 'condition',
        'brand', 'country', 'mechanism', 'water_resistance',
        'body_material', 'circlet', 'color', 'case_shape', 'gender'
    )
    list_editable = (
        'is_available', 'is_published', 'is_on_main', 'condition',
    )
    search_fields = (
        'name', 'price',
    )
    list_per_page = 25


@admin.register(Brand)
class BrandAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(Country)
class CountryAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(Mechanism)
class MechanismAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(WaterResistance)
class WaterResistanceAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(BodyMaterial)
class BodyMaterialAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(Circlet)
class CircletAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(Color)
class ColorAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(CaseShape)
class CaseShapeAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(Gender)
class GenderAdmin(BaseForCategoriesAdmin):
    pass


@admin.register(WatchImage)
class WatchImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Condition)
class ConditionAdmin(BaseForCategoriesAdmin):
    pass
