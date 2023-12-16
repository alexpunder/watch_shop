from django.contrib import admin

from .models import (
    Watch, Brand, Country, Mechanism, WaterResistance, BodyMaterial, Circlet,
    Color, CaseShape, Gender, WatchImage, Condition
)


class ProductImageInline(admin.TabularInline):
    model = WatchImage
    extra = 1


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
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Mechanism)
class MechanismAdmin(admin.ModelAdmin):
    pass


@admin.register(WaterResistance)
class WaterResistanceAdmin(admin.ModelAdmin):
    pass


@admin.register(BodyMaterial)
class BodyMaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(Circlet)
class CircletAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(CaseShape)
class CaseShapeAdmin(admin.ModelAdmin):
    pass


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    pass


@admin.register(WatchImage)
class WatchImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    pass
