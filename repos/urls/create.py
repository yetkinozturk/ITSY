from django.conf.urls import patterns, url
from repos.models import CodeRepository
from repos.views import CreateRepoView

urlpatterns = patterns('',
    url(r'^repos',
        CreateRepoView.as_view(
            model=CodeRepository,
            success_url='/repos/view/repos/',
            page_title = 'Add a Repo',
            page_heading = 'Add a Code Repository',
        ),
        name='repos'),
)