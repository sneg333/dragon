from django.db import models
from polls.models import *
from django.db.models.signals import post_save

class Status(models.Model):
    name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    status_create = models.DateTimeField(auto_now_add = True, auto_now = False)
    status_update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы заказа'

    def __str__(self):
        return "статус %s" % self.name

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price all in order
    order_name = models.CharField(max_length=150, blank=True, default=None)
    order_email = models.EmailField(blank=True, default=None)
    order_phone = models.CharField(max_length=150, blank=True, default=None)
    order_adress = models.CharField(max_length=300, blank=True, verbose_name='адрес доставки', default=None)
    commnt = RichTextUploadingField(blank=True, default=None, verbose_name='комментарий')
    status = models.ForeignKey(Status)
    order_create = models.DateTimeField(auto_now_add = True, auto_now = False)
    order_update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name )

    def save(self, *args, **kwargs): # переопределение поля
        super(Order, self).save(*args, **kwargs)

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, default=None)
    tovar = models.ForeignKey(Tovar, blank=True, default=None)
    nmb = models.IntegerField(default=1)
    orice_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    product_create = models.DateTimeField(auto_now_add = True, auto_now = False)
    product_update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'товар в заказе'
        verbose_name_plural = 'товары в заказе'

    def __str__(self):
        return "%s" % self.tovar.title_tovar

    def save(self, *args, **kwargs): # переопределение поля
        orice_per_item = self.tovar.cena
        self.orice_per_item = orice_per_item
        self.total_price = self.nmb * self.orice_per_item

        super(ProductInOrder, self).save(*args, **kwargs)

def product_in_order_post_save(sender, instance, created, **kwargs): # пост сейв сигнал
    order = instance.order
    all_products_in_older = ProductInOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_products_in_older:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender = ProductInOrder)
