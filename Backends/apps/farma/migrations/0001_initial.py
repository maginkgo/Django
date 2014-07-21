# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Farmacia'
        db.create_table(u'farma_farmacia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('direccion', self.gf('django.db.models.fields.TextField')(max_length=20)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(max_length=20)),
        ))
        db.send_create_signal(u'farma', ['Farmacia'])


    def backwards(self, orm):
        # Deleting model 'Farmacia'
        db.delete_table(u'farma_farmacia')


    models = {
        u'farma.farmacia': {
            'Meta': {'object_name': 'Farmacia'},
            'direccion': ('django.db.models.fields.TextField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['farma']