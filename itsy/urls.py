from django.conf.urls import patterns, include, url
from dashboard.views import MainDashboardView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', MainDashboardView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
