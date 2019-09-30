from django.db import models
from polls.models import *

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
    order_name = models.CharField(max_length=150, blank=True)
    order_email = models.EmailField(blank=True)
    order_phone = models.CharField(max_length=150, blank=True)
    status = models.ForeignKey(Status)
    order_create = models.DateTimeField(auto_now_add = True, auto_now = False)
    order_update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.status.name )

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, blank=True)
    tovar = models.ForeignKey(Tovar, blank=True)
    is_active = models.BooleanField(default=True)
    product_create = models.DateTimeField(auto_now_add = True, auto_now = False)
    product_update = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'

    def __str__(self):
        return "товар %s" % self.tovar.title_tovar