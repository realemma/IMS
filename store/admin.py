from django.contrib import admin

# Register your models here.

from .models import Category, Location,Item

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Item)


