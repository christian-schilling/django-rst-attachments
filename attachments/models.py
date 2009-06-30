from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from os import path
import Image

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

class AttachedImage(models.Model):
    name = models.CharField(max_length=255)
    link_to = models.URLField(blank=True)
    display = models.PositiveIntegerField(default=1,choices=(
        (1 ,_('full')),
        (100,_('100x100')),
        (200,_('200x200')),
        (300,_('300x300')),
    ))
    image = models.ImageField(upload_to=settings.MEDIA_PREFIX+'/attachments/images/%Y/%m')

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    attached_to = generic.GenericForeignKey()

    def __unicode__(self):
        return self.name

    def save(self,*args,**kwargs):
        super(AttachedImage,self).save(*args,**kwargs)
        if self.display_url != self.image.url:
            origfilename = settings.MEDIA_ROOT+unicode(self.image)
            base,ext = origfilename.rsplit('.',1)
            dispfilename = u'%s_disp.%s' % (base,ext)
            im = Image.open(origfilename)
            im = im.resize(imrect(im.size,(float(self.display),)*2))
            im.save(dispfilename)

    @property
    def display_url(self):
        if self.display>20:
            base,ext = self.image.url.rsplit('.',1)
            return u'%s_disp.%s' % (base,ext)
        else:
            return self.image.url

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

