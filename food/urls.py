from django.urls import path

from . import views

urlpatterns = [

    # food main page
    path('', views.food, name='food'),

    #  Individual product
    path('product/<slug:product_slug>', views.product_details, name='product-details'),

    # Individual Category
    path('search/<slug:category_slug>', views.list_category, name='list-category'),


]