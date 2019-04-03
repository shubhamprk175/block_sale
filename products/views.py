from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
import datetime

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
        # print(request.POST['image'])
        form = ProductForm(request.POST)
        # form['image'] = request.POST['image']
        if form.is_valid():
            product_item = form.save(commit=False)
            product_photo = request.FILES['image']
            print(product_photo.name)
            print(product_photo.size)
            d = datetime.date.today()
            directory = f"photos/{d.year}/{d:%m}/{d:%d}/"
            product_item.image = directory + product_photo.name
            fs = FileSystemStorage()
            fs.save(directory + product_photo.name, product_photo)
            product_item.save()
            # print(form.cleaned_data)
    else:
        form = ProductForm()
    return render(request, 'products/addproduct.html', {"form":form})
