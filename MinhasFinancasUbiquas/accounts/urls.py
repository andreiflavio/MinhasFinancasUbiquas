from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from MinhasFinancasUbiquas.accounts import views

urlpatterns = [
    url(r'^$', auth_views.login,
        {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', auth_views.logout, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^cadastre-se/$', views.register, name='register'),           
   	url(r'^nova-senha/$', views.password_reset, name='password_reset'),
    url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^editar/$', views.edit, name='edit'),
    url(r'^editar-senha/$', views.edit_password, name='edit_password'),
    url(r'^desativar_conta/$', views.desativar_conta, name='desativar_conta'),
]