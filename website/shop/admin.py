from django.contrib import admin

from .models import (
    Watch, Brand, Country, Mechanism, WaterResistance, BodyMaterial, Circlet,
    Color, CaseShape, Gender, Image
)


@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    pass


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


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
