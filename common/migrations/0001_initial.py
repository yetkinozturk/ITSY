# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comment'
        db.create_table(u'common_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('common', ['Comment'])

        # Adding M2M table for field comments on 'Comment'
        m2m_table_name = db.shorten_name(u'common_comment_comments')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_comment', models.ForeignKey(orm['common.comment'], null=False)),
            ('to_comment', models.ForeignKey(orm['common.comment'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_comment_id', 'to_comment_id'])

        # Adding model 'MainConfiguration'
        db.create_table(u'common_mainconfiguration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email_use_tls', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_host', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('email_host_user', self.gf('django.db.models.fields.EmailField')(max_length=255)),
            ('email_host_password', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email_port', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=587)),
            ('email_fail_silently', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notification_email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('allow_registration', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('active_after_registration', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('allow_delete_items', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email_changes_to_reporter', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_changes_to_watchers', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_changes_to_assignee', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_changes_to_people', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('common', ['MainConfiguration'])

        # Adding model 'History'
        db.create_table(u'common_history', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('entry_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('common', ['History'])

        # Adding model 'IssueFieldName'
        db.create_table(u'common_issuefieldname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128, db_index=True)),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('common', ['IssueFieldName'])


    def backwards(self, orm):
        # Deleting model 'Comment'
        db.delete_table(u'common_comment')

        # Removing M2M table for field comments on 'Comment'
        db.delete_table(db.shorten_name(u'common_comment_comments'))

        # Deleting model 'MainConfiguration'
        db.delete_table(u'common_mainconfiguration')

        # Deleting model 'History'
        db.delete_table(u'common_history')

        # Deleting model 'IssueFieldName'
        db.delete_table(u'common_issuefieldname')


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
        'common.comment': {
            'Meta': {'object_name': 'Comment'},
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'comments_rel_+'", 'null': 'True', 'to': "orm['common.Comment']"}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'common.history': {
            'Meta': {'object_name': 'History'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']"}),
            'entry_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'common.issuefieldname': {
            'Meta': {'object_name': 'IssueFieldName'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'common.mainconfiguration': {
            'Meta': {'object_name': 'MainConfiguration'},
            'active_after_registration': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'allow_delete_items': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allow_registration': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_changes_to_assignee': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_changes_to_people': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_changes_to_reporter': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_changes_to_watchers': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_fail_silently': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_host': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'email_host_password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email_host_user': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'email_port': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '587'}),
            'email_use_tls': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notification_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['common']