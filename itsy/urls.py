from django.conf.urls import patterns, include, url
from dashboard.views import MainDashboardView
from django.contrib import admin
from django.views.generic import RedirectView


admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', MainDashboardView.as_view(), name='home'),
    url(r'^issue/', include('issue.routes', namespace='issue')),
    url(r'^project/', include('project.routes', namespace='project')),
    url(r'^account/', include('account.routes',namespace='account')),
    url(r'^search/', include('haystack.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
