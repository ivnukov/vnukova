from django.conf.urls import url, patterns, include
from catalogue import views

urlpatterns = [
    url(r'^$', views.main, name  = "main" ),
    url(r'^(?P<section_id>[A-Z])/$',views.list_view, name = "list_view"),
  #  url(r'^detail/(?P<pk>\d+)/$', views.ItemDetailView.as_view(), name = "detail_view"),
 	url(r'^detail/(?P<pk>\d+)/$', views.show_product, name = "detail_view"),
       
]