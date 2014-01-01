from django.conf.urls import patterns, url

urlpatterns = patterns('frontend.views',
                       url(r'^$', 'index'),
                       url(r'^about/$', 'about'),
                       url(r'^check/$', 'check'),
                       )