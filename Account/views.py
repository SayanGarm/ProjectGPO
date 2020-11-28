from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import Profile
from ArticleBoard.models import Article

class ProfileView(View):
    def get(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        articles = Article.objects.filter(author=request.user)

        context = { 'profile': profile,
                    'articles': articles}

        return render(request, 'registration/profile.html', context)
