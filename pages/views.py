from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
    products = Product.objects.order_by('-posted_on').filter(status=True)
    context = {
        'products': products
    }
    return render(request, 'pages/index.html', context)