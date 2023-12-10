from django.contrib import admin

from .models import Message, ExtendMessage


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(ExtendMessage)
class MessageAdmin(admin.ModelAdmin):
    pass
