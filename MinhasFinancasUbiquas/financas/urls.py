from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^classificacao/$', views.ClassificacaoListView.as_view(), name='classificacao_list'),
    url(r'classificacao/add/$', views.ClassificacaoCreate.as_view(), name='classificacao_add'),
    url(r'classificacao/(?P<pk>[0-9]+)/$', views.ClassificacaoUpdate.as_view(), name='classificacao_update'),
    url(r'classificacao/(?P<pk>[0-9]+)/delete/$', views.ClassificacaoDelete.as_view(), name='classificacao_delete')
]