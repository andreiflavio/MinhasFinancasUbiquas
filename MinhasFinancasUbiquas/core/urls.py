from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pessoa/$', views.PessoaListView.as_view(), name='pessoa_list'),
    url(r'pessoa/add/$', views.PessoaCreate.as_view(), name='pessoa_add'),
    url(r'pessoa/(?P<pk>[0-9]+)/$', views.PessoaUpdate.as_view(), name='pessoa_update'),
    url(r'pessoa/(?P<pk>[0-9]+)/delete/$', views.PessoaDelete.as_view(), name='pessoa_delete'),
]