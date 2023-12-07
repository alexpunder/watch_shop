from django.shortcuts import render

from .forms import MessageForm, ExtendMessageForm


def homepage(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = MessageForm()
    return render(
        request, template_name='index.html', context={'form': form}
    )


def sell_watches(request):
    template_name = 'watches/sell_watches.html'
    if request.method == 'POST':
        form = ExtendMessageForm(request.POST, request.FILES)
        if form.is_valid():
            pass
    else:
        form = ExtendMessageForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
