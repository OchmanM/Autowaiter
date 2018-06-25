from django.contrib import admin

# Register your models here.

from orders.models import *

admin.site.register(Table)
admin.site.register(Order)
admin.site.register(Product)