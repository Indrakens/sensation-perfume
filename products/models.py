from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):

    class Meta:
        verbose_name_plural = 'Brands'

    name = models.CharField(max_length=254)
    brand_friendly_name = models.CharField(max_length=254, null=True,
                                            blank=True)

    def __str__(self):
        return self.name

    def get_brand_friendly_name(self):
        return self.brand_friendly_name


class Genders(models.Model):

    class Meta:
        verbose_name_plural = 'Genders'

    name = models.CharField(max_length=254)
    gender_friendly_name = models.CharField(max_length=254, null=True,
                                            blank=True)

    def __str__(self):
        return self.name

    def get_gender_friendly_name(self):
        return self.gender_friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True,
                                blank=True, on_delete=models.SET_NULL)                 
    gender = models.ForeignKey('Genders', null=True,
                                blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    product_description = models.TextField()
    include = models.CharField(max_length=254, null=True, blank=True)
    has_giftwrap = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                blank=True)
    price_was = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                    blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += review.rating

        if reviews_total > 0:
            return reviews_total / self.reviews.count()

        return 0


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    rating = models.IntegerField(default=3)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='reviews',
                                    on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
