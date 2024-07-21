from django.urls import path
from .views import NewsView, news_detail, homeView

urlpatterns = [
    path('', homeView, name='home'),
    path('all_news', NewsView, name='news'),
    path('news/<int:id>/', news_detail, name='news_detail'),
]

