from django.urls import path
from .views import (NewsView, news_detail, HomeView, contactView, ErrorView, aboutView,
                    foreignNewsView, sportNewsView, economyNewsView, technologyNewsView, societyNewsView,)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('all_news', NewsView, name='news'),
    path('news/<slug:news>/', news_detail, name='news_detail'),
    path('contact/', contactView, name='contact_page'),
    path('error/', ErrorView, name='error'),
    path('about/', aboutView, name='about_page'),
    path('jahon/', foreignNewsView, name='foreignNews'),
    path('sport/', sportNewsView, name='sportNews'),
    path('economy/', economyNewsView, name='economyNews'),
    path('technology/', technologyNewsView, name='technologyNews'),
    path('society/', societyNewsView, name='societyNews'),
]

