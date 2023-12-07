from django.shortcuts import render

from .forms import MessageForm


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
