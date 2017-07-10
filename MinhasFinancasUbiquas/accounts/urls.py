from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from MinhasFinancasUbiquas.accounts import views

urlpatterns = [
    url(r'^$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^cadastre-se/$', views.register, name='register'),           
   	url(r'^nova-senha/$', views.password_reset, name='password_reset'),
]