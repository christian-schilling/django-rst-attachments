from imagekit.specs import ImageSpec
from imagekit import processors

class DynamicResize(processors.Resize):
    crop=True
    upscale=True

    @classmethod
    def process(cls,img,fmt,obj):
        cls.width=obj.image_width
        cls.height=obj.image_height
        return processors.Resize.process.im_func(cls,img,fmt,obj)

class Display(ImageSpec):
    quality = 95
    pre_cache = False
    access_as = 'scaled'
    processors = [DynamicResize]

