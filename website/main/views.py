from django.shortcuts import render, redirect

from .forms import MessageForm, ExtendMessageForm
from .bot_sending_messages import message


def homepage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            text = form.cleaned_data['description']
            image = form.cleaned_data['image']
            message(phone, text, image)
            return redirect('main:homepage')
    else:
        form = MessageForm()

    return render(
        request, template_name='index.html', context={
            'form': form
        }
    )


def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = MessageForm()
    return render(
        request, template_name='util_pages/about.html', context={'form': form}
    )


def sell_watches(request):
    template_name = 'watches/sell_watches.html'
    if request.method == 'POST':
        extend_form = ExtendMessageForm(request.POST, request.FILES)
        if extend_form.is_valid():
            pass
    else:
        extend_form = ExtendMessageForm()
    context = {
        'extend_form': extend_form
    }
    return render(request, template_name, context)
