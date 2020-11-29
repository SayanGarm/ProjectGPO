from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Profile
from ArticleBoard.models import Article
from ArticleBoard.forms import ArticleListForm

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        form = ArticleListForm(request.GET)
        form.is_valid()

        articles = Article.objects.filter(author=request.user)
        if form.cleaned_data['search']:
            articles = articles.filter(title=form.cleaned_data['search'])

        context = { 'profile': profile,
                    'articles': articles,
                    'articles_count': articles.count(),
                    'form': form}

        return render(request, 'registration/profile.html', context)
