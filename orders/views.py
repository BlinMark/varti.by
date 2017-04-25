from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm, OrderCreateSizeForm
from cart.cart import Cart


def OrderCreate(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            assert isinstance(cart, object)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})

    form = OrderCreateForm()
    form_2 = OrderCreateSizeForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form,
                                                        'form_2': form_2})

