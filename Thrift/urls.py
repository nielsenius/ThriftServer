from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^create_user/', 'ThriftServer.views.create_user'),
    
    url(r'^create_item/', 'ThriftServer.views.create_item'),
    url(r'^request_item/', 'ThriftServer.views.request_item'),
    url(r'^give_item/', 'ThriftServer.views.give_item'),
    
    url(r'^create_hashtag/', 'ThriftServer.views.create_hashtag'),
    
    url(r'^login/', 'ThriftServer.views.login')
)
