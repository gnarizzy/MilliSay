from django.conf.urls import patterns, url
from readwrite import views

urlpatterns = patterns('',
        url(r'^(?P<postid>\d+)/$', views.post_detail, name='post'),
        url(r'^all/$',views.post_list, name='post_list'),
        url(r'^$', views.index, name='index'),
        )