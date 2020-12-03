from django.http import HttpResponse
from django.shortcuts import redirect

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