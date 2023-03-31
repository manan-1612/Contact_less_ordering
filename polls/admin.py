from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Table)
admin.site.register(food_item)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Order_food_mapping)
