from django.db import models
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    # Fields for the Category model
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    type = models.CharField(max_length=100, default='nike-air')

    def __str__(self):
        # Return the category name when the object is printed
        return self.name

    def get_friendly_name(self):
        # Return the friendly name of the category
        return self.friendly_name


class Product(models.Model):
    # ForeignKey to link each product to a category, with optional null values
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        # Return the product name when the object is printed
        return self.name


class Favourites(models.Model):
    favourite_item = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='products')
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='products')
