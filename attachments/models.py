from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from os import path
from imagekit.models import ImageModel

def imrect(size, target):
    """
    >>> imrect((100,200),(30,30))
    (15, 30)
    >>> imrect((150,100),(100,100))
    (100, 66)
    """
    divide = max(float(size[0])/target[0],float(size[1])/target[1])
    return int(size[0]/divide),int(size[1]/divide)
    

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

class AttachedImage(ImageModel):
    name = models.CharField(max_length=255)
    link_to = models.URLField(blank=True)
    size = models.CharField(default='small',max_length=20,choices=(
        ('small',_('small')),
        ('medium',_('medium')),
        ('big',_('big')),
    ))
    format = models.CharField(default='landscape',max_length=20,choices=(
        ('square',_('square')),
        ('landscape',_('landscape')),
        ('portrait',_('portrait')),
    ))
    image = models.ImageField(upload_to=settings.MEDIA_PREFIX+'/attachments/images/%Y/%m')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    attached_to = generic.GenericForeignKey()

    class IKOptions:
        spec_module = 'attachments.specs'
        cache_dir = 'attachments/cache'
        image_field = 'image'

    def __unicode__(self):
        return self.name

    @property
    def display_url(self):
        return getattr(self,'image_%s_%s'%(self.size,self.format)).url

    @property
    def rst_line(self):
        line = u'.. |%s| image:: %s\n :alt: %s\n' % (
            self.name,
            self.display_url,
            self.name,
        )
        return line + u'.. _%s: %s\n' % (
            self.name,
            self.link_to or self.image.url,
        )

