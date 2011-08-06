
from south.db import db
from django.db import models
from attachments.models import *

class Migration:
    
    def forwards(self):
        
        
        # Mock Models
        ContentType = db.mock_model(model_name='ContentType', db_table='django_content_type', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[])
        
        # Model 'AttachedFile'
        db.create_table('attachments_attachedfile', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('name', models.CharField(max_length=255)),
            ('file', models.FileField(upload_to='attachments/files/%Y/%m')),
            ('content_type', models.ForeignKey(ContentType)),
            ('object_id', models.PositiveIntegerField()),
        ))
        
        # Mock Models
        ContentType = db.mock_model(model_name='ContentType', db_table='django_content_type', db_tablespace='', pk_field_name='id', pk_field_type=models.AutoField, pk_field_args=[])
        
        # Model 'AttachedImage'
        db.create_table('attachments_attachedimage', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('name', models.CharField(max_length=255)),
            ('link_to', models.URLField(blank=True)),
            ('display', models.PositiveIntegerField(default=1)),
            ('image', models.ImageField(upload_to='attachments/images/%Y/%m')),
            ('content_type', models.ForeignKey(ContentType)),
            ('object_id', models.PositiveIntegerField()),
        ))
        
        db.send_create_signal('attachments', ['AttachedFile','AttachedImage'])
    
    def backwards(self):
        db.delete_table('attachments_attachedimage')
        db.delete_table('attachments_attachedfile')
        
