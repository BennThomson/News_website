from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import detail
from .models import NewsModel, Category
from .forms import ContactForm

def NewsView(request):
    news_list = NewsModel.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news.html', context)


def news_detail(request, id):
    news = get_object_or_404(NewsModel, id=id, status=NewsModel.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news-detail.html', context)


def homeView(request):
    news = NewsModel.published.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'categories': categories
    }
    return render(request, template_name='news/home.html', context=context)


def contactView(request):
    context = {}
    return render(request, template_name='news/contact.html', context=context)


def ErrorView(request):
    context = {}
    return render(request, template_name='news/404.html', context=context)


def aboutView(request):
    context = {}
    return render(request, template_name='news/about_page.html', context=context)


def contactView(request):
    print(request.POST)
    form = ContactForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("Hush kelibsiz")
        # return redirect('contact_page')
    context = {
        'form': form
    }

    return render(request, 'news/contact.html', context=context)

