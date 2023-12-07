from django import forms
from phonenumber_field.formfields import PhoneNumberField


YES_OR_NO = (
    ('Да', 'Да'),
    ('Нет', 'Нет'),
)


class MessageForm(forms.Form):
    phone_number = PhoneNumberField()
    description = forms.CharField(label='Описание', max_length=255)
    image = forms.ImageField(label='Изображение')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].required = True
        self.fields['phone_number'].label = 'Номер телефона'


class ExtendMessageForm(forms.Form):
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Ваше имя',
    )
    phone_number = PhoneNumberField()
    email = forms.EmailField(
        label='Электронная почта',
        required=False
    )
    watch_mark = forms.CharField(
        max_length=255,
        label='Марка часов',
        required=False
    )
    watch_model = forms.CharField(
        max_length=255,
        label='Модель часов и/или референс',
        required=False
    )
    year_of_purchase = forms.DateField(
        label='Дата покупки',
        widget=forms.SelectDateWidget(),
        required=False
    )
    description = forms.CharField(
        max_length=255,
        label='Описание',
        required=False
    )
    packing_box = forms.ChoiceField(
        label='Имеютются ли упаковка и документы?',
        choices=YES_OR_NO,
        required=False
    )
    image = forms.ImageField(
        label='Изображение часов',
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].required = True
        self.fields['phone_number'].label = 'Номер телефона'
