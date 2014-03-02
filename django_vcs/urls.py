from django.conf.urls import patterns, url

urlpatterns = patterns('django_vcs.views',
    url('^$', 'repo_list', name='repo_list'),
    url('^(?P<slug>[\w-]+)/$', 'recent_commits', name='recent_commits'),
    url('^(?P<slug>[\w-]+)/browser/(?P<path>.*)$', 'code_browser', name='code_browser'),
    url('^(?P<slug>[\w-]+)/commit/(?P<commit_id>.*)/$', 'commit_detail', name='commit_detail'),
)
