from django.shortcuts import render
from django.views import generic
from .models import Article

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        return Article.objects.order_by('-created_at')[:5]


