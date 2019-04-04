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

admin.site.register(Dom)
admin.site.register(Dost_Oplat)
admin.site.register(Usluga)
admin.site.register(Garantija)
