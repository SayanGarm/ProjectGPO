from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.urls import reverse_lazy

from .forms import ArticleForm
from .models import Article
from Account.decorators import allowed_roles, author_or_moder_only

class ArticleCreate(View):
    def get(self, request, *args, **kwargs):
        context = { 'form': ArticleForm}
        return render(request, 'Article/create_article.html', context)
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.author = request.user
            new_article.title = form.cleaned_data['title']
            new_article.content = form.cleaned_data['content']
            new_article.document = form.cleaned_data['document']
            new_article.save()

            return redirect('start-page-switch')
           


        return render(request, 'Article/create_article.html', {})

class ArticleList(View):
    @allowed_roles(roles=['moderator', 'customer'])
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        context = { 'articles': articles }
        return render(request, 'Article/articles_table_page.html', context)

class ArticleView(View):
    @author_or_moder_only
    @allowed_roles(roles=['moderator', 'customer'])
    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        
        context = {'article': article}
        return render(request, 'Article/article_page.html', context)


def index(request) :
    return render(request, 'Article/create_article.html', {})
