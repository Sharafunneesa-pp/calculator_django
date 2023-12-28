"""
URL configuration for calculatorproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from calc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',views.AdditionView.as_view(),name='addition'),
    path('sub/',views.SubtractionView.as_view(),name='subtraction'),
    path('mult/',views.MultiplicationView.as_view(),name='multiplication'),
    path('div/',views.DivisionView.as_view(),name='division'),
    path('fact/',views.FactorialView.as_view(),name='factorial'),
    path('',views.IndexView.as_view(),name='home'),



]
