from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = Mainsite.objects.all()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,

    }
    return render(request, 'mainsite/index.html', context=context)

def about(request):
    return render(request, 'mainsite/about.html', {'menu': menu, 'title': 'О Нас'})

def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('home')
        
    else:
        form = AddPostForm()
    return render(request, 'mainsite/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_slug):
    post = get_object_or_404(Mainsite, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,

    }

    return render(request, 'mainsite/post.html', context=context)

def show_category(request, cat_slug):
    posts = Mainsite.objects.filter(cat__slug=cat_slug)


    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_slug,

    }

    return render(request, 'mainsite/index.html', context=context)