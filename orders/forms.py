from django import forms
from .models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'phone', 'email', 'area', 'city',
                  'street', 'home', 'korpus', 'flat']
