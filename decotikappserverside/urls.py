"""
URL configuration for decotikappserverside project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from prices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kplus/', views.get_prices, name='prices'),
    path('042/', views.get_prices042, name='042'),
    path('046/', views.get_prices046, name='046'),
    path('048/', views.get_prices048, name='048'),
    path('055/', views.get_prices055, name='055'),
    path('058/', views.get_prices058, name='058')
]
