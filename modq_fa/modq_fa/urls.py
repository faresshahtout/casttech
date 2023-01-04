"""modq_fa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from users.views import register_request as std_hp
from users.views import logout_request as stdlg
from CastsTypes.views import request_view as request
from CastsTypes.views import upload_file as requestu
from CastsTypes.views import choose as requestc

urlpatterns = [
    path('', std_hp),
    path('', std_hp,name='home'),
    path('logout/', stdlg),
    path('admin/', admin.site.urls),
    path('order/', request,name='request_a_cast'),
    path('upload/', requestu,name='uploadACsv'),
    path('choose/', requestc,name='choose')


]
