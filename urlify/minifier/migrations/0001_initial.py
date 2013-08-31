# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MinifiedURL'
        db.create_table(u'minifier_minifiedurl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'minifier', ['MinifiedURL'])


    def backwards(self, orm):
        # Deleting model 'MinifiedURL'
        db.delete_table(u'minifier_minifiedurl')


    models = {
        u'minifier.minifiedurl': {
            'Meta': {'object_name': 'MinifiedURL'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['minifier']