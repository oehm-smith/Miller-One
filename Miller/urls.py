from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'Miller.views.home', name='shhome'),
    url(r'^reports/', include('Shopping.urls')), # 'Shopping.views.add'),
)

urlpatterns += patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^shopping/', include(admin.site.urls)),
)
