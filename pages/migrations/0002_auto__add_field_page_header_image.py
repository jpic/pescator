# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.header_image'
        db.add_column(u'pages_page', 'header_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Page.header_image'
        db.delete_column(u'pages_page', 'header_image')


    models = {
        u'pages.block': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Block'},
            'body': ('redactor.fields.RedactorField', [], {}),
            'body_en': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'}),
            'body_fr': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "u'pages/block.html'", 'max_length': '50'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Page'},
            'blocks': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['pages.Block']", 'symmetrical': 'False', 'blank': 'True'}),
            'body': ('redactor.fields.RedactorField', [], {}),
            'body_en': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'}),
            'body_fr': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'}),
            'header_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'photos': ('sortedm2m.fields.SortedManyToManyField', [], {'to': u"orm['pages.Photo']", 'symmetrical': 'False', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "u'pages/page_detail.html'", 'max_length': '50'})
        },
        u'pages.photo': {
            'Meta': {'ordering': "(u'name',)", 'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pages']