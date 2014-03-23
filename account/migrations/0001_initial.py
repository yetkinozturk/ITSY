# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AccountRole'
        db.create_table(u'account_accountrole', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('account', ['AccountRole'])

        # Adding model 'AccountTeam'
        db.create_table(u'account_accountteam', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('account', ['AccountTeam'])

        # Adding model 'Account'
        db.create_table(u'account_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.AccountRole'], null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.AccountTeam'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='US', max_length=4)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('im', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('is_admin', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('account', ['Account'])

        # Adding M2M table for field follows on 'Account'
        m2m_table_name = db.shorten_name(u'account_account_follows')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_account', models.ForeignKey(orm['account.account'], null=False)),
            ('to_account', models.ForeignKey(orm['account.account'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_account_id', 'to_account_id'])

        # Adding model 'Filter'
        db.create_table(u'account_filter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('query', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal('account', ['Filter'])

        # Adding model 'FavoriteFilters'
        db.create_table(u'account_favoritefilters', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
        ))
        db.send_create_signal('account', ['FavoriteFilters'])

        # Adding M2M table for field filters on 'FavoriteFilters'
        m2m_table_name = db.shorten_name(u'account_favoritefilters_filters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('favoritefilters', models.ForeignKey(orm['account.favoritefilters'], null=False)),
            ('filter', models.ForeignKey(orm['account.filter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['favoritefilters_id', 'filter_id'])


    def backwards(self, orm):
        # Deleting model 'AccountRole'
        db.delete_table(u'account_accountrole')

        # Deleting model 'AccountTeam'
        db.delete_table(u'account_accountteam')

        # Deleting model 'Account'
        db.delete_table(u'account_account')

        # Removing M2M table for field follows on 'Account'
        db.delete_table(db.shorten_name(u'account_account_follows'))

        # Deleting model 'Filter'
        db.delete_table(u'account_filter')

        # Deleting model 'FavoriteFilters'
        db.delete_table(u'account_favoritefilters')

        # Removing M2M table for field filters on 'FavoriteFilters'
        db.delete_table(db.shorten_name(u'account_favoritefilters_filters'))


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
        'account.favoritefilters': {
            'Meta': {'object_name': 'FavoriteFilters'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['account.Account']"}),
            'filters': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['account.Filter']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'account.filter': {
            'Meta': {'object_name': 'Filter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'query': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['account']