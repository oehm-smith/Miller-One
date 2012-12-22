from django.conf.urls import patterns, include, url


urlpatterns = patterns('Shopping',
    url(r'^$', 'views.index', name='index'),
    url(r'^add/$', 'views.add', name='add'),
    url(r'^item/(?P<item_id>\d+)/$', 'views.item', name='item'),
)