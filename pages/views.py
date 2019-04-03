from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        print("Doing")
        products = Product.objects.order_by('-posted_on').filter(status=True).exclude(posted_by=request.user.id)
        print("Done")
    else:
        products = Product.objects.order_by('-posted_on').filter(status=True)
    context = {
        'products': products
    }
    return render(request, 'pages/index.html', context)
