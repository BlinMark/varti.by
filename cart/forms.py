from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
CHOICES = [('A0', 'A0 80x120'),
           ('A1', 'A1 60x80'),
           ('A2', 'A2 40x60'),
           ('A3', 'A3 30x40'),
           ('A4', 'A4 20x30')]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    size = forms.TypedChoiceField(choices=CHOICES)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
