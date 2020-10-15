from django.contrib import messages
from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem ,Order
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.


class ProductList(ListView):
    model = Item
    paginate_by = 2
    template_name = 'product_list.html'


class ProductDetail(DetailView):
    model = Item
    template_name = 'product.html'


def add_to_cart(request, slug):
    item       = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs   =  Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,'this item quantity has been updated successfully!')

        else:
            messages.info(request,'this item has been added to the cart successfully!')
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,'this item has been added to the cart successfully!')

    return redirect("core:product",slug=slug)


def remove_from_cart(request, slug):
    item       = get_object_or_404(Item, slug=slug)

    order_qs   =  Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request,'this item has been removed from the cart successfully!')
            return redirect("core:product",slug=slug)

        else:
            messages.info(request,'this item was not in your cart')
            return redirect("core:product",slug=slug)


    else:
        messages.info(request,'you do not have an active order !!')

        return redirect("core:product",slug=slug)

