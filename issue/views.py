from django.shortcuts import get_object_or_404
from django import forms
from haystack.forms import SearchForm
from haystack.query import SearchQuerySet
from django_tables2 import RequestConfig
from issue.models import (Issue, IssueCharValue, IssueTextValue, IssueImageValue,
                          IssueFileValue, IssuePersonValue, IssueDateValue,
                          IssueBoolValue, IssueChoiceValue)
from account.models import Account
from common.views import (LoginRequiredListView,LoginRequiredCreateView,
                          LoginRequiredDeleteView,LoginRequiredUpdateView,
                          LoginRequiredTemplateView)


class CreateIssueDetailsForm(forms.ModelForm):
    """
    This form is displayed in the second step of issue create.
    init method is overriden to add fields from the selected issue template
    save method is overriden to save related objects.
    """
    original_fields = {}
    field_value_class = {}
    field_type_instance = {}
    class Meta:
        model = Issue

    def __init__(self, *args, **kwargs):
        super(CreateIssueDetailsForm, self).__init__(*args, **kwargs)
        issue = kwargs.get('instance', None)

        if issue:
            self.fields.pop('effort_calc')
            self.fields.pop('template')
            self.original_fields = self.fields.copy()

            if issue.template:

                char_fields = issue.template.char_fields.all()
                for field in char_fields:
                    self.fields[field.name] = forms.CharField(max_length=255, required=field.required)
                    self.field_value_class[field.name] = IssueCharValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueCharValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueCharValue.DoesNotExist:
                        pass

                text_fields = issue.template.text_fields.all()
                for field in text_fields:
                    self.fields[field.name] = forms.CharField(widget=forms.Textarea, required=field.required)
                    self.field_value_class[field.name] = IssueTextValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueTextValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueTextValue.DoesNotExist:
                        pass

                bool_fields = issue.template.bool_fields.all()
                for field in bool_fields:
                    self.fields[field.name] = forms.BooleanField(required=False)
                    self.field_value_class[field.name] = IssueBoolValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueBoolValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueBoolValue.DoesNotExist:
                        pass

                choice_fields = issue.template.choice_fields.all()
                for field in choice_fields:
                    self.fields[field.name] = forms.ChoiceField(choices=[ (str(i), str(i)) for i in field.choices.split(',')],required=field.required)
                    self.field_value_class[field.name] = IssueChoiceValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueChoiceValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueChoiceValue.DoesNotExist:
                        pass

                date_fields = issue.template.date_fields.all()
                for field in date_fields:
                    self.fields[field.name] = forms.DateTimeField(required=field.required)
                    self.field_value_class[field.name] = IssueDateValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueDateValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueDateValue.DoesNotExist:
                        pass

                image_fields = issue.template.image_fields.all()
                for field in image_fields:
                    self.fields[field.name] = forms.ImageField(required=field.required)
                    self.field_value_class[field.name] = IssueImageValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueImageValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueImageValue.DoesNotExist:
                        pass

                file_fields = issue.template.file_fields.all()
                for field in file_fields:
                    self.fields[field.name] = forms.FileField(required=field.required)
                    self.field_value_class[field.name] = IssueFileValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueFileValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueFileValue.DoesNotExist:
                        pass

                people = issue.template.people.all()
                for field in people:
                    self.fields[field.role] = forms.ModelChoiceField(queryset=Account.objects.all(),required=field.required)
                    self.field_value_class[field.role] = IssuePersonValue
                    self.field_type_instance[field.role] = field
                    try:
                        item = IssuePersonValue.objects.get(issue=issue,field=field)
                        self.fields[field.role].initial = item.value
                    except IssuePersonValue.DoesNotExist:
                        pass

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(CreateIssueDetailsForm, self).save(commit=False)
        if commit:
            m.save()
        if len(self.field_value_class) > 0:
            for k,v in self.original_fields.iteritems():
                self.cleaned_data.pop(k)
        for k,v in self.cleaned_data.iteritems():
            if self.field_value_class:
                item,created = self.field_value_class[k].objects.get_or_create(
                    issue=m,
                    field=self.field_type_instance.get(k))
                item.value = self.cleaned_data.get(k)
                item.save()
        return m


class CreateIssueDetails(LoginRequiredUpdateView):
    slug = ''
    context_object_name = 'issue'
    form_class = CreateIssueDetailsForm

    def get(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        return super(CreateIssueDetails, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        return super(CreateIssueDetails, self).post(request, *args, **kwargs)

    def get_object(self):
        issue = get_object_or_404(Issue, slug=self.slug)
        issue.reporter = self.request.user.id
        issue.save()
        return issue


class CreateIssueView(LoginRequiredCreateView):

    def get_success_url(self):
        return '/issue/create/details/%s/' % self.object.slug


class CreateIssueFlow(LoginRequiredCreateView):
    pass


class CreateIssueField(LoginRequiredCreateView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/create/issuefield.html'

    def get_context_data(self, **kwargs):
        context = super(CreateIssueField, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class UpdateIssueField(LoginRequiredUpdateView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/edit/issuefield.html'
    obj_id = -1
    post_fix = ''

    def get_context_data(self, **kwargs):
        context = super(UpdateIssueField, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        context['post_fix'] = self.post_fix
        return context

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateIssueField, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(UpdateIssueField, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)


class ListIssueFieldView(LoginRequiredListView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/view/issuefield.html'
    model = None
    table = None

    def get_context_data(self, **kwargs):
        context = super(ListIssueFieldView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        tb = self.table(self.model.objects.all())
        RequestConfig(self.request).configure(tb)
        context['object_list'] = tb
        return context


class ListIssueView(LoginRequiredListView):
    template_name = 'issue/view/issue.html'
    table=None
    model = None

    def get_context_data(self, **kwargs):
        context = super(ListIssueView, self).get_context_data(**kwargs)
        tb = self.table(self.model.objects.all())
        RequestConfig(self.request).configure(tb)
        context['object_list'] = tb
        return context

    def get(self, request, *args, **kwargs):
        return super(ListIssueView, self).get(request, *args, **kwargs)


class DeleteIssueItem(LoginRequiredDeleteView):
    obj_id = -1
    page_title='ITSY Delete Issue Item'
    page_heading='Delete An Issue Item:'
    template_name = 'issue/create/delete.html'
    context_object_name = 'object'

    def get(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(DeleteIssueItem, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.obj_id = kwargs.get('id')
        return super(DeleteIssueItem, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.model, id=self.obj_id)

    def get_context_data(self, **kwargs):
        context = super(DeleteIssueItem, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class IssueSearch(LoginRequiredTemplateView):
    query = ''
    template_name = 'issue/search/simple.html'
    def get(self, request, *args, **kwargs):
        return super(IssueSearch, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(IssueSearch, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IssueSearch, self).get_context_data(**kwargs)
        context['issue_list'] = SearchQuerySet().autocomplete(
            content_auto=self.request.GET.get('q','')
        )
        return context


class IssueAdvancedSearch(LoginRequiredTemplateView):
    query = ''
    template_name = 'issue/search/advanced.html'
    def get(self, request, *args, **kwargs):
        return super(IssueAdvancedSearch, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(IssueAdvancedSearch, self).post(request, *args, **kwargs)