from .models import NewsModel, Category


def latest_news(request):
    latest_news = NewsModel.objects.order_by('-published_time')[:10]
    categories = Category.objects.all()
    context = {
        'latest_news': latest_news,
        'categories': categories
    }
    return context
