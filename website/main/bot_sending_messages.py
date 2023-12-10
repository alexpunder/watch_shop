import os
from django.conf import settings
from telegram import Bot


TELEGRAM_TOKEN = '6727372454:AAHFXntTCuHnO5Vl7cUKfUf69O9ctFYf-k0'
CHANAL_ID = '-1002109369857'  # 1414299754 (мой ID)


def message(phone, text, image):
    bot = Bot(token=TELEGRAM_TOKEN)
    image_path = os.path.join(settings.MEDIA_ROOT, 'temp_image.jpg')
    with open(image_path, 'wb') as image_file:
        for chunk in image.chunks():
            image_file.write(chunk)

    text_message = (
        'Пользователь оставил следюущие данные: \n'
        f'Телефон для связи - {phone} \n'
        f'Сопроводительный текст - {text} \n'
    )
    with open(image_path, 'rb') as image_file:
        bot.send_photo(
            chat_id=CHANAL_ID, photo=image_file, caption=text_message
        )

    os.remove(image_path)
