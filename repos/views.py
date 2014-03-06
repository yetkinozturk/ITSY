from django.shortcuts import get_object_or_404
from common.views import (LoginRequiredCreateView,LoginRequiredListView,
                          LoginRequiredUpdateView,LoginRequiredDeleteView)
from django_tables2 import RequestConfig


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
        RequestConfig(self.request).configure(tb)
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