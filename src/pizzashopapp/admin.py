from django.contrib import admin

from .models import PizzaShop,Pizza

# Register your models here.
admin.site.register(PizzaShop)
admin.site.register(Pizza)