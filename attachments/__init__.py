from django.conf import settings
import models
from django.contrib.contenttypes.models import ContentType

def complete_content(obj,content_field='content',images_field='images',files_field='files',name_field=None):

    if getattr(obj,'is_html',False):
        return getattr(obj,content_field)
    
    retval = u''
    
    
    if name_field:
        retval += u"="*len(settings.WEBSITE_NAME)+u"\n"
        retval += settings.WEBSITE_NAME+u"\n"
        retval += u"="*len(settings.WEBSITE_NAME)+u"\n\n"
        retval += u"-"*len(getattr(obj,name_field))+u"\n"
        retval += obj.name+u"\n"
        retval += u"-"*len(getattr(obj,name_field))+u"\n\n"
    
    retval += getattr(obj,content_field)
    retval += u'\n\n.. ' + u"#"*80
    retval += u'\n   ' + u"The following lines are automatically inserted to access attachments."
    retval += u'\n   ' + u"#"*80
    
    images = models.AttachedImage.objects.filter(
         content_type=ContentType.objects.get_for_model(obj),
         object_id=obj.id,
    )
    files = models.AttachedFile.objects.filter(
         content_type=ContentType.objects.get_for_model(obj),
         object_id=obj.id,
    )
    try:
        retval += u'\n\n'+u'\n'.join((i.rst_line for i in images))
    except UnicodeEncodeError:
        pass
    try:
        retval += u'\n\n'+u'\n'.join((i.rst_line for i in files))
    except UnicodeEncodeError:
        pass
    return retval