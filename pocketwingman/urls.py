from django.conf.urls import patterns, url

from pocketwingman import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_id>\d+)/$', views.help_me, name='help_me'),
    url(r'^help_out/(?P<category_id>\d+)/$', views.help_out, name='help_out'),

)