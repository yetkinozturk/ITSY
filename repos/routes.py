from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^create/', include('repos.urls.create', namespace='create')),
    url(r'^view/', include('repos.urls.view', namespace='view')),
    url(r'^delete/', include('repos.urls.delete', namespace='delete')),
    url(r'^edit/', include('repos.urls.edit', namespace='edit')),
)