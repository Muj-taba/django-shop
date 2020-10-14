from django.db import models
from django.conf import settings
from django.shortcuts import reverse


CATEGORY_CHOSES = {
    ('S','Shirt'),
    ('SW','Sport wear'),
    ('OT','Outwear')
}

LABEL_CHOSES = {
    ('P','primary'),
    ('S','secondary'),
    ('D','danger')
}

class Item(models.Model):
    title          = models.CharField(max_length=100)
    price          = models.FloatField()
    discount_price = models.FloatField(default=False,blank=True,null=True)
    slug           = models.SlugField()
    category       = models.CharField(choices=CATEGORY_CHOSES,max_length=2)
    label          = models.CharField(choices=LABEL_CHOSES,max_length=1)
    description    = models.CharField(max_length=100)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('core:product', kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse('core:add_to_cart', kwargs={'slug': self.slug})



class OrderItem(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    ordered      = models.BooleanField(default=False)
    item     = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items        = models.ManyToManyField(OrderItem,)
    start_date   = models.DateField(auto_now_add=True)
    ordered_date = models.DateField()
    ordered      = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username

