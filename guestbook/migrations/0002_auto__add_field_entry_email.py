# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Entry.email'
        db.add_column(u'guestbook_entry', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='t@tt.tt', max_length=75),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Entry.email'
        db.delete_column(u'guestbook_entry', 'email')


    models = {
        u'guestbook.entry': {
            'Meta': {'ordering': "(u'creation_datetime',)", 'object_name': 'Entry'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'creation_datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['guestbook']