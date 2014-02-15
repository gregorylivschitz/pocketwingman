from django.conf.urls import patterns, url

from pocketwingman import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^pocketwingman/help_me/$', views.help_me, name='help_me'),
    url(r'^pocketwingman/help_out/$', views.help_out, name='help_out'),
    url(r'^pocketwingman/help_me/(?P<category_id>\d+)/$', views.help_me_result, name='help_me_result'),
    url(r'^pocketwingman/help_out/(?P<category_id>\d+)/$', views.help_out_result, name='help_out_result'),
    url(r'^pocketwingman/help_me/(?P<category_id>\d+)/(?P<result_id>\d+)$', views.help_me_result_post, name='help_me_result_post'),
    url(r'^pocketwingman/register/$', views.register, name='register'),
    url(r'^pocketwingman/login/$', views.user_login, name='login'),
    url(r'^pocketwingman/restricted/', views.restricted, name='restricted'),
    url(r'^pocketwingman/logout/$', views.user_logout, name='logout'),
    url(r'^pocketwingman/hard_mode/$', views.hard_mode, name='hard_mode'),
    url(r"^pocketwingman/easy_mode/$", views.easy_mode, name='easy_mode'),
)