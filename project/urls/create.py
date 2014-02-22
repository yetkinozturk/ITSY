from django.conf.urls import patterns, url
from project.views import CreateProjectView
from project.models import (Project,ProjectCategory,ProjectVersion,Milestone,
                            MilestoneStatus)

urlpatterns = patterns('',

    url(r'^project/',
        CreateProjectView.as_view(
            model=Project,
            success_url='/project/view/project/',
            page_title='ITSY Create Project',
            page_heading='Create a Project:'
        ),
        name='project'),

    url(r'^category/',
        CreateProjectView.as_view(
            model=ProjectCategory,
            success_url='/project/view/category/',
            page_title='ITSY Create Project Category',
            page_heading='Create a Project Category:'
        ),
        name='category'),

    url(r'^version/',
        CreateProjectView.as_view(
            model=ProjectVersion,
            success_url='/project/view/version/',
            page_title='ITSY Create Project Version',
            page_heading='Create a Project Version:'
        ),
        name='version'),

    url(r'^milestone/',
        CreateProjectView.as_view(
            model=Milestone,
            success_url='/project/view/milestone/',
            page_title='ITSY Create Milestone',
            page_heading='Create a Milestone:'
        ),
        name='milestone'),

    url(r'^milestatus/',
        CreateProjectView.as_view(
            model=MilestoneStatus,
            success_url='/project/view/milestatus/',
            page_title='ITSY Create Milestone Status',
            page_heading='Create a Milestone Status'
        ),
        name='milestatus'),
)