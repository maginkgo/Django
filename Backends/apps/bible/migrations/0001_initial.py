# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Biblia'
        db.create_table(u'bible_biblia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'bible', ['Biblia'])

        # Adding model 'Verso'
        db.create_table(u'bible_verso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('biblia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bible.Biblia'])),
            ('numero', self.gf('django.db.models.fields.IntegerField')()),
            ('capitulo', self.gf('django.db.models.fields.IntegerField')()),
            ('libro', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('texto', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'bible', ['Verso'])


    def backwards(self, orm):
        # Deleting model 'Biblia'
        db.delete_table(u'bible_biblia')

        # Deleting model 'Verso'
        db.delete_table(u'bible_verso')


    models = {
        u'bible.biblia': {
            'Meta': {'object_name': 'Biblia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'bible.verso': {
            'Meta': {'object_name': 'Verso'},
            'biblia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bible.Biblia']"}),
            'capitulo': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libro': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'numero': ('django.db.models.fields.IntegerField', [], {}),
            'texto': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['bible']