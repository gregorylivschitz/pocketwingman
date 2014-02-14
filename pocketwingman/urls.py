from django.conf.urls import patterns, url

from pocketwingman import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^help_me/$', views.help_me, name='help_me'),
    url(r'^help_out/$', views.help_out, name='help_out'),
    url(r'^help_me/(?P<category_id>\d+)/$', views.help_me_result, name='help_me_result'),
    url(r'^help_out/(?P<category_id>\d+)/$', views.help_out_result, name='help_out_result'),
    url(r'^help_me/(?P<category_id>\d+)/(?P<result_id>\d+)$', views.help_me_result_post, name='help_me_result_post'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^hard_mode/$', views.hard_mode, name='hard_mode'),
    url(r'^easy_mode/$', views.easy_mode, name='easy_mode'),
)