from django.conf.urls import patterns, url
from readwrite import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
