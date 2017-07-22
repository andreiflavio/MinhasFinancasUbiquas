from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^classificacao/$', views.ClassificacaoListView.as_view(), name='classificacao_list'),
    url(r'classificacao/add/$', views.ClassificacaoCreate.as_view(), name='classificacao_add'),
    url(r'classificacao/(?P<pk>[0-9]+)/$', views.ClassificacaoUpdate.as_view(), name='classificacao_update'),
    url(r'classificacao/(?P<pk>[0-9]+)/delete/$', views.ClassificacaoDelete.as_view(), name='classificacao_delete'),
    url(r'^conta/$', views.ContaListView.as_view(), name='conta_list'),
    url(r'conta/add/$', views.ContaCreate.as_view(), name='conta_add'),
    url(r'conta/(?P<pk>[0-9]+)/$', views.ContaUpdate.as_view(), name='conta_update'),
    url(r'conta/(?P<pk>[0-9]+)/delete/$', views.ContaDelete.as_view(), name='conta_delete'),
    url(r'^cartaocredito/$', views.CartaoCreditoListView.as_view(), name='cartaocredito_list'),
    url(r'cartaocredito/add/$', views.CartaoCreditoCreate.as_view(), name='cartaocredito_add'),
    url(r'cartaocredito/(?P<pk>[0-9]+)/$', views.CartaoCreditoUpdate.as_view(), name='cartaocredito_update'),
    url(r'cartaocredito/(?P<pk>[0-9]+)/delete/$', views.CartaoCreditoDelete.as_view(), name='cartaocredito_delete'),
]