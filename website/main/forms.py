from django import forms

from .models import Message, ExtendMessage


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = (
            'phone_number', 'description', 'image'
        )


class FooterMessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = (
            'phone_number', 'description'
        )
        widgets = {
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Введите номер для связи'}
            ),
            'description': forms.TextInput(
                attrs={'placeholder': 'Напишите, что Вас интересует'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].label = ''
        self.fields['description'].label = ''


class ExtendMessageForm(forms.ModelForm):

    class Meta:
        model = ExtendMessage
        fields = (
            'first_name', 'phone_number', 'watch_mark', 'email',
            'watch_model', 'year_of_purchase', 'description',
            'packing_box', 'image'
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Обязательное поле'}
            ),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Обязательное поле'}
            ),
            'watch_mark': forms.TextInput(
                attrs={'placeholder': 'Обязательное поле'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'По желанию'}
            ),
            'watch_model': forms.TextInput(
                attrs={'placeholder': 'По желанию'}
            ),
            'year_of_purchase': forms.DateInput(
                attrs={'placeholder': 'По желанию'}),
            'description': forms.TextInput(
                attrs={'placeholder': 'По желанию'}
            ),
            'packing_box': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }
