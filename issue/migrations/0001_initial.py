# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IssueType'
        db.create_table(u'issue_issuetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueType'])

        # Adding model 'IssuePriority'
        db.create_table(u'issue_issuepriority', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssuePriority'])

        # Adding model 'IssueCharField'
        db.create_table(u'issue_issuecharfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueCharField'])

        # Adding model 'IssueTextField'
        db.create_table(u'issue_issuetextfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueTextField'])

        # Adding model 'IssueImageField'
        db.create_table(u'issue_issueimagefield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueImageField'])

        # Adding model 'IssueFileField'
        db.create_table(u'issue_issuefilefield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueFileField'])

        # Adding model 'IssueBooleanField'
        db.create_table(u'issue_issuebooleanfield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueBooleanField'])

        # Adding model 'IssueDatetimeField'
        db.create_table(u'issue_issuedatetimefield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueDatetimeField'])

        # Adding model 'IssueChoiceField'
        db.create_table(u'issue_issuechoicefield', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('choices', self.gf('django.db.models.fields.TextField')()),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueChoiceField'])

        # Adding model 'IssuePerson'
        db.create_table(u'issue_issueperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssuePerson'])

        # Adding model 'IssueStatus'
        db.create_table(u'issue_issuestatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('_prev_name', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueStatus'])

        # Adding model 'IssueFlow'
        db.create_table(u'issue_issueflow', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('accounts', self.gf('common.fields.ListField')(null=True, blank=True)),
            ('current', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('next', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('prev', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueFlow'])

        # Adding model 'IssueTemplate'
        db.create_table(u'issue_issuetemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('flow', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueFlow'], null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueTemplate'])

        # Adding M2M table for field char_fields on 'IssueTemplate'
        m2m_table_name = db.shorten_name(u'issue_issuetemplate_char_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuetemplate', models.ForeignKey(orm['issue.issuetemplate'], null=False)),
            ('issuecharfield', models.ForeignKey(orm['issue.issuecharfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuetemplate_id', 'issuecharfield_id'])

        # Adding M2M table for field text_fields on 'IssueTemplate'
        m2m_table_name = db.shorten_name(u'issue_issuetemplate_text_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuetemplate', models.ForeignKey(orm['issue.issuetemplate'], null=False)),
            ('issuetextfield', models.ForeignKey(orm['issue.issuetextfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuetemplate_id', 'issuetextfield_id'])

        # Adding M2M table for field image_fields on 'IssueTemplate'
        m2m_table_name = db.shorten_name(u'issue_issuetemplate_image_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuetemplate', models.ForeignKey(orm['issue.issuetemplate'], null=False)),
            ('issueimagefield', models.ForeignKey(orm['issue.issueimagefield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuetemplate_id', 'issueimagefield_id'])

        # Adding M2M table for field file_fields on 'IssueTemplate'
        m2m_table_name = db.shorten_name(u'issue_issuetemplate_file_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuetemplate', models.ForeignKey(orm['issue.issuetemplate'], null=False)),
            ('issuefilefield', models.ForeignKey(orm['issue.issuefilefield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuetemplate_id', 'issuefilefield_id'])

        # Adding M2M table for field bool_fields on 'IssueTemplate'
        m2m_table_name = db.shorten_name(u'issue_issuetemplate_bool_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuetemplate', models.ForeignKey(orm['issue.issuetemplate'], null=False)),
            ('issuebooleanfield', models.ForeignKey(orm['issue.issuebooleanfield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuetemplate_id', 'issuebooleanfield_id'])

        # Adding M2M table for field choice_fields on 'IssueTemplate'
        m2m_table_name = db.shorten_name(u'issue_issuetemplate_choice_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuetemplate', models.ForeignKey(orm['issue.issuetemplate'], null=False)),
            ('issuechoicefield', models.ForeignKey(orm['issue.issuechoicefield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuetemplate_id', 'issuechoicefield_id'])

        # Adding M2M table for field date_fields on 'IssueTemplate'
        m2m_table_name = db.shorten_name(u'issue_issuetemplate_date_fields')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuetemplate', models.ForeignKey(orm['issue.issuetemplate'], null=False)),
            ('issuedatetimefield', models.ForeignKey(orm['issue.issuedatetimefield'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuetemplate_id', 'issuedatetimefield_id'])

        # Adding M2M table for field people on 'IssueTemplate'
        m2m_table_name = db.shorten_name(u'issue_issuetemplate_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuetemplate', models.ForeignKey(orm['issue.issuetemplate'], null=False)),
            ('issueperson', models.ForeignKey(orm['issue.issueperson'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuetemplate_id', 'issueperson_id'])

        # Adding model 'Issue'
        db.create_table(u'issue_issue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='title', unique_with=())),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('effort', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('effort_calc', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('project_version', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ProjectVersion'])),
            ('assignee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'], null=True, blank=True)),
            ('reporter', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueType'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueStatus'], null=True, blank=True)),
            ('priority', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssuePriority'], null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueTemplate'])),
            ('changelog', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('is_draft', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('resolved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('issue', ['Issue'])

        # Adding M2M table for field sub_issues on 'Issue'
        m2m_table_name = db.shorten_name(u'issue_issue_sub_issues')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_issue', models.ForeignKey(orm['issue.issue'], null=False)),
            ('to_issue', models.ForeignKey(orm['issue.issue'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_issue_id', 'to_issue_id'])

        # Adding model 'IssueWatch'
        db.create_table(u'issue_issuewatch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
        ))
        db.send_create_signal('issue', ['IssueWatch'])

        # Adding M2M table for field watchers on 'IssueWatch'
        m2m_table_name = db.shorten_name(u'issue_issuewatch_watchers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('issuewatch', models.ForeignKey(orm['issue.issuewatch'], null=False)),
            ('account', models.ForeignKey(orm['account.account'], null=False))
        ))
        db.create_unique(m2m_table_name, ['issuewatch_id', 'account_id'])

        # Adding model 'IssueComment'
        db.create_table(u'issue_issuecomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('issue', ['IssueComment'])

        # Adding model 'IssueCharValue'
        db.create_table(u'issue_issuecharvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueCharField'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueCharValue'])

        # Adding model 'IssueTextValue'
        db.create_table(u'issue_issuetextvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueTextField'])),
            ('value', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueTextValue'])

        # Adding model 'IssueImageValue'
        db.create_table(u'issue_issueimagevalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueImageField'])),
            ('value', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueImageValue'])

        # Adding model 'IssueFileValue'
        db.create_table(u'issue_issuefilevalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueFileField'])),
            ('value', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueFileValue'])

        # Adding model 'IssuePersonValue'
        db.create_table(u'issue_issuepersonvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssuePerson'])),
            ('value', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'], null=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssuePersonValue'])

        # Adding model 'IssueBoolValue'
        db.create_table(u'issue_issueboolvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueBooleanField'])),
            ('value', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('issue', ['IssueBoolValue'])

        # Adding model 'IssueDateValue'
        db.create_table(u'issue_issuedatevalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueDatetimeField'])),
            ('value', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueDateValue'])

        # Adding model 'IssueChoiceValue'
        db.create_table(u'issue_issuechoicevalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('issue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.Issue'])),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['issue.IssueChoiceField'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('issue', ['IssueChoiceValue'])


    def backwards(self, orm):
        # Deleting model 'IssueType'
        db.delete_table(u'issue_issuetype')

        # Deleting model 'IssuePriority'
        db.delete_table(u'issue_issuepriority')

        # Deleting model 'IssueCharField'
        db.delete_table(u'issue_issuecharfield')

        # Deleting model 'IssueTextField'
        db.delete_table(u'issue_issuetextfield')

        # Deleting model 'IssueImageField'
        db.delete_table(u'issue_issueimagefield')

        # Deleting model 'IssueFileField'
        db.delete_table(u'issue_issuefilefield')

        # Deleting model 'IssueBooleanField'
        db.delete_table(u'issue_issuebooleanfield')

        # Deleting model 'IssueDatetimeField'
        db.delete_table(u'issue_issuedatetimefield')

        # Deleting model 'IssueChoiceField'
        db.delete_table(u'issue_issuechoicefield')

        # Deleting model 'IssuePerson'
        db.delete_table(u'issue_issueperson')

        # Deleting model 'IssueStatus'
        db.delete_table(u'issue_issuestatus')

        # Deleting model 'IssueFlow'
        db.delete_table(u'issue_issueflow')

        # Deleting model 'IssueTemplate'
        db.delete_table(u'issue_issuetemplate')

        # Removing M2M table for field char_fields on 'IssueTemplate'
        db.delete_table(db.shorten_name(u'issue_issuetemplate_char_fields'))

        # Removing M2M table for field text_fields on 'IssueTemplate'
        db.delete_table(db.shorten_name(u'issue_issuetemplate_text_fields'))

        # Removing M2M table for field image_fields on 'IssueTemplate'
        db.delete_table(db.shorten_name(u'issue_issuetemplate_image_fields'))

        # Removing M2M table for field file_fields on 'IssueTemplate'
        db.delete_table(db.shorten_name(u'issue_issuetemplate_file_fields'))

        # Removing M2M table for field bool_fields on 'IssueTemplate'
        db.delete_table(db.shorten_name(u'issue_issuetemplate_bool_fields'))

        # Removing M2M table for field choice_fields on 'IssueTemplate'
        db.delete_table(db.shorten_name(u'issue_issuetemplate_choice_fields'))

        # Removing M2M table for field date_fields on 'IssueTemplate'
        db.delete_table(db.shorten_name(u'issue_issuetemplate_date_fields'))

        # Removing M2M table for field people on 'IssueTemplate'
        db.delete_table(db.shorten_name(u'issue_issuetemplate_people'))

        # Deleting model 'Issue'
        db.delete_table(u'issue_issue')

        # Removing M2M table for field sub_issues on 'Issue'
        db.delete_table(db.shorten_name(u'issue_issue_sub_issues'))

        # Deleting model 'IssueWatch'
        db.delete_table(u'issue_issuewatch')

        # Removing M2M table for field watchers on 'IssueWatch'
        db.delete_table(db.shorten_name(u'issue_issuewatch_watchers'))

        # Deleting model 'IssueComment'
        db.delete_table(u'issue_issuecomment')

        # Deleting model 'IssueCharValue'
        db.delete_table(u'issue_issuecharvalue')

        # Deleting model 'IssueTextValue'
        db.delete_table(u'issue_issuetextvalue')

        # Deleting model 'IssueImageValue'
        db.delete_table(u'issue_issueimagevalue')

        # Deleting model 'IssueFileValue'
        db.delete_table(u'issue_issuefilevalue')

        # Deleting model 'IssuePersonValue'
        db.delete_table(u'issue_issuepersonvalue')

        # Deleting model 'IssueBoolValue'
        db.delete_table(u'issue_issueboolvalue')

        # Deleting model 'IssueDateValue'
        db.delete_table(u'issue_issuedatevalue')

        # Deleting model 'IssueChoiceValue'
        db.delete_table(u'issue_issuechoicevalue')


    models = {
        'account.account': {
            'Meta': {'object_name': 'Account'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'follows': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'followers'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['account.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'im': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_admin': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.AccountRole']", 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.AccountTeam']", 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'US'", 'max_length': '4'}),
            'website': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        'account.accountrole': {
            'Meta': {'object_name': 'AccountRole'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'account.accountteam': {
            'Meta': {'object_name': 'AccountTeam'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'issue.issue': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'Issue'},
            'assignee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']", 'null': 'True', 'blank': 'True'}),
            'changelog': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effort': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'effort_calc': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'priority': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssuePriority']", 'null': 'True', 'blank': 'True'}),
            'project_version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.ProjectVersion']"}),
            'reporter': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'resolved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'title'", 'unique_with': '()'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueStatus']", 'null': 'True', 'blank': 'True'}),
            'sub_issues': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.Issue']", 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueTemplate']"}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueType']", 'null': 'True', 'blank': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'issue.issuebooleanfield': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueBooleanField'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'issue.issueboolvalue': {
            'Meta': {'object_name': 'IssueBoolValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueBooleanField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'issue.issuecharfield': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueCharField'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'issue.issuecharvalue': {
            'Meta': {'object_name': 'IssueCharValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueCharField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'issue.issuechoicefield': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueChoiceField'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'choices': ('django.db.models.fields.TextField', [], {}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'issue.issuechoicevalue': {
            'Meta': {'object_name': 'IssueChoiceValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueChoiceField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'issue.issuecomment': {
            'Meta': {'object_name': 'IssueComment'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'issue.issuedatetimefield': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueDatetimeField'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'issue.issuedatevalue': {
            'Meta': {'object_name': 'IssueDateValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueDatetimeField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'value': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'issue.issuefilefield': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueFileField'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'issue.issuefilevalue': {
            'Meta': {'object_name': 'IssueFileValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueFileField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'value': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'issue.issueflow': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueFlow'},
            'accounts': ('common.fields.ListField', [], {'null': 'True', 'blank': 'True'}),
            'current': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'next': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prev': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'issue.issueimagefield': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueImageField'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'issue.issueimagevalue': {
            'Meta': {'object_name': 'IssueImageValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueImageField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'value': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'issue.issueperson': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssuePerson'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'issue.issuepersonvalue': {
            'Meta': {'object_name': 'IssuePersonValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssuePerson']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'value': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']", 'null': 'True', 'blank': 'True'})
        },
        'issue.issuepriority': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssuePriority'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'issue.issuestatus': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueStatus'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'issue.issuetemplate': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueTemplate'},
            'bool_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.IssueBooleanField']", 'null': 'True', 'blank': 'True'}),
            'char_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.IssueCharField']", 'null': 'True', 'blank': 'True'}),
            'choice_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.IssueChoiceField']", 'null': 'True', 'blank': 'True'}),
            'date_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.IssueDatetimeField']", 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'file_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.IssueFileField']", 'null': 'True', 'blank': 'True'}),
            'flow': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueFlow']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.IssueImageField']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.IssuePerson']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"}),
            'text_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['issue.IssueTextField']", 'null': 'True', 'blank': 'True'})
        },
        'issue.issuetextfield': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueTextField'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'issue.issuetextvalue': {
            'Meta': {'object_name': 'IssueTextValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.IssueTextField']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'value': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'issue.issuetype': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'IssueType'},
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'issue.issuewatch': {
            'Meta': {'object_name': 'IssueWatch'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']"}),
            'watchers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Account']", 'symmetrical': 'False'})
        },
        'project.milestone': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'Milestone'},
            'bug_fixed': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bug_to_fixed': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'complete_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effort': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'effort_calc': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feature_developed': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'feature_to_develop': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'responsible': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'title'", 'unique_with': '()'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.MilestoneStatus']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'project.milestonestatus': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'MilestoneStatus'},
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'project.project': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'Project'},
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'responsible': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'title'", 'unique_with': '()'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'project.projectcategory': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'ProjectCategory'},
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'responsible': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']", 'null': 'True', 'blank': 'True'})
        },
        'project.projectversion': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'ProjectVersion'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.ProjectCategory']", 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestones': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['project.Milestone']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"}),
            'responsible': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']", 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['issue']