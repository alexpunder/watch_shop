from django.shortcuts import render, redirect

from .forms import MessageForm, ExtendMessageForm
from .bot_sending_messages import message, extend_message


def homepage(request):
    """
    Представление для отображения главной страницы. Обрабатывается форма
    отправки сообщения ботом в телеграмм-канал; сохранение обращения
    пользователя в БД.
    """
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            text = form.cleaned_data['description']
            image = form.cleaned_data['image']
            message(phone, text, image)
            form.save()
            return redirect('main:popup_message')
    else:
        form = MessageForm()

    return render(
        request, template_name='index.html', context={
            'form': form
        }
    )


def sell_watches(request):
    """
    Представление для отображения страницы с продажей пользователем часов.
    Обрабатывается форма отправки сообщения ботом в телеграмм-канал;
    сохранение обращения пользователя в БД.
    """
    template_name = 'watches/sell_watches.html'
    if request.method == 'POST':
        extend_form = ExtendMessageForm(request.POST, request.FILES)
        if extend_form.is_valid():
            extend_message(**extend_form.cleaned_data)
            extend_form.save()
            return redirect('main:popup_message')
    else:
        extend_form = ExtendMessageForm()
    context = {
        'extend_form': extend_form
    }
    return render(request, template_name, context)


def buy_watch(request):
    template_name = 'watches/watch_details.html'
    return render(request, template_name)


def send_message(request):
    """
    Представление для отображения страницы 'О нас'.
    Обрабатывается форма отправки сообщения ботом в телеграмм-канал;
    без сохранение обращения пользователя в БД.
    """
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = MessageForm()
    return render(
        request, template_name='util_pages/about.html', context={'form': form}
    )


def evaluation(request):
    """
    Представление для отображения страницы 'Оценка часов'.
    """
    template_name = 'watches/evaluation.html'
    return render(request, template_name)


def services(request):
    """
    Представление для отображения страницы 'Услуги'.
    """
    template_name = 'watches/services.html'
    return render(request, template_name)


def popup_message(request):
    template_name = 'watches/popup_message.html'
    return render(request, template_name)
