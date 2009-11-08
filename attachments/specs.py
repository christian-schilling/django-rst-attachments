from imagekit.specs import ImageSpec
from imagekit import processors

class ResizeMediumSquare(processors.Resize):
    crop = True
    width = 100
    height = 100
class MediumSquare(ImageSpec):
    pre_cache = False
    access_as = 'image_medium_square'
    processors = [ResizeMediumSquare]
class ResizeMediumLandscape(processors.Resize):
    crop = True
    width = 154
    height = 100
class MediumLandscape(ImageSpec):
    pre_cache = False
    access_as = 'image_medium_landscape'
    processors = [ResizeMediumLandscape]
class ResizeMediumPortrait(processors.Resize):
    crop = True
    width = 100
    height = 154
class MediumPortrait(ImageSpec):
    pre_cache = False
    access_as = 'image_medium_portrait'
    processors = [ResizeMediumPortrait]

class ResizeSmallSquare(processors.Resize):
    crop = True
    width = 64
    height = 64
class SmallSquare(ImageSpec):
    pre_cache = False
    access_as = 'image_small_square'
    processors = [ResizeSmallSquare]
class ResizeSmallLandscape(processors.Resize):
    crop = True
    width = 100
    height = 64
class SmallLandscape(ImageSpec):
    pre_cache = False
    access_as = 'image_small_landscape'
    processors = [ResizeSmallLandscape]
class ResizeSmallPortrait(processors.Resize):
    crop = True
    width = 64
    height = 100
class SmallPortrait(ImageSpec):
    pre_cache = False
    access_as = 'image_small_portrait'
    processors = [ResizeSmallPortrait]

class ResizeBigSquare(processors.Resize):
    crop = True
    width = 172
    height = 172
class BigSquare(ImageSpec):
    pre_cache = False
    access_as = 'image_big_square'
    processors = [ResizeBigSquare]
class ResizeBigLandscape(processors.Resize):
    crop = True
    width = 262
    height = 172
class BigLandscape(ImageSpec):
    pre_cache = False
    access_as = 'image_big_landscape'
    processors = [ResizeBigLandscape]
class ResizeBigPortrait(processors.Resize):
    crop = True
    width = 172
    height = 262
class BigPortrait(ImageSpec):
    pre_cache = False
    access_as = 'image_big_portrait'
    processors = [ResizeBigPortrait]
