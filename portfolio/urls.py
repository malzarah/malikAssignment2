from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),


    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),


    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),


    path('investment_list', views.investor_list, name='investment_list'),
    path('investment/create/', views.investor_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investor_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investor_delete, name='investment_delete'),

    url(r'^customers_json/', views.CustomerList.as_view()),
    url(r'^mutualfund/$', views.mutualfund_list, name='mutualfund_list'),
    url(r'^mutualfund/(?P<pk>\d+)/delete/$', views.mutualfund_delete, name='mutualfund_delete'),
    url(r'^mutualfund/(?P<pk>\d+)/edit/$', views.mutualfund_edit, name='mutualfund_edit'),
    url(r'^mutualfund/create/$', views.mutualfund_new, name='mutualfund_new'),

    url(r'^customers_json/', views.CustomerList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)