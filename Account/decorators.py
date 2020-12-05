from django.http import HttpResponse
from django.shortcuts import redirect

from ArticleBoard.models import Article

def allowed_roles(roles=[]):
    def decorator(view_func):
        def wrapper_func(self, request, *args, **kwargs):
            groups = request.user.groups
    
            if (groups.exists()):
                for role in roles:
                    if (groups.filter(name=role).exists()):
                        return view_func(self, request, *args, **kwargs)
            
            return HttpResponse('Вы не имеете требуемой должности!')      
        return wrapper_func
    return decorator

def author_or_moder_only(view_func):
    def wrapper_function(self, request, pk):
        MODERATOR = 'moderator'
        groups = request.user.groups
        article = Article.objects.get(id = pk)
        if (groups.exists()):
            if (groups.filter(name=MODERATOR).exists()):
                return view_func(self, request, pk)
            elif (article.author == request.user):
                return view_func(self, request, pk)
            else:
                return HttpResponse('Вы не имеете требуемой должности!')      
        else:
            return HttpResponse('Вы не имеете требуемой должности!')      

    return wrapper_function