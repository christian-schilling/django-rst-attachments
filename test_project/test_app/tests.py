# encoding: utf-8
from djangosanetesting import cases

from django.conf import settings

from attachments import models
from test_app.models import Post

class TestAttachments(cases.UnitTestCase):

    def setUp(self):
        import Image
        img = Image.new("RGB",(400,300))
        img.save(settings.MEDIA_ROOT+u"foäo.png")
        
        self.p1 = Post.objects.create(title="post1",text="Post 1's text")
        self.ia1 = models.AttachedImage.objects.create(
            name = "Image1",
            attached_to=self.p1,
            image = unicode(u"foo.png"),
        )
        
    def tearDown(self):
        import os
        os.system('rm '+settings.MEDIA_ROOT+'foo.png')
        
        models.AttachedImage.objects.all().delete()
        Post.objects.all().delete()

    def test_image_rst_line(self):

        self.assertEqual(self.ia1.rst_line,''.join((
            u".. |Image1| image:: attachments/cache/foo_scaled.png\n",
            u" :alt: Image1\n",
            u" :class: left\n",
            u".. _Image1: foo.png\n",
        )))
        
    def test_complete_content(self):
        from attachments import complete_content
        complete = complete_content(self.p1,content_field='text')
        ref = u''.join((
            u"Post 1's text\n\n",
            u".. ################################################################################\n",
            u"   The following lines are automatically inserted to access attachments.\n",
            u"   ################################################################################\n",
            u"\n",
            u".. |Image1| image:: attachments/cache/foo_scaled.png\n",
            u" :alt: Image1\n",
            u" :class: left\n",
            u".. _Image1: foo.png\n\n\n",
        ))
        self.assertEqual(complete,ref)
            
            
            
                    