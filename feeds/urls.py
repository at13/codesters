from django.conf.urls import patterns, include, url

from feeds.views import *

urlpatterns = patterns('',
    url(r'^$', FeedListView.as_view(), name='feed_list'),
    url(r'^popular/$', FeedPopularListView.as_view(), name='feed_popular_list'),
    url(r'^type/(?P<slug>[-\w]+)/$', FeedTypeListView.as_view(), name='feed_type_list'),
    url(r'^tag/(?P<slug>[-\w]+)/$', FeedTagListView.as_view(), name='feed_tag_list'),
    url(r'^(?P<pk>\d+)/$', FeedDetailView.as_view(), name='feed_detail'),
    url(r'^new/$', FeedCreateView.as_view(), name='feed_create'),
)