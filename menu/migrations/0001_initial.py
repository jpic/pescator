# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'menu_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug_fr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'menu', ['Category'])

        # Adding model 'Dish'
        db.create_table(u'menu_dish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True)),
            ('category', self.gf('adminsortable.fields.SortableForeignKey')(to=orm['menu.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_fr', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_en', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug_fr', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('slug_en', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('description', self.gf('redactor.fields.RedactorField')(blank=True)),
            ('description_fr', self.gf('redactor.fields.RedactorField')(null=True, blank=True)),
            ('description_en', self.gf('redactor.fields.RedactorField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('sale_price_euros', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'menu', ['Dish'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'menu_category')

        # Deleting model 'Dish'
        db.delete_table(u'menu_dish')


    models = {
        u'menu.category': {
            'Meta': {'ordering': "['order']", 'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'menu.dish': {
            'Meta': {'ordering': "['order']", 'object_name': 'Dish'},
            'category': ('adminsortable.fields.SortableForeignKey', [], {'to': u"orm['menu.Category']"}),
            'description': ('redactor.fields.RedactorField', [], {'blank': 'True'}),
            'description_en': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'}),
            'description_fr': ('redactor.fields.RedactorField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_en': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'db_index': 'True'}),
            'sale_price_euros': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug_fr': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['menu']