# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('about/', views.about),
    path('', views.articles_list, name="list"),
    path('create/', views.articles_create, name="create"),
    path('<slug:slug>/', views.article_details, name="detail"),
]
