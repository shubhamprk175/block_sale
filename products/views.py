from django.shortcuts import render

from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.order_by('-posted_on').filter(status=True)
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)

def product(request, product_id):
    return render(request, 'products/product.html')