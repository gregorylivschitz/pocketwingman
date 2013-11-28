from django.conf.urls import patterns, url

from pocketwingman import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^/helpme$', views.HelpMeView.as_view(), name='helpme'),
    url(r'^/helpout$', views.HelpOutView.as_view(), name='helpout'),
    url(r'^/helpme/results/$', views.ResultsView.as_view(), name='help_me_results'),
    url(r'^/helpme/results/$', views.ResultsView.as_view(), name='help_out_results')

)