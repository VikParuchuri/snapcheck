# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PhoneRecord'
        db.create_table('api_phonerecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('api', ['PhoneRecord'])

        # Adding unique constraint on 'PhoneRecord', fields ['username', 'phone_number']
        db.create_unique('api_phonerecord', ['username', 'phone_number'])


    def backwards(self, orm):
        # Removing unique constraint on 'PhoneRecord', fields ['username', 'phone_number']
        db.delete_unique('api_phonerecord', ['username', 'phone_number'])

        # Deleting model 'PhoneRecord'
        db.delete_table('api_phonerecord')


    models = {
        'api.phonerecord': {
            'Meta': {'unique_together': "(('username', 'phone_number'),)", 'object_name': 'PhoneRecord'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
    }

    complete_apps = ['api']