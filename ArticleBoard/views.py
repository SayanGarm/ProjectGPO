from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.urls import reverse_lazy
from django.db.transaction import atomic

from .forms import ArticleForm, ReviewForm
from .models import Article, Review
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

            return redirect('article_info', pk = new_article.id)
           
        return render(request, 'Article/create_article.html', {})

class ArticleList(View):
    @allowed_roles(roles=['moderator', 'customer'])
    def get(self, request, *args, **kwargs):
        articles = Article.objects.getAllFromRole(request.user)
        context = { 'articles': articles }
        return render(request, 'Article/articles_table_page.html', context)

class ArticleView(View):
    @author_or_moder_only
    @allowed_roles(roles=['moderator', 'customer'])
    def get(self, request, pk):
        this_article = Article.objects.get(id=pk)
        is_moder = request.user.groups.filter(name='moderator').exists()
        reviews = Review.objects.filter(article=this_article)
        context = { 'article': this_article,
                    'is_moder': is_moder,
                    'reviews': reviews }
        return render(request, 'Article/article_page.html', context)
    @atomic
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        article = Article.objects.get(id=pk)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.author = request.user
            new_review.title = form.cleaned_data['title']
            new_review.content = form.cleaned_data['content']
            new_review.status = form.cleaned_data['status']
            new_review.article = Article.objects.get(id=pk)
            new_review.save()

            print(new_review.status)

            article.status = new_review.status
            print(article.save())

        return self.get(request, pk)

def index(request) :
    return render(request, 'Article/create_article.html', {})
