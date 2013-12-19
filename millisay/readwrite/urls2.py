from django.conf.urls import patterns, url
from readwrite import views
#This is pretty bad design, but it's the only way to get a clean submit url without making a whole new app
urlpatterns = patterns('',
        url(r'^$', views.submit_post, name='submit'),
        )