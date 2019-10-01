from django.contrib import admin
from .models import *

class TovarPlusInAdmin(admin.TabularInline): # добавление фото прямо во вкладке товара в админке
    model = Gallery
    extra = 0 # количество добавок

class ZakazAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email',
                    'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']

admin.site.register(Zakaz, ZakazAdmin)

class TovarAdmin(admin.ModelAdmin):
    list_display = ['id','title_tovar', 'iden', 'is_active']
    search_fields = ['title_tovar', 'iden']
    inlines = [TovarPlusInAdmin]

admin.site.register(Tovar, TovarAdmin)

class KatalogAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title_katalog",)}

admin.site.register(Katalog, KatalogAdmin)

class PodKatalogAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title_podkatalog",)}

admin.site.register(PodKatalog, PodKatalogAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title_gallery', 'is_active']

admin.site.register(Gallery, GalleryAdmin)

admin.site.register(Dom)
admin.site.register(Dost_Oplat)
admin.site.register(Usluga)
admin.site.register(Garantija)
