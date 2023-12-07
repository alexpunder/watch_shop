from django.forms import Form, CharField, ImageField
from phonenumber_field.formfields import PhoneNumberField


class MessageForm(Form):
    number_phone = PhoneNumberField()
    description = CharField(label='Описание', max_length=255)
    image = ImageField(label='Изображение')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['number_phone'].required = True
        self.fields['number_phone'].label = 'Номер телефона'
