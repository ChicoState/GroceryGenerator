"""grocery_gen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from grocery_gen_app.views import *

urlpatterns = [
	path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('recipe/<int:recipe_id>/', recipe_view, name='recipe'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register_user, name='register'),
    path('search/', search, name='search'),
    path('favorites/<int:recipe_id>/', favorites_view, name='favorites'),
    path('favorites/', favorites_view, name='favorites'),
    path('similar/<int:recipe_id>/', similar, name='similar'),
]
