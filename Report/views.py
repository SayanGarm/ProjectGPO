from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.urls import reverse_lazy

from docxtpl import DocxTemplate
from Account.models import Profile
from ArticleBoard.models import Article
from django.contrib.auth.models import User


class UserList(View):
    def get(self, request, *args, **kwargs):
            doc = DocxTemplate("Report/templates/шаблон.docx")

            users = Profile.objects.get_customers()
            for user in users:
                user.articles = Article.objects.filter(author = user.user)

            context = { 'users': users }
            doc.render(context)
            doc.save("отчет.docx")
            return HttpResponse("ok")