from django.db import models
from django.utils.text import slugify
import random

# Create your models here.


class Product(models.Model):
    PRODUCT_TYPE = (
        ('physical', 'physical'),
        ('digital', 'digital'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField()
    product_type = models.CharField(
        choices=PRODUCT_TYPE, default='physical', max_length=250)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    stock = models.PositiveBigIntegerField(default=0)
    weight = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    dimensions = models.CharField(max_length=50, blank=True, null=True)

    downloadable_file = models.FileField(
        upload_to='products/digital_files', blank=True, null=True)
    download_limit = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        base_slug = slugify(self.name)

        # Only change the slug if it's not set or if the base_slug does not match the current slug's base
        if not self.slug or not self.slug.startswith(base_slug):
            unique_slug = f"{base_slug}-{random.randint(1000, 9999)}"

            # Ensure the generated slug is unique
            while Product.objects.filter(slug=unique_slug).exclude(id=self.id).exists():
                unique_slug = f"{base_slug}-{random.randint(1000, 9999)}"

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def is_in_stock(self):
        return self.product_type == 'physical' and self.stock > 0

    def __str__(self):
        return self.name
