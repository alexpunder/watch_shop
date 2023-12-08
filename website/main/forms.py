from django import forms
from phonenumber_field.formfields import PhoneNumberField


YES_OR_NO = (
    ('', ''),
    ('Да', 'Да'),
    ('Нет', 'Нет'),
)


class MessageForm(forms.Form):
    phone_number = PhoneNumberField()
    description = forms.CharField(
        label='Описание',
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Важная информация'})
    )
    image = forms.ImageField(
        label='Изображение',
        widget=forms.FileInput(attrs={'placeholder': 'Изображение часов'})
    )

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
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Почта'}
        ),
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
        label='Год покупки',
        input_formats=['%Y'],
        widget=forms.DateInput(
            attrs={'class': 'form-control'}
        ),
        required=False
    )
    description = forms.CharField(
        max_length=255,
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Важная информация', 'style': 'height: 50px;'
            }
        ),
        required=False
    )
    packing_box = forms.ChoiceField(
        label='Имеютются ли упаковка и документы?',
        choices=YES_OR_NO,
        widget=forms.Select(attrs={'class': 'form-control'}),
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
