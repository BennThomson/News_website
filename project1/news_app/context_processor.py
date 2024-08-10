from .models import NewsModel, Category
import requests


def latest_news(request):
    latest_news = NewsModel.objects.order_by('-published_time')[:10]
    categories = Category.objects.all()
    print(requests.get(url="https://nbu.uz/exchange-rates/json/").json()[23]["title"])
    BuyUSD = requests.get(url='https://nbu.uz/exchange-rates/json/').json()[23]['nbu_buy_price']
    SellUSD = requests.get(url='https://nbu.uz/exchange-rates/json/').json()[23]['nbu_cell_price']
    BuyRuble = requests.get(url='https://nbu.uz/exchange-rates/json/').json()[18]['nbu_buy_price']
    SellRuble = requests.get(url='https://nbu.uz/exchange-rates/json/').json()[18]['nbu_cell_price']
    context = {
        'latest_news': latest_news,
        'categories': categories,
        'BuyUSD': BuyUSD,
        'SellUSD': SellUSD,
        'BuyRuble': BuyRuble,
        'SellRuble': SellRuble,
    }
    return context
