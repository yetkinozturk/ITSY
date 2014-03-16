from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django_tables2 import RequestConfig
from common.views import (LoginRequiredCreateView,AuthorizationRequiredMixin,
                          LoginRequiredListView,LoginRequiredDeleteView,
                          LoginRequiredUpdateView)
from account.forms import UserCreationForm,UpdateAccountForm,CreateAccountForm


class RegistrationView(CreateView):
    form_class = UserCreationForm
    template_name = 'account/register.html'


class UpdateUser(UpdateView):
    pass


class CreateAccountItem(AuthorizationRequiredMixin, LoginRequiredCreateView):
    page_title = ''
    page_heading = ''
    template_name = 'account/create/item.html'
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(CreateAccountItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class CreateAccountView(AuthorizationRequiredMixin, LoginRequiredCreateView):
    page_title = ''
    page_heading = ''
    template_name = 'account/create/item.html'
    raise_exception = True
    form_class = CreateAccountForm

    def get_context_data(self, **kwargs):
        context = super(CreateAccountView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class ListAccountView(AuthorizationRequiredMixin, LoginRequiredListView):
    page_title = ''
    page_heading = ''
    template_name = 'account/view/list.html'
    model = None
    table = None
    raise_exception = True

    def get_context_data(self, **kwargs):
        context = super(ListAccountView, self).get_context_data(**kwargs)
        tb = self.table(self.model.objects.all())
        RequestConfig(self.request, paginate={"per_page": 15}).configure(tb)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        context['object_list'] = tb
        return context


class DeleteAccountItem(LoginRequiredDeleteView):  # it's also authorization req
    obj_id = -1
    page_title='ITSY Delete an Account'
    page_heading='Delete an Account:'
    template_name = 'account/delete/item.html'
    context_object_name = 'object'

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(DeleteAccountItem, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(DeleteAccountItem, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)

    def get_context_data(self, **kwargs):
        context = super(DeleteAccountItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class UpdateAccountItem(AuthorizationRequiredMixin,LoginRequiredUpdateView):
    page_title = ''
    page_heading = ''
    template_name = 'account/edit/item.html'
    obj_id = -1
    post_fix = ''

    def get_context_data(self, **kwargs):
        context = super(UpdateAccountItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        context['post_fix'] = self.post_fix
        return context

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateAccountItem, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateAccountItem, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)


class UpdateAccount(AuthorizationRequiredMixin,LoginRequiredUpdateView):
    page_title = ''
    page_heading = ''
    template_name = 'account/edit/item.html'
    obj_id = -1
    post_fix = ''
    form_class = UpdateAccountForm

    def get_context_data(self, **kwargs):
        context = super(UpdateAccount, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        context['post_fix'] = self.post_fix
        return context

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateAccount, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateAccount, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)