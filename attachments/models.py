from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class AttachedFile(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=settings.MEDIA_PREFIX+'/attachments/files/%Y/%m')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    attached_to = generic.GenericForeignKey()

    def __unicode__(self):
        return self.name

    @property
    def rst_line(self):
        return u'.. _%s: %s\n' % (
            self.name,
            self.file.url,
        )

class AttachedImage(models.Model):
    name = models.CharField(max_length=255)
    link_to = models.URLField(blank=True)
    display = models.PositiveIntegerField(default=1,choices=(
        (1 ,_('full')),
        #(10,_('linked thumbnail')),
    ))
    image = models.ImageField(upload_to=settings.MEDIA_PREFIX+'/attachments/images/%Y/%m')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    attached_to = generic.GenericForeignKey()

    def __unicode__(self):
        return self.name

    @property
    def rst_line(self):
        line = u'.. |%s| image:: %s\n :alt: %s\n' % (
            self.name,
            self.image.url,
            self.name,
        )
        if not self.link_to:
            return line
        return line + u'.. _%s: %s\n' % (
            self.name,
            self.link_to,
        )

