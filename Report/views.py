from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.urls import reverse_lazy

from docxtpl import DocxTemplate
from docx import Document
from Account.models import Profile

class UserList(View):
    def get(self, request, *args, **kwargs):
           
            doc = DocxTemplate('templates/a.docx')
            context = { 'emitent' : 'ООО Ромашка', 
                        'address1' : 'г. Москва, ул. Долгоруковская, д. 0',
                        'участник': 'ООО Участник', 
                        'адрес_участника': 'г. Москва, ул. Полевая, д. 0', 
                        'director': 'И.И. Иванов'}
            doc.render(context)
            doc.save("templ-final.docx")
            return HttpResponse("ok")