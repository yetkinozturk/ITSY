from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django import forms
from issue.models import Issue


class CreateIssueDetailsForm(forms.ModelForm):
    class Meta:
        model = Issue

    def __init__(self, *args, **kwargs):
        super(CreateIssueDetailsForm, self).__init__(*args, **kwargs)
        issue = kwargs.get('instance', None)
        if issue:
            self.fields.pop('effort_calc')
            self.fields.pop('template')
            if issue.template:
                self.fields['profile'] = forms.CharField(max_length=200)

class CreateIssueDetails(UpdateView):
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
        return get_object_or_404(Issue, slug=self.slug)


class CreateIssueView(CreateView):

    def get_success_url(self):
        return '/issue/create/details/%s/' % self.object.slug


class CreateIssueFlow(CreateView):
    pass


class CreateIssueField(CreateView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/create/issuefield.html'

    def get_context_data(self, **kwargs):
        context = super(CreateIssueField, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class ListIssueFieldView(ListView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/view/issuefield.html'

    def get_context_data(self, **kwargs):
        context = super(ListIssueFieldView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class ListIssueView(ListView):
    template_name = 'issue/view/issue.html'