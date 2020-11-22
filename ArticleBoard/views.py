from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def index(request) :
    return render(request, 'ArticleBoard/index.html', {})
