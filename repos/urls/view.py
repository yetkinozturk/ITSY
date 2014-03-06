from django.conf.urls import patterns, url
from django_vcs.models import CodeRepository
from repos.views import ListRepoView
from repos.tables import RepoTable


urlpatterns = patterns('',
    url(r'^repos',
        ListRepoView.as_view(
            queryset=CodeRepository.objects.all(),
            model=CodeRepository,
            table=RepoTable,
            page_title = 'Code Repositories',
            page_heading = 'Code Repositories:',
        ),
        name='repos'),
)