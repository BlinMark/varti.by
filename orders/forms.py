from django import forms
from .models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'phone', 'country', 'area', 'city',
                  'street', 'home', 'korpus', 'flat']

class OrderCreateSizeForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = ['product_size']

