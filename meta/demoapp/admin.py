from django.contrib import admin
from .models import MenuCategory, MenuCard, MenuChart,Reservation

# we register our models so that it can be identified by django-admin, and not just by manage.py

# Register your models here.
admin.site.register(MenuCategory)
admin.site.register(MenuCard)
admin.site.register(MenuChart)
admin.site.register(Reservation)

