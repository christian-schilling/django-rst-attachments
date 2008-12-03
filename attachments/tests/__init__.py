import unittest
import datetime
import sys
import os

from django.core import management
from django.conf import settings

# Add the tests directory so the rst_attachments_testapp is on sys.path
test_root = os.path.dirname(__file__)
sys.path.append(test_root)

# Import rst_attachments_testapp's models
import rst_attachments_testapp.models
from rst_attachments_testapp.models import *

from attachments.models import AttachedImage

class TestAttachments(unittest.TestCase):

    def setUp(self):
        """Swaps out various Django calls for fake ones for our own nefarious purposes."""
        def new_get_apps():
            return [rst_attachments_testapp.models]
        from django.db import models
        from django.conf import settings
        models.get_apps_old, models.get_apps = models.get_apps, new_get_apps
        settings.INSTALLED_APPS, settings.OLD_INSTALLED_APPS = (
            ["rst_attachments_testapp"],
            settings.INSTALLED_APPS,
        )
        self.redo_app_cache()
        management.call_command('syncdb')

    def tearDown(self):
        """Undoes what monkeypatch did."""
        from django.db import models
        from django.conf import settings
        models.get_apps = models.get_apps_old
        settings.INSTALLED_APPS = settings.OLD_INSTALLED_APPS
        self.redo_app_cache()

        # Also delete all model instances
        AttachedImage.objects.all().delete()
        Post.objects.all().delete()

    def redo_app_cache(self):
        from django.db.models.loading import AppCache
        a = AppCache()
        a.loaded = False
        a._populate()

    def test_rst_line(self):
        import Image,os
        img = Image.new("RGB",(400,300))
        img.save(settings.MEDIA_ROOT+"foo.png")
        p1 = Post.objects.create(title="post1",text="Post 1's text")
        ia1 = AttachedImage.objects.create(
            name = "Image1",
            attached_to=p1,
            image = "foo.png",
        )

        self.assertEqual(ia1.rst_line,
            u""".. |Image1| image:: %s\n :alt: Image1\n""" % (ia1.image.url)
           +u""".. _Image1: %s\n""" % (ia1.image.url)
        )
        self.assertEqual(ia1.image.url,ia1.display_url)

        ia1.display = '100'
        ia1.save()
        self.assertNotEqual(ia1.image.url,ia1.display_url)
        os.remove(settings.MEDIA_ROOT+"foo.png")
        os.remove(settings.MEDIA_ROOT+"foo_disp.png")

