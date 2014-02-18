from django.conf.urls import patterns, include, url

from issue.views import CreateIssueView

urlpatterns = patterns('',
    #url(r'^$', MainDashboardView.as_view(), name='home'),
    url(r'^create/', CreateIssueView.as_view(),name='create_issue'),
)
