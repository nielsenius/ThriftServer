from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^create_user/', 'ThriftServer.views.create_user'),
    url(r'^get_user/', 'ThriftServer.views.get_user'),
    
    url(r'^create_item/', 'ThriftServer.views.create_item'),
    url(r'^get_item/', 'ThriftServer.views.get_item'),
    url(r'^get_items/', 'ThriftServer.views.get_items'),
    url(r'^request_item/', 'ThriftServer.views.request_item'),
    url(r'^give_item/', 'ThriftServer.views.give_item'),
        
    url(r'^login/', 'ThriftServer.views.login'),
    
    url(r'^search/', 'ThriftServer.views.search'),
    
    url(r'^populate/', 'ThriftServer.views.populate')
)
