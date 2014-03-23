# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CodeRepository'
        db.create_table(u'repos_coderepository', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=(), max_length=50, populate_from='name')),
            ('repository_type', self.gf('django.db.models.fields.IntegerField')()),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('repos', ['CodeRepository'])


    def backwards(self, orm):
        # Deleting model 'CodeRepository'
        db.delete_table(u'repos_coderepository')


    models = {
        'repos.coderepository': {
            'Meta': {'object_name': 'CodeRepository'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'repository_type': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': "'name'"})
        }
    }

    complete_apps = ['repos']