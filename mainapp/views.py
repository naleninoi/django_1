import os, datetime, json

from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404


from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


def main(request):
    title = 'Главная'
    products = Product.objects.all()[:3]
    content = {
        'title': title,
        'products': products
    }
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    title = 'Продукты'
    links_menu = ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category = {'name': 'все', 'pk': 0}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk = pk)

        content = {
            'title': title,
            'links_menu': links_menu,
            'products': products_list,
            'category': category,
            'basket': basket
        }
        return render(request, 'mainapp/products_list.html', content)

    same_products = Product.objects.all()[1:7]
    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'Контакты'
    visit_date = datetime.datetime.now()
    file_path = os.path.join(settings.BASE_DIR, 'mainapp/json/contacts.json')
    with open(file_path, encoding='utf-8') as file_contacts:
        locations = json.load(file_contacts)
    content = {'title': title, 'visit_date': visit_date, 'locations': locations}
    return render(request, 'mainapp/contact.html', content)


def not_found(request, exception):
    print(exception)
    # подготовка данных и т.д.
    return render(request, '404.html', context={'item': 'no data here'}, status=404)
