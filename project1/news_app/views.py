from django.shortcuts import render, get_object_or_404
from django.views.generic import detail

from .models import NewsModel, Category


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


