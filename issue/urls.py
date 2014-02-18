from django.conf.urls import patterns, include, url

from issue.views import (CreateIssueView,CreateIssueTypeView,CreateIssueStatusView,
                         CreateIssuePriorityView,CreateIssueCharView,CreateIssueTextView,
                         CreateIssueImageView,CreateIssueFileView,CreateIssuePersonView,
                         CreateIssueFlowView,CreateIssueTemplateView)

urlpatterns = patterns('',
    #url(r'^$', MainDashboardView.as_view(), name='home'),
    url(r'^create/', CreateIssueView.as_view(),name='create_issue'),
    url(r'^createissuetype/', CreateIssueTypeView.as_view(),name='create_issue'),
    url(r'^createissuestatus/', CreateIssueStatusView.as_view(),name='create_issue'),
    url(r'^createissuepriority/', CreateIssuePriorityView.as_view(),name='create_issue'),
    url(r'^createissuechar/', CreateIssueCharView.as_view(),name='create_issue'),
    url(r'^createissuetext/', CreateIssueTextView.as_view(),name='create_issue'),
    url(r'^createissueimage/', CreateIssueImageView.as_view(),name='create_issue'),
    url(r'^createissuefile/', CreateIssueFileView.as_view(),name='create_issue'),
    url(r'^createissueperson/', CreateIssuePersonView.as_view(),name='create_issue'),
    url(r'^createissueflow/', CreateIssueFlowView.as_view(),name='create_issue'),
    url(r'^createissuetemplate/', CreateIssueTemplateView.as_view(),name='create_issue'),
)
