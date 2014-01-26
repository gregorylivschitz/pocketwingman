from django.conf.urls import patterns, url

from pocketwingman import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category_id>\d+)/$', views.help_me, name='help_me'),
    url(r'^help_out/(?P<category_id>\d+)/$', views.help_out, name='help_out'),
#    url(r'^$', views.IndexView.as_view(), name='index')
#    url(r'^/helpme$', views.HelpMeView.as_view(), name='helpme'),
#    url(r'^/helpout$', views.HelpOutView.as_view(), name='helpout'),
#    url(r'^/helpme/results/$', views.ResultsView.as_view(), name='help_me_results'),
#    url(r'^/helpme/results/$', views.ResultsView.as_view(), name='help_out_results')

)