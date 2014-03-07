from django.conf.urls import patterns, include, url
from repos.views import (RepoListView,RecentCommitsView, CodeBrowserView,
                         CommitDetailView)

urlpatterns = patterns('',
    url(r'^create/', include('repos.urls.create', namespace='create')),
    url(r'^view/', include('repos.urls.view', namespace='view')),
    url(r'^delete/', include('repos.urls.delete', namespace='delete')),
    url(r'^edit/', include('repos.urls.edit', namespace='edit')),
    url('^(?P<slug>[\w-]+)/$', RecentCommitsView.as_view(), name='recent_commits'),
    url('^(?P<slug>[\w-]+)/browser/(?P<path>.*)$', CodeBrowserView.as_view(), name='code_browser'),
    url('^(?P<slug>[\w-]+)/commit/(?P<commit_id>.*)/$', CommitDetailView.as_view(), name='commit_detail'),
    url('^',RepoListView.as_view(),name='repo_list')
)