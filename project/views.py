from django.shortcuts import get_object_or_404
from django_tables2   import RequestConfig
import autocomplete_light
from ckeditor.widgets import CKEditorWidget
from common.views import (LoginRequiredListView,LoginRequiredCreateView,
                          LoginRequiredDeleteView,LoginRequiredUpdateView)


class ListProjectView(LoginRequiredListView):
    page_title = ''
    page_heading = ''
    template_name = 'project/view/list.html'
    model = None
    table = None

    def get_context_data(self, **kwargs):
        context = super(ListProjectView, self).get_context_data(**kwargs)
        tb = self.table(self.model.objects.all())
        RequestConfig(self.request, paginate={"per_page": 25}).configure(tb)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        context['object_list'] = tb
        return context


class CreateProjectView(LoginRequiredCreateView):
    page_title = ''
    page_heading = ''
    template_name = 'project/create/item.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProjectView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context

    def get_form_class(self,*args,**kwargs):
        form = autocomplete_light.modelform_factory(self.model)
        #raise Exception(dir(form))
        if 'summary' in form.base_fields:
            form.base_fields['summary'].widget = CKEditorWidget()
        return form

class DeleteProjectItem(LoginRequiredDeleteView):
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

class UpdateProjectItem(LoginRequiredUpdateView):
    page_title = ''
    page_heading = ''
    template_name = 'project/edit/item.html'
    obj_id = -1
    post_fix = ''

    def get_context_data(self, **kwargs):
        context = super(UpdateProjectItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        context['post_fix'] = self.post_fix
        return context

    def get_form_class(self,**kwargs):
        return autocomplete_light.modelform_factory(self.model)

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateProjectItem, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateProjectItem, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)