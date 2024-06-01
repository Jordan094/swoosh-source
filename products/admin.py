from django.contrib import admin
from .models import Product, Category, Favourites

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'category',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class FavouritesAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        field_names = [field.name for field in Favourites._meta.fields]
        return field_names


admin.site.register(Favourites, FavouritesAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)