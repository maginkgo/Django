# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Guardia'
        db.create_table(u'farma_guardia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('farmacia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['farma.Farmacia'])),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='a', max_length=1)),
        ))
        db.send_create_signal(u'farma', ['Guardia'])


        # Changing field 'Farmacia.nombre'
        db.alter_column(u'farma_farmacia', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Farmacia.telefono'
        db.alter_column(u'farma_farmacia', 'telefono', self.gf('django.db.models.fields.IntegerField')(max_length=30))

        # Changing field 'Farmacia.direccion'
        db.alter_column(u'farma_farmacia', 'direccion', self.gf('django.db.models.fields.CharField')(max_length=50))

    def backwards(self, orm):
        # Deleting model 'Guardia'
        db.delete_table(u'farma_guardia')


        # Changing field 'Farmacia.nombre'
        db.alter_column(u'farma_farmacia', 'nombre', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Changing field 'Farmacia.telefono'
        db.alter_column(u'farma_farmacia', 'telefono', self.gf('django.db.models.fields.IntegerField')(max_length=20))

        # Changing field 'Farmacia.direccion'
        db.alter_column(u'farma_farmacia', 'direccion', self.gf('django.db.models.fields.TextField')(max_length=20))

    models = {
        u'farma.farmacia': {
            'Meta': {'object_name': 'Farmacia'},
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'max_length': '30'})
        },
        u'farma.guardia': {
            'Meta': {'object_name': 'Guardia'},
            'farmacia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farma.Farmacia']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'a'", 'max_length': '1'})
        }
    }

    complete_apps = ['farma']