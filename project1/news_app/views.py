from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import detail, ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import NewsModel, Category
from .forms import ContactForm


def NewsView(request):
    request.META['title'] = 'News'
    news_list = NewsModel.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news.html', context)


def news_detail(request, news):
    request.META['title'] = 'News-detail'
    news = get_object_or_404(NewsModel, slug=news, status=NewsModel.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/single_page.html', context)


# def homeView(request):
#     latest_news = NewsModel.published.all().order_by('-published_time')[:5]
#     news = NewsModel.published.all()
#     categories = Category.objects.all()
#     iqdisodiyot_news = NewsModel.published.all().filter(category__name='Iqdisodiyot')
#     local_top_one_new = NewsModel.published.filter(category__name='Iqdisodiyot').order_by('-published_time')[:1]
#     context = {
#         'news': news,
#         'categories': categories,
#         'latest_news': latest_news,
#         'local_news': iqdisodiyot_news,
#         'local_new_one': local_top_one_new
#     }
#     return render(request, template_name='news/home.html', context=context) #home

class HomeView(ListView):
    model = NewsModel
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        self.request.META['title'] = 'Home'
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['latest_news'] = NewsModel.published.all().order_by('-published_time')[:5]
        context['iqdisodiyot_news'] = NewsModel.published.all().filter(category__name='Iqdisodiyot').order_by('-published_time')[:5]
        context['jamiyat_news'] = NewsModel.published.all().filter(category__name='Jamiyat').order_by('-published_time')[:5]
        context['texnologiya_news'] = NewsModel.published.all().filter(category__name='Fan-texnika').order_by('-published_time')[:5]
        context['sport_news'] = NewsModel.published.all().filter(category__name='Sport').order_by('-published_time')[:5]
        return context


def ErrorView(request):
    request.META['title'] = 'Error'
    context = {}
    return render(request, template_name='news/404.html', context=context)


def aboutView(request):
    request.META['title'] = 'Biz haqimizda'
    context = {}
    return render(request, template_name='news/about_page.html', context=context)


def contactView(request):
    request.META['title'] = 'Biz bilan aloqa'
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        # return HttpResponse("Hush kelibsiz")
        return redirect('contact_page')
    context = {
        'form': form
    }
    return render(request, 'news/contact.html', context=context)


def foreignNewsView(request):
    request.META['title'] = 'Jahon yangiliklari'
    foreign_news = NewsModel.published.filter(category__name='Jahon')
    context = {
        "foreign_news": foreign_news
    }
    return render(request, template_name='news/jahon.html', context=context)


def economyNewsView(request):
    request.META['title'] = 'Iqdisodiyot yangiliklari'
    economy_news = NewsModel.published.filter(category__name='Iqdisodiyot')
    context = {
        "economy_news": economy_news
    }
    return render(request, template_name='news/iqdisodiyot.html', context=context)


def societyNewsView(request):
    request.META['title'] = 'Jamiyat Yangiliklari'
    society_news = NewsModel.published.filter(category__name='Jamiyat')
    context = {
        "society_news": society_news
    }
    return render(request, template_name='news/jamiyat.html', context=context)


def technologyNewsView(request):
    request.META['title'] = 'Texnologiya Yangiliklari'
    technology_news = NewsModel.published.filter(category__name='Fan-texnika')
    context = {
        "technology_news": technology_news
    }
    return render(request, template_name='news/texnologiya.html', context=context)


def sportNewsView(request):
    request.META['title'] = 'Sport yangiliklari'
    sport_news = NewsModel.published.filter(category__name='Sport')
    context = {
        "sport_news": sport_news
    }
    return render(request, template_name='news/sport.html', context=context)


class UpdateNewsView(UpdateView):
    model = NewsModel
    field = ['title', 'slug', 'body', 'image', 'category']
    template_name = 'crud functions/update.html'
