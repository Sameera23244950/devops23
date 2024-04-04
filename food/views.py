from django.shortcuts import render

from . models import Category

from django.shortcuts import get_object_or_404
from .models import Product





# Create your views here.

def food(request):

    all_products = Product.objects.all()

    context = {'my_products' :all_products}

    return render(request, 'food/food.html', context)

def categories(request):

    all_categories = Category.objects.all()

    return {'all_categories': all_categories}


def list_category(request, category_slug=None):
    # Note the capital 'C' in 'Category'
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(Category=category)
    return render(request, 'food/list-category.html', {'category': category, 'products': products})

     

def product_details(request, product_slug):
    # Fetch the product details
    details = get_object_or_404(Product, slug=product_slug)
    product_details1 = {'productdetails': details}
    return render(request, 'food/product-details.html', product_details1)

