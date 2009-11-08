
from south.db import db
from django.db import models
from attachments.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding field 'AttachedImage.float'
        db.add_column('attachments_attachedimage', 'float', orm['attachments.attachedimage:float'])
        
    
    
    def backwards(self, orm):
        
        # Deleting field 'AttachedImage.float'
        db.delete_column('attachments_attachedimage', 'float')
        
    
    
    models = {
        'attachments.attachedfile': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'attachments.attachedimage': {
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'float': ('django.db.models.fields.CharField', [], {'default': "'left'", 'max_length': '20'}),
            'format': ('django.db.models.fields.CharField', [], {'default': "'landscape'", 'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link_to': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'size': ('django.db.models.fields.CharField', [], {'default': "'small'", 'max_length': '20'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }
    
    complete_apps = ['attachments']
