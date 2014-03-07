from django.conf.urls import patterns, url
from repos.views import DeleteRepoItem
from repos.models import CodeRepository

urlpatterns = patterns('',

    url(r'^repos/(?P<id>\w+)/',
        DeleteRepoItem.as_view(
            model=CodeRepository,
            success_url='/repos/view/repos/',
            page_title='ITSY Delete Code Repo',
            page_heading='Delete Code Repository:'
        ),
        name='repos'),
)