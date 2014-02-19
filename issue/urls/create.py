from django.conf.urls import patterns, url

from issue.views import (CreateIssueView,CreateIssueTypeView,CreateIssueStatusView,
                         CreateIssuePriorityView,CreateIssueCharView,CreateIssueTextView,
                         CreateIssueImageView,CreateIssueFileView,CreateIssuePersonView,
                         CreateIssueFlowView,CreateIssueTemplateView)


urlpatterns = patterns('',
    url(r'^type/',       CreateIssueTypeView.as_view(),      name='type'),
    url(r'^status/',     CreateIssueStatusView.as_view(),    name='status'),
    url(r'^priority/',   CreateIssuePriorityView.as_view(),  name='priority'),
    url(r'^char/',       CreateIssueCharView.as_view(),      name='char'),
    url(r'^text/',       CreateIssueTextView.as_view(),      name='text'),
    url(r'^image/',      CreateIssueImageView.as_view(),     name='image'),
    url(r'^file/',       CreateIssueFileView.as_view(),      name='file'),
    url(r'^person/',     CreateIssuePersonView.as_view(),    name='person'),
    url(r'^flow/',       CreateIssueFlowView.as_view(),      name='flow'),
    url(r'^template/',   CreateIssueTemplateView.as_view(),  name='template'),
    url(r'^',            CreateIssueView.as_view(),          name='item'),
)