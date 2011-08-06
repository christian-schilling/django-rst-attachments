from django import template
from django.utils.safestring import mark_safe
import attachments

register = template.Library()

@register.filter
def complete_content(obj,content_field='content'):
    return mark_safe(attachments.complete_content(obj, content_field))