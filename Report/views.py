from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.urls import reverse_lazy

from docxtpl import DocxTemplate
from Account.models import Profile
from Account.decorators import allowed_roles
from ArticleBoard.models import Article
from django.contrib.auth.models import User

from datetime import datetime, time


class UserList(View):
    @allowed_roles(roles = ['moderator'])
    def get(self, request, *args, **kwargs):
            doc = DocxTemplate("Report/templates/шаблон.docx")

            users = Profile.objects.get_customers()
            for user in users:
                user.articles = Article.objects.filter(author = user.user)

            context = { 'users': users }
            doc.render(context)

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=Otchet_'+ str(datetime.now())+'.docx'
            doc.save(response)
            return response
