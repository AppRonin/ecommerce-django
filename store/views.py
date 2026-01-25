from django.shortcuts import render
from .models import Product

# Create your views here.
def store(request, category_slug=None):
    
    if category_slug != None:
        products = Product.objects.all().filter(is_available=True, category__slug=category_slug)
    else:
        products = Product.objects.all().filter(is_available=True)

    products_count = products.count()

    context = {'products': products, 'products_count': products_count}

    return render(request, 'store/store.html', context)