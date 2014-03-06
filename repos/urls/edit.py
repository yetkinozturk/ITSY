from django.conf.urls import patterns, url
from repos.views import UpdateRepoItem
from django_vcs.models import CodeRepository

urlpatterns = patterns('',

    url(r'^repos/(?P<id>\w+)/',
        UpdateRepoItem.as_view(
            model=CodeRepository,
            success_url='/repos/view/repos/',
            page_title='ITSY Edit Code Repository',
            page_heading='Edit Code Repository:'
        ),
        name='repos'),
)