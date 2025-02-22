"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # www.xxx  -> 函数
    path('index/', views.index),

    path('list/', views.user_list),

    path('add/', views.user_add),

    path('tpl/',views.tpl),

    path('news/',views.news),

    #请求和响应
    path("something/",views.something),

    #用户登录
    path("login/",views.login),

    path("orm/",views.orm),

    #案例 用户管理
    path("info/",views.info),
    path("infoAdd",views.infoAdd),
    path("infoDelete",views.infoDelete),


]
