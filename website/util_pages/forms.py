from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=55,
        widget=forms.TextInput(
            attrs={'placeholder': 'Чтобы знать, как обращаться'}
        )
    )
    phone_number = PhoneNumberField(
        widget=RegionalPhoneNumberWidget(
            attrs={'placeholder': 'Чтобы знать, куда звонить'}
        )
    )
    text = forms.CharField(
        label='Описание',
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Чтобы знать, как обращаться'}
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].required = True
        self.fields['phone_number'].label = 'Номер телефона'
