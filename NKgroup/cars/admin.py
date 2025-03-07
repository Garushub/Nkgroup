from django.contrib import admin
from .models import Car, CarPhoto

class CarPhotoInline(admin.TabularInline):
    model = CarPhoto
    extra = 1

class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'category', 'price_per_day', 'license_plate')
    inlines = [CarPhotoInline]

admin.site.register(Car, CarAdmin)