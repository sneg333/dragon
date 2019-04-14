from django.contrib import admin
from .models import *

class ZakazAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email',
                    'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']

admin.site.register(Zakaz, ZakazAdmin)

class TovarAdmin(admin.ModelAdmin):
    list_display = ['title_tovar']
    search_fields = ['title_tovar']

admin.site.register(Tovar, TovarAdmin)

class KatalogAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title_katalog",)}

admin.site.register(Katalog, KatalogAdmin)

class PodKatalogAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title_podkatalog",)}

admin.site.register(PodKatalog, PodKatalogAdmin)

admin.site.register(Dom)
admin.site.register(Dost_Oplat)
admin.site.register(Usluga)
admin.site.register(Garantija)
admin.site.register(Gallery)