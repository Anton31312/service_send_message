from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import blog, ArticleDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('article/', blog, name='article_list'),
    path('article/view/<int:pk>/', cache_page(60)(ArticleDetailView.as_view()), name='article_view'),
    ]