from django import forms


class AddToCart(forms.Form):
    update = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
