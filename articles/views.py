from django.shortcuts import render
from .models import Articles
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def articles_list(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})


def article_details(request, slug):
    # return HttpResponse(slug)
    article = Articles.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="accounts:login")
def articles_create(request):
    return render(request, 'articles/articles_create.html')

