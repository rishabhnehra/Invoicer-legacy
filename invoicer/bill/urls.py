from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
	url(r'^$', views.dashboard , name='dashboard'),
	url(r'^(?P<id>[0-9]+)/', views.detail, name='summary'),
	url(r'^new/$', views.new_bill, name='new'),
	url(r'^new/products/(?P<id>[0-9]+)/$', views.products, name='products'),
	url(r'^history/$', views.history, name='history'),
]