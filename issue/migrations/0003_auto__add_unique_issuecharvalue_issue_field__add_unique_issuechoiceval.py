# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'IssueCharValue', fields ['issue', 'field']
        db.create_unique(u'issue_issuecharvalue', ['issue_id', 'field_id'])

        # Adding unique constraint on 'IssueChoiceValue', fields ['issue', 'field']
        db.create_unique(u'issue_issuechoicevalue', ['issue_id', 'field_id'])

        # Adding unique constraint on 'IssueFileValue', fields ['issue', 'field']
        db.create_unique(u'issue_issuefilevalue', ['issue_id', 'field_id'])

        # Adding unique constraint on 'IssueDateValue', fields ['issue', 'field']
        db.create_unique(u'issue_issuedatevalue', ['issue_id', 'field_id'])

        # Adding unique constraint on 'IssueBoolValue', fields ['issue', 'field']
        db.create_unique(u'issue_issueboolvalue', ['issue_id', 'field_id'])

        # Adding unique constraint on 'IssueTextValue', fields ['issue', 'field']
        db.create_unique(u'issue_issuetextvalue', ['issue_id', 'field_id'])

        # Adding unique constraint on 'IssuePersonValue', fields ['issue', 'field']
        db.create_unique(u'issue_issuepersonvalue', ['issue_id', 'field_id'])

        # Adding unique constraint on 'IssueImageValue', fields ['issue', 'field']
        db.create_unique(u'issue_issueimagevalue', ['issue_id', 'field_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'IssueImageValue', fields ['issue', 'field']
        db.delete_unique(u'issue_issueimagevalue', ['issue_id', 'field_id'])

        # Removing unique constraint on 'IssuePersonValue', fields ['issue', 'field']
        db.delete_unique(u'issue_issuepersonvalue', ['issue_id', 'field_id'])

        # Removing unique constraint on 'IssueTextValue', fields ['issue', 'field']
        db.delete_unique(u'issue_issuetextvalue', ['issue_id', 'field_id'])

        # Removing unique constraint on 'IssueBoolValue', fields ['issue', 'field']
        db.delete_unique(u'issue_issueboolvalue', ['issue_id', 'field_id'])

        # Removing unique constraint on 'IssueDateValue', fields ['issue', 'field']
        db.delete_unique(u'issue_issuedatevalue', ['issue_id', 'field_id'])

        # Removing unique constraint on 'IssueFileValue', fields ['issue', 'field']
        db.delete_unique(u'issue_issuefilevalue', ['issue_id', 'field_id'])

        # Removing unique constraint on 'IssueChoiceValue', fields ['issue', 'field']
        db.delete_unique(u'issue_issuechoicevalue', ['issue_id', 'field_id'])

        # Removing unique constraint on 'IssueCharValue', fields ['issue', 'field']
        db.delete_unique(u'issue_issuecharvalue', ['issue_id', 'field_id'])


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
        'issue.history': {
            'Meta': {'object_name': 'History'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']"}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['issue.Issue']", 'null': 'True', 'blank': 'True'}),
            'log': ('django.db.models.fields.TextField', [], {})
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
            'Meta': {'unique_together': "(('issue', 'field'),)", 'object_name': 'IssueBoolValue'},
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
            'Meta': {'unique_together': "(('issue', 'field'),)", 'object_name': 'IssueCharValue'},
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
            'Meta': {'unique_together': "(('issue', 'field'),)", 'object_name': 'IssueChoiceValue'},
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
            'Meta': {'unique_together': "(('issue', 'field'),)", 'object_name': 'IssueDateValue'},
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
            'Meta': {'unique_together': "(('issue', 'field'),)", 'object_name': 'IssueFileValue'},
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
            'Meta': {'unique_together': "(('issue', 'field'),)", 'object_name': 'IssueImageValue'},
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
            'Meta': {'unique_together': "(('issue', 'field'),)", 'object_name': 'IssuePersonValue'},
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
            'Meta': {'unique_together': "(('issue', 'field'),)", 'object_name': 'IssueTextValue'},
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
            '_prev_title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
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
            '_prev_title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
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
            '_prev_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'responsible': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']", 'null': 'True', 'blank': 'True'})
        },
        'project.projectversion': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'ProjectVersion'},
            '_prev_title': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
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