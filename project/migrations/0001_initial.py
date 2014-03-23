# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MilestoneStatus'
        db.create_table(u'project_milestonestatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('project', ['MilestoneStatus'])

        # Adding model 'Milestone'
        db.create_table(u'project_milestone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='title', unique_with=())),
            ('effort', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True)),
            ('effort_calc', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('bug_to_fixed', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('bug_fixed', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('feature_to_develop', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('feature_developed', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('responsible', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.MilestoneStatus'], null=True, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('complete_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('project', ['Milestone'])

        # Adding model 'ProjectCategory'
        db.create_table(u'project_projectcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('responsible', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'], null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('project', ['ProjectCategory'])

        # Adding model 'ProjectVersion'
        db.create_table(u'project_projectversion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.ProjectCategory'], null=True, blank=True)),
            ('responsible', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'], null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('project', ['ProjectVersion'])

        # Adding M2M table for field milestones on 'ProjectVersion'
        m2m_table_name = db.shorten_name(u'project_projectversion_milestones')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectversion', models.ForeignKey(orm['project.projectversion'], null=False)),
            ('milestone', models.ForeignKey(orm['project.milestone'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projectversion_id', 'milestone_id'])

        # Adding model 'Project'
        db.create_table(u'project_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='title', unique_with=())),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('responsible', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'], null=True, blank=True)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('project', ['Project'])

        # Adding model 'ProjectMembership'
        db.create_table(u'project_projectmembership', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
        ))
        db.send_create_signal('project', ['ProjectMembership'])

        # Adding M2M table for field members on 'ProjectMembership'
        m2m_table_name = db.shorten_name(u'project_projectmembership_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projectmembership', models.ForeignKey(orm['project.projectmembership'], null=False)),
            ('account', models.ForeignKey(orm['account.account'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projectmembership_id', 'account_id'])

        # Adding model 'Board'
        db.create_table(u'project_board', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from='title', unique_with=())),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('project', ['Board'])


    def backwards(self, orm):
        # Deleting model 'MilestoneStatus'
        db.delete_table(u'project_milestonestatus')

        # Deleting model 'Milestone'
        db.delete_table(u'project_milestone')

        # Deleting model 'ProjectCategory'
        db.delete_table(u'project_projectcategory')

        # Deleting model 'ProjectVersion'
        db.delete_table(u'project_projectversion')

        # Removing M2M table for field milestones on 'ProjectVersion'
        db.delete_table(db.shorten_name(u'project_projectversion_milestones'))

        # Deleting model 'Project'
        db.delete_table(u'project_project')

        # Deleting model 'ProjectMembership'
        db.delete_table(u'project_projectmembership')

        # Removing M2M table for field members on 'ProjectMembership'
        db.delete_table(db.shorten_name(u'project_projectmembership_members'))

        # Deleting model 'Board'
        db.delete_table(u'project_board')


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
        'project.board': {
            'Meta': {'ordering': "['-entry_date']", 'object_name': 'Board'},
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'title'", 'unique_with': '()'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
        'project.projectmembership': {
            'Meta': {'object_name': 'ProjectMembership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['account.Account']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['project.Project']"})
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

    complete_apps = ['project']