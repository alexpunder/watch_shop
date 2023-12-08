from django.shortcuts import render

from .forms import MessageForm, ExtendMessageForm


def homepage(request):
    if request.method == 'POST':
        form_name = request.POST.get('form_name')

        if form_name == 'message_form':
            form = MessageForm(request.POST, request.FILES)
            extend_form = ExtendMessageForm()
            if form.is_valid():
                pass

        elif form_name == 'extend_form':
            form = MessageForm()
            extend_form = ExtendMessageForm(request.POST, request.FILES)
            if extend_form.is_valid():
                pass
    else:
        form = MessageForm()
        extend_form = ExtendMessageForm()

    return render(
        request, template_name='index.html', context={
            'form': form,
            'extend_form': extend_form
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
