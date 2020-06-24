from django.contrib import admin
from .models import *

from import_export.admin import ImportExportModelAdmin as iema


@admin.register(Customer)
class Customer(iema):
    pass
@admin.register(Product)
class Product(iema):
    pass
@admin.register(Order)
class Order(iema):
    pass
@admin.register(OrderItem)
class OrderItem(iema):
    pass
@admin.register(ShippingAddress)
class ShippingAddress(iema):
    pass



