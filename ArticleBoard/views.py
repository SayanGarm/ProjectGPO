from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.urls import reverse_lazy

from .forms import ArticleForm
from .models import Article

class ArticleCreate(View):
    def get(self, request, *args, **kwargs):
        context = { 'form': ArticleForm}
        return render(request, 'Article/create_article.html', context)
    def post(self, request, *args, **kwargs):

        return render(request, 'Article/create_article.html', {})



def index(request) :
    return render(request, 'Article/create_article.html', {})
