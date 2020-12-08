from django.contrib import admin

from basketapp.models import Basket


class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_display_links = ('product', 'quantity')


admin.site.register(Basket, BasketAdmin)
