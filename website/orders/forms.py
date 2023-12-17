from django import forms

from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = (
            'first_name', 'last_name', 'phone_number',
            'email', 'adress'
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Обязательное поле'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Обязательное поле'}
            ),
            'phone_number': forms.TextInput(
                attrs={'placeholder': 'Обязательное поле'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Обязательное поле'}
            ),
            'adress': forms.TextInput(
                attrs={'placeholder': 'По желанию'}
            ),
        }
