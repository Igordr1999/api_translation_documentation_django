"""untitled67 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news import views
from api import views as api_views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from rest_framework import routers
from news import views
from news.views import BlogViewSet


router = routers.DefaultRouter()
router.register('blog', BlogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qqq/', views.my_view),
    path('article/<int:number>/', views.article),
    path('change/<code>/', views.change_lang),
    path('about/', views.about),
    path('api/', include(router.urls)),
    path('api/Blog.getAll/', views.getAll),
    path('api-auth/', include('rest_framework.urls')),

]
