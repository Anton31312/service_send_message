from django.contrib import admin

from blog.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'body', 'preview', 'date_is_published','views_count','is_active',)
    search_fields = ('title', 'body',)
    list_filter = ('date_is_published','views_count','is_active',)