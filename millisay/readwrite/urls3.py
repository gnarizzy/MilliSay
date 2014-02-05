#another hideous file just for one clean URL. I feel so dirty. Don't look at me!
from django.conf.urls import patterns, url
from readwrite import views

urlpatterns = patterns('',
        url(r'^$', views.new, name='new'),
        )