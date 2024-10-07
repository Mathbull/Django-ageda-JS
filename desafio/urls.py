"""
URL configuration for desafio project.

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
from django.urls import path, re_path
from django.views.generic import RedirectView
from core import views
from django.conf import settings

from django.views.static import serve

urlpatterns = [

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),


    path('', RedirectView.as_view(url='/agenda')),

    path('admin/', admin.site.urls),

    path('login/', views.login_user),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user),
   # path('login_2/', views.login_user_2),

    path('register/', views.register_user),
    path('register/submit', views.register_user_submit),


    path('agenda/', views.lista_eventos_2),

    path('agenda_2/', views.lista_eventos_2),

    path('agenda/eventos/', views.new_evento),

    path('agenda/eventos/submit', views.new_evento_submit),

    path('agenda/eventos/delete/<int:id_evento>/', views.delete_evento),
    
]
