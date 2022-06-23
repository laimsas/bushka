from django.contrib import admin
from .models import Categorie, Weapon

# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('categorie', 'description')
    

class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'categorie')


admin.site.register(Categorie)
admin.site.register(Weapon)