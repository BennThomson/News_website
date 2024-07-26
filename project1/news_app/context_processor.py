from .models import NewsModel


def latest_news(request):
    latest_news = NewsModel.objects.order_by('-published_time')[:10]
    context = {
        'latest_news': latest_news
    }
    return context
