from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse

from .models import Profile
from ArticleBoard.models import Article
from ArticleBoard.forms import ArticleListForm

def StartPageSwitch(request):
    groups = request.user.groups

    if (groups.exists()):
        if (groups.filter(name='moderator').exists()):
            return ModeratorPage.as_view()(request)
    else:
        return HttpResponse('Вы не имеете требуемой должности!')

    return UserPage.as_view()(request)

class UserPage(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        search_form = ArticleListForm(request.GET)
        search_form.is_valid()

        articles = Article.objects.filter(author=request.user)
        articles_count = {
            'A': articles.filter(status='A').count(),
            'B': articles.filter(status='B').count(),
            'C': articles.filter(status='C').count()
        }
        
        if search_form.cleaned_data['search']:
            articles = articles.filter(title=search_form.cleaned_data['search'])

        context = { 'profile': profile,
                    'articles': articles,
                    'articles_count': articles_count,
                    'search_form': search_form}

        return render(request, 'registration/user_home.html', context)

class ModeratorPage(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        context = { 'profile': profile }

        return render(request, 'registration/moderator_home.html', context)