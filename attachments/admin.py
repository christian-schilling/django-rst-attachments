from django.contrib.contenttypes import generic
from attachments import models

class AttachedImageInline(generic.GenericTabularInline):
    model = models.AttachedImage

class AttachedFileInline(generic.GenericTabularInline):
    model = models.AttachedFile
