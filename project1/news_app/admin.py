from django.contrib import admin
from .models import NewsModel, Category, ContactModel

admin.site.register(ContactModel)

@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'published_time', 'status']
    list_filter = ['status', 'created_time', 'published_time', 'category']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_time'
    search_fields = ['title', 'body']
    ordering = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
