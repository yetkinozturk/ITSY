from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save,pre_delete
from django.core.exceptions import ValidationError
from common.models import IssueFieldName
from common.utils import update_field_name, delete_field_name
from account.models import Account
from autoslug import AutoSlugField


class MilestoneStatus(models.Model):
    status = models.CharField(_(u'Status'), max_length=128)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)

    class Meta:
        ordering = ['-entry_date']
        app_label = 'project'

    def __unicode__(self):
        return self.status


class Milestone(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    _prev_title = models.CharField(max_length=128,editable=False, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    effort = models.CharField(_(u'Effort'),max_length=128, null=True, blank=True)
    effort_calc = models.PositiveIntegerField(_(u'Effort Calculated'), null=True, blank=True,editable=False)
    bug_to_fixed = models.PositiveIntegerField(_(u'Bugs to Fixed'), null=True, blank=True)
    bug_fixed = models.PositiveIntegerField(_(u'Bugs Fixed'), null=True, blank=True)
    feature_to_develop = models.PositiveIntegerField(_(u'Feature to Develop'), null=True, blank=True)
    feature_developed = models.PositiveIntegerField(_(u'Feature Developed'), null=True, blank=True)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    status = models.ForeignKey(MilestoneStatus,verbose_name=_(u'Status'), null=True, blank=True)
    due_date = models.DateTimeField(_(u'Due Date'), null=True, blank=True)
    complete_date = models.DateTimeField(_(u'Date Completed'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']
        app_label = 'project'

    def __unicode__(self):
        return self.title

    def clean(self):
        if IssueFieldName.objects.filter(name=self.title):
            if not self.pk:
                raise ValidationError(_(u'There is another (type of) item with this title'))
            else:
                IssueFieldName.objects.filter(name=self.title).delete()

post_save.connect(receiver=update_field_name, sender=Milestone)
pre_delete.connect(receiver=delete_field_name, sender=Milestone)


class ProjectCategory(models.Model):
    name = models.CharField(_(u'Category Name'), max_length=128)
    _prev_name = models.CharField(max_length=128,editable=False, null=True, blank=True)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)

    class Meta:
        ordering = ['-entry_date']
        app_label = 'project'

    def __unicode__(self):
        return self.name

    def clean(self):
        if IssueFieldName.objects.filter(name=self.name):
            if not self.pk:
                raise ValidationError(_(u'There is another (type of) item with this name'))
            else:
                IssueFieldName.objects.filter(name=self.name).delete()

post_save.connect(receiver=update_field_name, sender=ProjectCategory)
pre_delete.connect(receiver=delete_field_name, sender=ProjectCategory)


class ProjectVersion(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    _prev_title = models.CharField(max_length=128,editable=False, null=True, blank=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    project = models.ForeignKey('Project', verbose_name=_(u'Project'))
    milestones = models.ManyToManyField(Milestone, verbose_name=_(u'Milestones'),null=True,blank=True)
    category = models.ForeignKey(ProjectCategory, verbose_name=_(u'Category'),null=True,blank=True)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']
        app_label = 'project'

    def __unicode__(self):
        return u'%s / %s'%(self.project.title, self.title)

    def clean(self):
        if IssueFieldName.objects.filter(name=self.title):
            if not self.pk:
                raise ValidationError(_(u'There is another (type of) item with this title'))
            else:
                IssueFieldName.objects.filter(name=self.title).delete()


post_save.connect(receiver=update_field_name, sender=ProjectVersion)
pre_delete.connect(receiver=delete_field_name, sender=ProjectVersion)


class Project(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    _prev_title = models.CharField(max_length=128,editable=False, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    responsible = models.ForeignKey(Account, verbose_name=_(u'Responsible'), null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']
        app_label = 'project'

    def __unicode__(self):
        return self.title

    def clean(self):
        if IssueFieldName.objects.filter(name=self.title):
            if not self.pk:
                raise ValidationError(_(u'There is another (type of) item with this title'))
            else:
                IssueFieldName.objects.filter(name=self.title).delete()

post_save.connect(receiver=update_field_name, sender=Project)
pre_delete.connect(receiver=delete_field_name, sender=Project)


class ProjectMembership(models.Model):
    project = models.ForeignKey(Project, verbose_name=_(u'Project'))
    members = models.ManyToManyField(Account,verbose_name=_(u'Members'),null=True,blank=True)

    class Meta:
        app_label = 'project'


class Board(models.Model):
    title = models.CharField(_(u'Title'), max_length=255, db_index=True)
    _prev_title = models.CharField(max_length=128,editable=False, null=True, blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    summary = models.TextField(_(u'Summary'), null=True, blank=True)
    project = models.ForeignKey(Project, verbose_name=_(u'Project'))
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True)
    update_date = models.DateTimeField(_(u'Update Date'), auto_now=True)

    class Meta:
        ordering = ['-entry_date']
        app_label = 'project'

    def __unicode__(self):
        return self.title

    def clean(self):
        if IssueFieldName.objects.filter(name=self.title):
            if not self.pk:
                raise ValidationError(_(u'There is another (type of) item with this title'))
            else:
                IssueFieldName.objects.filter(name=self.title).delete()

post_save.connect(receiver=update_field_name, sender=Board)
pre_delete.connect(receiver=delete_field_name, sender=Board)