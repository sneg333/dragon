from django.contrib import admin
from .models import *

<<<<<<< HEAD
=======
# class TovarPlusInAdmin(admin.TabularInline): # добавление фото прямо во вкладке товара в админке
#     model = Gallery
#     extra = 0 # количество добавок

>>>>>>> a67ad82c94aaefd5389dc039041a0b4105c59841
class ZakazAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email',
                    'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']

admin.site.register(Zakaz, ZakazAdmin)

class TovarAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ['title_tovar']
    search_fields = ['title_tovar']
=======
    list_display = ['id','title_tovar', 'iden', 'is_active']
    search_fields = ['title_tovar', 'iden']
    # inlines = [TovarPlusInAdmin]
>>>>>>> a67ad82c94aaefd5389dc039041a0b4105c59841

admin.site.register(Tovar, TovarAdmin)

class KatalogAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title_katalog",)}

admin.site.register(Katalog, KatalogAdmin)

class PodKatalogAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title_podkatalog",)}

admin.site.register(PodKatalog, PodKatalogAdmin)

<<<<<<< HEAD
=======
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_gallery', 'is_active']

admin.site.register(Gallery, GalleryAdmin)

>>>>>>> a67ad82c94aaefd5389dc039041a0b4105c59841
admin.site.register(Dom)
admin.site.register(Dost_Oplat)
admin.site.register(Usluga)
admin.site.register(Garantija)
<<<<<<< HEAD
admin.site.register(Gallery)
=======
>>>>>>> a67ad82c94aaefd5389dc039041a0b4105c59841
