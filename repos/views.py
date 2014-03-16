import os
from django.shortcuts import get_object_or_404
from django.http import Http404
from common.views import (LoginRequiredCreateView,LoginRequiredListView,
                          LoginRequiredUpdateView,LoginRequiredDeleteView,
                          LoginRequiredTemplateView)
from django_tables2 import RequestConfig
from repos.models import CodeRepository


class CreateRepoView(LoginRequiredCreateView):
    page_title = ''
    page_heading = ''
    template_name = 'repos/create/item.html'

    def get_context_data(self, **kwargs):
        context = super(CreateRepoView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class ListRepoView(LoginRequiredListView):
    page_title = ''
    page_heading = ''
    template_name = 'repos/view/list.html'
    model = None
    table = None

    def get_context_data(self, **kwargs):
        context = super(ListRepoView, self).get_context_data(**kwargs)
        tb = self.table(self.model.objects.all())
        RequestConfig(self.request, paginate={"per_page": 15}).configure(tb)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        context['object_list'] = tb
        return context


class UpdateRepoItem(LoginRequiredUpdateView):
    page_title = ''
    page_heading = ''
    template_name = 'repos/edit/item.html'
    obj_id = -1

    def get_context_data(self, **kwargs):
        context = super(UpdateRepoItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateRepoItem, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateRepoItem, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)


class DeleteRepoItem(LoginRequiredDeleteView):
    obj_id = -1
    page_title='ITSY Delete a Code Repo'
    page_heading='Delete Code Repository:'
    template_name = 'repos/delete/item.html'
    context_object_name = 'object'

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(DeleteRepoItem, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(DeleteRepoItem, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)

    def get_context_data(self, **kwargs):
        context = super(DeleteRepoItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class RepoListView(LoginRequiredListView):
    queryset = CodeRepository.objects.all()
    template_name = 'repos/repo_list.html'
    context_object_name = 'repos'


class RecentCommitsView(LoginRequiredTemplateView):
    template_name = 'repos/recent_commits.html'
    page_title = ''
    page_heading = ''
    slug = ''

    def get_context_data(self, **kwargs):
        context = super(RecentCommitsView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        repo = get_object_or_404(CodeRepository, slug=self.slug)
        context['repo'] = repo
        context['commits'] = repo.get_recent_commits()
        return context

    def get(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        return super(RecentCommitsView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        return super(RecentCommitsView, self).post(request, *args, **kwargs)


class CodeBrowserView(LoginRequiredTemplateView):
    template_name = 'repos/file_contents.html'
    slug = ''
    path = ''
    page_title = ''
    page_heading = ''
    is_folder_view = True

    def get(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        self.path = kwargs.get('path')
        return super(CodeBrowserView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        self.path = kwargs.get('path')
        return super(CodeBrowserView, self).post(request, *args, **kwargs)

    def get_template_names(self):
        if self.is_folder_view:
            return 'repos/folder_contents.html'
        else:
            return 'repos/file_contents.html'

    def get_context_data(self, **kwargs):
        context = super(CodeBrowserView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        repo = get_object_or_404(CodeRepository, slug=self.slug)
        context['repo'] = repo
        context['path'] = self.path
        rev = self.request.GET.get('rev') or None
        file_contents = repo.get_file_contents(self.path, rev)
        if file_contents is None:
            folder_contents = repo.get_folder_contents(self.path, rev)
            if folder_contents is None:
                raise Http404
            self.is_folder_view = True
            context['files'], context['folders'] = folder_contents
            context['files'] = [(os.path.join(self.path, o), o) for o in context['files']]
            context['folders'] = [(os.path.join(self.path, o), o) for o in context['folders']]
            return context
        self.is_folder_view = False
        context['file'] = file_contents
        return context


class CommitDetailView(LoginRequiredTemplateView):
    template_name = 'repos/commit_detail.html'
    page_title = ''
    page_heading = ''
    slug = ''
    commit_id = ''

    def get_context_data(self, **kwargs):
        context = super(CommitDetailView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        repo = get_object_or_404(CodeRepository, slug=self.slug)
        commit = repo.get_commit(self.commit_id)
        if commit is None:
            raise Http404
        context['repo'] = repo
        context['commit'] = commit
        return context

    def get(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        self.commit_id = kwargs.get('commit_id')
        return super(CommitDetailView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        self.commit_id = kwargs.get('commit_id')
        return super(CommitDetailView, self).post(request, *args, **kwargs)
