from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
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

def addproduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product_item = form.save(commit = False)
            product_item.save()
    else:
        form = ProductForm()
    return render(request, 'products/addproduct.html', {"form":form})
