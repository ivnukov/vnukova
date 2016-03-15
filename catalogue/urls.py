from django.conf.urls import url, patterns, include
from catalogue import views

urlpatterns = [
    url(r'^$', views.main, name  = "main" ),
    url(r'^(?P<section_id>[A-Z])/$',views.list_view, name = "list_view"),
#    url(r'^detail/(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name = "detail_view"),
 	url(r'^detail/(?P<pk>\d+)/$', views.product, name = "detail_view"),
	url(r'^add_to_cart/(?P<id>\d+)/$', views.add_to_cart , name='add_to_card'),
	url(r'^cart/$', views.cart, name='cart'),
	url(r'^del_from_cart/(?P<id>\d+)/$', views.del_from_cart , name='del'),
	url(r'^increase/(?P<id>\d+)/$', views.increase , name='increase'),
	url(r'^decrease/(?P<id>\d+)/$', views.decrease , name='decrease'),
	url(r'^order/$', views.order , name='order'),
]