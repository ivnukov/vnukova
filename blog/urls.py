from django.conf.urls import url, patterns, include
from blog import views

urlpatterns = [
    url(r'^$', views.blog, name  = "blog" )
    ]