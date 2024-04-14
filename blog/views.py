from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import Article

def blog(request):
    context = {
        'object_list': Article.objects.all(),
        'title': " Блог",
    }
    return render(request, 'blog/article_list.html', context)


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
