from django.contrib import admin

from .models import Message, ExtendMessage


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'processed', 'pub_date', 'phone_number', 'description', 'image'
    )
    list_display_links = (
        'phone_number', 'pub_date',
    )
    list_editable = (
        'processed',
    )
    search_fields = (
        'phone_number', 'processed', 'pub_date'
    )
    list_filter = (
        'processed',
    )
    readonly_fields = (
        'pub_date', 'phone_number', 'description', 'image'
    )


@admin.register(ExtendMessage)
class ExtendMessageAdmin(admin.ModelAdmin):
    list_display = (
        'processed', 'pub_date', 'phone_number', 'first_name', 'email',
        'watch_mark', 'watch_model', 'description', 'image',
        'year_of_purchase', 'packing_box'
    )
    list_display_links = (
        'phone_number', 'pub_date',
    )
    list_editable = (
        'processed',
    )
    search_fields = (
        'phone_number', 'processed', 'pub_date', 'watch_mark', 'watch_model',
        'first_name', 'email',
    )
    list_filter = (
        'processed',
    )
    readonly_fields = (
        'pub_date', 'phone_number', 'description', 'image',
        'first_name', 'email', 'watch_mark', 'watch_model',
        'year_of_purchase', 'packing_box'
    )
