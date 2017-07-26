# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.product_list, name='produto_list'),
    #url para selecionar produtos pelo id da categoria
    #url(r'^([\d]+)/$',views.categoria_por_id, name='categoria_por_id'),
    #url para selecionar produtos pelo slug da categoria
    url(r'^(?P<slug>[\w_-]+)/$',views.categoria, name='categoria'),
    url(r'^produto/(?P<slug>[\w_-]+)/$', views.produto, name='produto'),

]