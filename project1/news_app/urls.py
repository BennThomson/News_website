from django.urls import path
from .views import NewsView, news_detail, HomeView, contactView, ErrorView, aboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all_news', NewsView, name='news'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('contact/', contactView, name='contact_page'),
    path('error/', ErrorView, name='error'),
    path('about/', aboutView, name='about_page'),
]

