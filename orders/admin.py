from django.contrib import admin
from .models import *

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    pass
class ToppingsAdmin(admin.ModelAdmin):
    pass
class PizzaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Customer, CustomerAdmin)
admin.site.register(PizzaOrder, PizzaAdmin)
admin.site.register(PizzaBase)
admin.site.register(Toppings, ToppingsAdmin)
admin.site.register(NotPizzaBase)
admin.site.register(NotPizzaOrder)
admin.site.register(SubModifications)
admin.site.register(Order)
