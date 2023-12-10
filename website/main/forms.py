from django.forms import ModelForm

from .models import Message, ExtendMessage


class MessageForm(ModelForm):

    class Meta:
        model = Message
        fields = (
            'phone_number', 'description', 'image'
        )


class ExtendMessageForm(ModelForm):

    class Meta:
        model = ExtendMessage
        fields = (
            'first_name', 'phone_number', 'email', 'watch_mark',
            'watch_model', 'year_of_purchase', 'description',
            'packing_box', 'image'
        )
