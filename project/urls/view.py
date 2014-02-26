from django.conf.urls import patterns, url
from project.views import ListProjectView
from project.models import (Project,ProjectCategory,ProjectVersion,Milestone,
                            MilestoneStatus)
from project import tables as project_tables
urlpatterns = patterns('',

    url(r'^project/',
        ListProjectView.as_view(
            queryset=Project.objects.all(),
            model = Project,
            table = project_tables.ProjectTable,
            page_title='ITSY Projects',
            page_heading='Projects:'
        ),
        name='project'),

    url(r'^category/',
        ListProjectView.as_view(
            queryset=ProjectCategory.objects.all(),
            model = ProjectCategory,
            table = project_tables.ProjectCategoryTable,
            page_title='ITSY Project Categories',
            page_heading='Project Categories:'
        ),
        name='category'),

    url(r'^version/',
        ListProjectView.as_view(
            queryset=ProjectVersion.objects.all(),
            model = ProjectVersion,
            table = project_tables.ProjectVersionTable,
            page_title='ITSY Project Versions',
            page_heading='Project Versions:'
        ),
        name='version'),

    url(r'^milestone/',
        ListProjectView.as_view(
            queryset=Milestone.objects.all(),
            model = Milestone,
            table = project_tables.MilestoneTable,
            page_title='ITSY Milestones',
            page_heading='Milestones:'
        ),
        name='milestone'),

    url(r'^milestatus/',
        ListProjectView.as_view(
            queryset=MilestoneStatus.objects.all(),
            model = MilestoneStatus,
            table = project_tables.MilestoneStatusTable,
            page_title='ITSY Milestone Statuses',
            page_heading='Milestone Statuses:'
        ),    name='milestatus'),
)

