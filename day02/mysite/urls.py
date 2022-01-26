"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #https://127.0.0.1:8000/page/2003/
    path('page/2003/',views.page_2003_view),
    path('',views.index_view),
    #127.0.0.1:8000/n/op/m
    re_path(r'^(?P<x>\d{1,2})/(?P<op>\w+)/(?P<y>\d{1,2})',views.cal2_view),
    path('<int:n>/<str:op>/<int:m>',views.cal_view),
    path('test_request',views.test_request),
    path('test_get_post',views.test_get_post),
    path('test_html',views.test_html)
    

    
]
