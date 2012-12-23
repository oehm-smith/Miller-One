from django.conf.urls import patterns, include, url

from Shopping.views import ItemList

urlpatterns = patterns('Shopping',
    url(r'^$', ItemList.as_view(), name='ItemList'),#'views.index'
#            url(r'^reports/items', ),

    url(r'^add/$', 'views.add', name='add'),
    url(r'^item/(?P<item_id>\d+)/$', 'views.item', name='item'),
    url(r'^item/(item/)+$', ItemList.as_view(), name='ItemList')    # ha ha!
)