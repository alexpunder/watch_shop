import os
from django.conf import settings
from telegram import Bot


TELEGRAM_TOKEN = '6727372454:AAHFXntTCuHnO5Vl7cUKfUf69O9ctFYf-k0'
CHANAL_ID = '-1002109369857'

bot = Bot(token=TELEGRAM_TOKEN)


def message(phone, text, image):
    some_text = text if text else 'ничего не написали...'
    text_message = (
        'Пользователь оставил следюущие данные: \n'
        f'Телефон для связи - {phone} \n'
        f'Сопроводительный текст - {some_text} \n'
    )
    if image:
        image_path = os.path.join(settings.MEDIA_ROOT, 'temp_image.jpg')
        with open(image_path, 'wb') as image_file:
            for chunk in image.chunks():
                image_file.write(chunk)

        text_message = (
            'Пользователь оставил следюущие данные \n'
            f'Телефон для связи: {phone} \n'
            f'Сопроводительный текст: {some_text} \n'
        )
        with open(image_path, 'rb') as image_file:
            bot.send_photo(
                chat_id=CHANAL_ID, photo=image_file, caption=text_message
            )
    else:
        bot.send_message(
            chat_id=CHANAL_ID, text=text_message
        )


def extend_message(**kwargs):
    first_name = kwargs['first_name']
    phone_number = kwargs['phone_number']
    watch_mark = kwargs['watch_mark']
    email = (
        'не указана' if kwargs['email'] is None
        else kwargs['email']
    )
    watch_model = (
        'не указана' if kwargs['watch_model'] is None
        else kwargs['watch_model']
    )
    year_of_purchase = (
        'не указан' if kwargs['year_of_purchase'] is None
        else kwargs['year_of_purchase']
    )
    description = (
        'ничего не написали' if kwargs['description'] is None
        else kwargs['description']
    )
    packing_box = (
        'не указано' if kwargs['packing_box'] is None
        else kwargs['packing_box']
    )
    image = kwargs.get('image')
    total_message = (
        'Пользователь оставил следюущие данные \n'
        f'Имя: {first_name} \n'
        f'Телефон для связи: {phone_number} \n'
        f'Марка часов: {watch_mark} \n'
        f'Электронная почта: {email} \n'
        f'Модель часов: {watch_model} \n'
        f'Год покупки: {year_of_purchase} \n'
        f'Описание: {description} \n'
        f'Наличие упаковки/документов: {packing_box} \n'
    )
    if image:
        image_path = os.path.join(settings.MEDIA_ROOT, 'temp_image_second.jpg')
        with open(image_path, 'wb') as image_file:
            for chunk in image.chunks():
                image_file.write(chunk)

        with open(image_path, 'rb') as image_file:
            bot.send_photo(
                chat_id=CHANAL_ID, photo=image_file, caption=total_message
            )
    else:
        bot.send_message(
            chat_id=CHANAL_ID, text=total_message
        )
