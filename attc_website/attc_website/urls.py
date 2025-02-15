"""
URL configuration for attc_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from attc_app.views import index, membership, about, facilities, coaching, leagues, news, contact, gallery

urlpatterns = [
    path('', index, name='index'),
    path('membership/', membership, name='membership'),
    path('about/', about, name='about'),
    path('coaching/', coaching, name='coaching'),
    path('facilities/', facilities, name='facilities'),
    path('news/', news, name='news'),
    path('leagues/', leagues, name='leagues'),
    path('contact/', contact, name='contact'),
    path('gallery/', gallery, name='gallery'),
    path('admin/', admin.site.urls),
]
