from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index, name='index'),
	url(r'^stat/$', views.stat, name='stat'),
	url(r'^customer/$', views.customer_info, name='customer_info'),
	url(r'^available_cars/$', views.available_cars, name='available_cars'),
]