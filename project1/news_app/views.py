from urllib import request
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import detail, ListView
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
#     return render(request, template_name='news/home.html', context=context)

class HomeView(ListView):
    model = NewsModel
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['latest_news'] = NewsModel.published.all().order_by('-published_time')[:5]
        context['iqdisodiyot_news'] = NewsModel.published.all().filter(category__name='Iqdisodiyot').order_by('-published_time')[:5]
        context['jamiyat_news'] = NewsModel.published.all().filter(category__name='Jamiyat').order_by('-published_time')[:5]
        context['texnologiya_news'] = NewsModel.published.all().filter(category__name='Fan-texnika').order_by('-published_time')[:5]
        context['sport_news'] = NewsModel.published.all().filter(category__name='Sport').order_by('-published_time')[:5]
        return context


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
    form = ContactForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        # return HttpResponse("Hush kelibsiz")
        return redirect('contact_page')
    context = {
        'form': form
    }

    return render(request, 'news/contact.html', context=context)

