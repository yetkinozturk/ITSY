from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.shortcuts import get_object_or_404
class ListProjectView(ListView):
    page_title = ''
    page_heading = ''
    template_name = 'project/view/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListProjectView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class CreateProjectView(CreateView):
    page_title = ''
    page_heading = ''
    template_name = 'project/create/item.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class DeleteProjectItem(DeleteView):
    obj_id = -1
    page_title='ITSY Delete Project Item'
    page_heading='Delete Project Item:'
    template_name = 'project/create/delete.html'
    context_object_name = 'object'

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(DeleteProjectItem, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(DeleteProjectItem, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)

    def get_context_data(self, **kwargs):
        context = super(DeleteProjectItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context

class UpdateProjectItem(UpdateView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/edit/issuefield.html'
    obj_id = -1
    post_fix = ''

    def get_context_data(self, **kwargs):
        context = super(UpdateProjectItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        context['post_fix'] = self.post_fix
        return context

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateProjectItem, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateProjectItem, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)