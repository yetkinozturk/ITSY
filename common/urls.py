from django.conf.urls import patterns, include, url
from common.views import UpdateSiteConfigView
from common.models import MainConfiguration

urlpatterns = patterns('',

    url(r'^',
        UpdateSiteConfigView.as_view(
            model=MainConfiguration,
            success_url='/',
        ),
        name='config'),
)
