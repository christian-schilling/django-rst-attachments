from imagekit.specs import ImageSpec
from imagekit import processors

class DynamicResize(processors.ImageProcessor):
    @classmethod
    def process(cls,img,fmt,obj):
        class TmpResize(processors.Resize):
            crop=True
            upscale=True
            width=obj.image_width
            height=obj.image_height
        return TmpResize.process(img,fmt,obj)

class Display(ImageSpec):
    quality = 95
    pre_cache = True
    access_as = 'scaled'
    processors = [DynamicResize]

