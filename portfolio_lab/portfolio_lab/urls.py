"""portfolio_lab URL Configuration

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
from django.urls import path
from portfolio_lab import settings
from django.conf.urls.static import static
from into_good_hands.views import IndexView, FormView, Login, Register, Profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', IndexView.as_view(), name='index'),
    path('form/', FormView.as_view(), name='form'),
    path('login', Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('profil/', Profile.as_view(), name='profil'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
