from itertools import product

from django.shortcuts import render, redirect
from .models import Category, Video
from django.views import View


# Create your views here.
def home_page(request):
    # Достаем данные из БД
    products = Video.objects.all()
    categories = Category.objects.all()
    # Достаем форму
    #form = SearchForm
    # Отправляем данные на фронт
    context = {'products': products, 'categories': categories}

    return render(request, 'home.html', context)


def video_page(request, pk):
    # Достаем данные из БД
    video = Video.objects.get(id=pk)
    # Отправляем данные на фронт
    context = {'video': video}
    return render(request, 'video.html', context)


def category_page(request, pk):
    # Определяем выбранную категорию
    category = Category.objects.get(id=pk)
    exact_video = Video.objects.filter(product_category=category)
    # Отправляем данные на фронт
    context = {'category': category, 'video': exact_video}
    return render(request, 'category.html', context)


def search(request):
    if request.method == "POST":
        get_product = request.POST.get('search_bar')

        if Product.objects.get(product_name__iregex=get_product):
            exact_product = Product.objects.get(product_name__iregex=get_product)
            return redirect(f'/product/{exact_product.id}')
        else:
            print('Не нашел')
            return redirect('/')




