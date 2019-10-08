from django.contrib import admin
from .models import *

class ProductInOrderPlusInAdmin(admin.TabularInline): # добавление фото прямо во вкладке товара в админке
    model = ProductInOrder
    extra = 0 # количество добавок

class StatusAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        models = Status

admin.site.register(Status, StatusAdmin)

class OrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderPlusInAdmin]

    class Meta:
        models = Order

admin.site.register(Order, OrderAdmin)

class ProductInOrderAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        models = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderAdmin)