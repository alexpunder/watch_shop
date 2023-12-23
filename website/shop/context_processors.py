from .cart import Cart
from main.forms import FooterMessageForm
from main.bot_sending_messages import message


def cart(request):
    return {'cart': Cart(request)}


def form_footer(request):
    form = FooterMessageForm()

    if request.method == 'POST':
        form = FooterMessageForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone_number']
            text = form.cleaned_data['description']
            message(phone, text)

    return {'form_footer': form}
