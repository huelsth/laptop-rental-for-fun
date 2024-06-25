from django.contrib import admin
from .models import Laptop, Accessory, Insurance, Rental

admin.site.register(Laptop)
admin.site.register(Accessory)
admin.site.register(Insurance)
admin.site.register(Rental)
