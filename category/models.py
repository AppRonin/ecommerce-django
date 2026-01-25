from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='photos/categories', blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def get_url(self):
        return reverse('product_by_categories', args=[self.slug])

    def __str__(self):
        return self.name