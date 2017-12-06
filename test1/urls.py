"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from demo.views import queryprograms
from demo.views import querywares
from demo.views import search
from demo.views import querybundles
from demo.views import download

urlpatterns = [
    url(r'^admin/', admin.site.urls),   
    url(r'^querywares', querywares, name='demo.views.querywares'),
    url(r'^querybundles', querybundles, name='demo.views.querybundles'),
    url(r'^search', search, name='demo.views.search'),
    url(r'^download', download, name='demo.views.download'),
    url(r'^$', queryprograms, name='demo.views.queryprograms'),
]
