from django.conf.urls import patterns, include, url
from dashboard.views import MainDashboardView
from django.contrib import admin
from issue import urls as issue_urls
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', MainDashboardView.as_view(), name='home'),
    url(r'^issue/', include(issue_urls)),

    url(r'^admin/', include(admin.site.urls)),
)
