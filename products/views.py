from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.
def products(request):
    products = Product.objects.order_by('-posted_on')
    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)
