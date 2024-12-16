from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'products/index.html')


def products(request):
    products = Product.objects.all()
    context = {
        "products" : products,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "products" : product,
    }
    return render(request, 'products/product_detail.html', context)

def create(request, pk):
    pass