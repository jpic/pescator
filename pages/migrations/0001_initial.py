# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Block'
        db.create_table(u'pages_block', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('body', self.gf('redactor.fields.RedactorField')()),
            ('body_fr', self.gf('redactor.fields.RedactorField')(null=True, blank=True)),
            ('body_en', self.gf('redactor.fields.RedactorField')(null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.CharField')(default=u'pages/block.html', max_length=50)),
        ))
        db.send_create_signal(u'pages', ['Block'])

        # Adding model 'Photo'
        db.create_table(u'pages_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'pages', ['Photo'])

        # Adding model 'Page'
        db.create_table(u'pages_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('slug_fr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('body', self.gf('redactor.fields.RedactorField')()),
            ('body_fr', self.gf('redactor.fields.RedactorField')(null=True, blank=True)),
            ('body_en', self.gf('redactor.fields.RedactorField')(null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.CharField')(default=u'pages/page_detail.html', max_length=50)),
        ))
        db.send_create_signal(u'pages', ['Page'])


        # Adding SortedM2M table for field blocks on 'Page'
        db.create_table(u'pages_page_blocks', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'pages.page'], null=False)),
            ('block', models.ForeignKey(orm[u'pages.block'], null=False)),
            ('sort_value', models.IntegerField())
        ))
        db.create_unique(u'pages_page_blocks', ['page_id', 'block_id'])

        # Adding SortedM2M table for field photos on 'Page'
        db.create_table(u'pages_page_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm[u'pages.page'], null=False)),
            ('photo', models.ForeignKey(orm[u'pages.photo'], null=False)),
            ('sort_value', models.IntegerField())
        ))
        db.create_unique(u'pages_page_photos', ['page_id', 'photo_id'])

    def backwards(self, orm):
        # Deleting model 'Block'
        db.delete_table(u'pages_block')

        # Deleting model 'Photo'
        db.delete_table(u'pages_photo')

        # Deleting model 'Page'
        db.delete_table(u'pages_page')

        # Removing M2M table for field blocks on 'Page'
        db.delete_table(db.shorten_name(u'pages_page_blocks'))

        # Removing M2M table for field photos on 'Page'
        db.delete_table(db.shorten_name(u'pages_page_photos'))


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