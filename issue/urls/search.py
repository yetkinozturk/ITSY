from django.conf.urls import patterns, url
from issue.views import IssueSearch,IssueAdvancedSearch

urlpatterns = patterns('',

    url(r'^simple/',
        IssueSearch.as_view(),
        name='simple'),

    url(r'^advanced/',
        IssueAdvancedSearch.as_view(),
        name='advanced'),
)
