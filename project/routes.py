from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^create/', include('project.urls.create', namespace='create')),
    url(r'^view/', include('project.urls.view', namespace='view')),
)
