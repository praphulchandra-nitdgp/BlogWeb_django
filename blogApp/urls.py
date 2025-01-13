from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='blog-index'),
    # path('about/', views.about, name='blog-about'),
]
