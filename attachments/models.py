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
    link_to = models.URLField(verify_exists=False,blank=True)
    rows = models.PositiveIntegerField(default=5)
    columns = models.PositiveIntegerField(default=4)
    float = models.CharField(max_length=20,default='left',choices=(
        ('left',_('left')),
        ('right',_('right')),
    ))
    image = models.ImageField(upload_to=settings.MEDIA_PREFIX+'/attachments/images/%Y/%m')

    @property
    def image_height(self):
        return self.rows*18 - 8
    @property
    def image_width(self):
        return 26*self.columns+16*(self.columns-1)

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
        return self.scaled.url

    @property
    def rst_line(self):
        line = u'.. |%s| image:: %s\n :alt: %s\n :class: %s\n' % (
            self.name,
            self.display_url,
            self.name,
            self.float,
        )
        return line + u'.. _%s: %s\n' % (
            self.name,
            self.link_to or self.image.url,
        )

    def save(self,*args,**kwargs):
        super(AttachedImage, self).save(*args, **kwargs)
        self._clear_cache()

