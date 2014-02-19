from django.core.context_processors import csrf
from django.shortcuts import render
from django.views.generic.base import View
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from issue.models import (Issue, IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField, IssueImageField,IssueFileField,IssuePerson,
                          IssueFlow,IssueTemplate)


class CreateIssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title', 'summary', 'effort', 'project_version', 'type',
            'status', 'priority', 'template', 'flow', 'sub_issues','due_date'
        ]

    def clean(self):
        cleaned_data = super(CreateIssueForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueView(View):
    template_name = 'issue/createissue.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_form'] = CreateIssueForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)


class CreateIssueTypeForm(ModelForm):
    class Meta:
        model = IssueType
        fields = [
            'name',
        ]

    def clean(self):
        cleaned_data = super(CreateIssueTypeForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueTypeView(View):
    template_name = 'issue/createissuetype.html'
    content = {}
    content['issue_types'] = IssueType.objects.all()

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_type_form'] = CreateIssueTypeForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssueTypeForm(request.POST)
        self.content['create_issue_type_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssueStatusForm(ModelForm):
    class Meta:
        model = IssueStatus
        fields = [
            'status',
        ]

    def clean(self):
        cleaned_data = super(CreateIssueStatusForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueStatusView(View):
    template_name = 'issue/createissuestatus.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_status_form'] = CreateIssueStatusForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssueStatusForm(request.POST)
        self.content['create_issue_status_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssuePriorityForm(ModelForm):
    class Meta:
        model = IssuePriority
        fields = [
            'name',
        ]

    def clean(self):
        cleaned_data = super(CreateIssuePriorityForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data

class CreateIssuePriorityView(View):
    template_name = 'issue/createissuepriority.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_priority_form'] = CreateIssuePriorityForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssuePriorityForm(request.POST)
        self.content['create_issue_priority_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssueCharForm(ModelForm):
    class Meta:
        model = IssueCharField
        fields = [
            'name',
        ]

    def clean(self):
        cleaned_data = super(CreateIssueCharForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueCharView(View):
    template_name = 'issue/createissuechar.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_char_form'] = CreateIssueCharForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssueCharForm(request.POST)
        self.content['create_issue_char_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssueTextForm(ModelForm):
    class Meta:
        model = IssueTextField
        fields = [
            'name',
        ]

    def clean(self):
        cleaned_data = super(CreateIssueTextForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueTextView(View):
    template_name = 'issue/createissuetext.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_text_form'] = CreateIssueTextForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssueTextForm(request.POST)
        self.content['create_issue_text_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssueImageForm(ModelForm):
    class Meta:
        model = IssueImageField
        fields = [
            'name',
        ]

    def clean(self):
        cleaned_data = super(CreateIssueImageForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueImageView(View):
    template_name = 'issue/createissueimage.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_image_form'] = CreateIssueImageForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssueImageForm(request.POST)
        self.content['create_issue_image_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssueFileForm(ModelForm):
    class Meta:
        model = IssueFileField
        fields = [
            'name',
        ]

    def clean(self):
        cleaned_data = super(CreateIssueFileForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueFileView(View):
    template_name = 'issue/createissuefile.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_file_form'] = CreateIssueFileForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssueFileForm(request.POST)
        self.content['create_issue_file_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssuePersonForm(ModelForm):
    class Meta:
        model = IssuePerson
        fields = [
            'role',
        ]

    def clean(self):
        cleaned_data = super(CreateIssuePersonForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssuePersonView(View):
    template_name = 'issue/createissueperson.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_person_form'] = CreateIssuePersonForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssuePersonForm(request.POST)
        self.content['create_issue_person_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssueFlowForm(ModelForm):
    class Meta:
        model = IssueFlow
        fields = [
            'name',
        ]

    def clean(self):
        cleaned_data = super(CreateIssueFlowForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueFlowView(View):
    template_name = 'issue/createissueflow.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_flow_form'] = CreateIssueFlowForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssueFlowForm(request.POST)
        self.content['create_issue_flow_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)


class CreateIssueTemplateForm(ModelForm):
    class Meta:
        model = IssueTemplate
        fields = [
            'name','char_fields','text_fields','image_fields','file_fields',
            'people','project',
        ]

    def clean(self):
        cleaned_data = super(CreateIssueTemplateForm, self).clean()
        if not cleaned_data:
            raise forms.ValidationError(_(u"Fields are required."))
        return cleaned_data


class CreateIssueTemplateView(View):
    template_name = 'issue/createissuetemplate.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_template_form'] = CreateIssueTemplateForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        self.content.update(csrf(request))
        form = CreateIssueTemplateForm(request.POST)
        self.content['create_issue_template_form'] = form
        if form.is_valid():
            form.save()
        return render(request, self.template_name,self.content)