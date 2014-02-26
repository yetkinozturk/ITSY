from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^create/', include('project.urls.create', namespace='create')),
    url(r'^view/', include('project.urls.view', namespace='view')),
    url(r'^edit/', include('project.urls.edit', namespace='edit')),
    url(r'^delete/', include('project.urls.delete', namespace='delete')),
)
