from typing import ByteString
from . import impellerpy


class Rect(impellerpy.Rect_):
    def __init__(
        self, x: float = 0, y: float = 0, width: float = 0, height: float = 0
    ):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Point(impellerpy.Point_):
    def __init__(self, x: float = 0, y: float = 0):
        super().__init__()
        self.x = x
        self.y = y


class Size(impellerpy.Size_):
    def __init__(self, width: float = 0, height: float = 0):
        super().__init__()
        self.width = width
        self.height = height


class ISize(impellerpy.ISize_):
    def __init__(self, width: int = 0, height: int = 0):
        super().__init__()
        self.width = width
        self.height = height


class Range(impellerpy.Range_):
    def __init__(self, start: int = 0, end: int = 0):
        super().__init__()
        self.start = start
        self.end = end


class Matrix(impellerpy.Matrix_):
    pass


class ColorMatrix(impellerpy.ColorMatrix_):
    pass


class RoundingRadii(impellerpy.RoundingRadii_):
    pass


class Color(impellerpy.Color_):
    def __init__(
        self, r: float = 0.0, g: float = 0.0, b: float = 0.0, a: float = 0.0
    ):
        super().__init__()
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a


class TextureDescriptor(impellerpy.TextureDescriptor_):
    def __init__(
        self,
        pixel_format: impellerpy.PixelFormat_,
        texture_size: ISize,
        mip_count: int = 1,
    ):
        super().__init__()
        self.pixel_format = pixel_format
        self.size = texture_size
        self.mip_count = mip_count



class ContextVulkanSettings(impellerpy.ContextVulkanSettings_):
    pass


class ContextVulkanInfo(impellerpy.ContextVulkanInfo_):
    pass


class ColorFilter(impellerpy.ColorFilter_):
    pass


class ColorSource(impellerpy.ColorSource_):
    pass


class ImageFilter(impellerpy.ImageFilter_):
    pass


class MaskFilter(impellerpy.MaskFilter_):
    pass


class Paint(impellerpy.Paint_):
    pass


class DisplayList(impellerpy.DisplayList_):
    pass


class Path(impellerpy.Path_):
    pass


class LineMetrics(impellerpy.LineMetrics_):
    pass


class GlyphInfo(impellerpy.GlyphInfo_):
    pass


class Paragraph(impellerpy.Paragraph_):
    pass


class Texture(impellerpy.Texture_):
    pass


class DisplayListBuilder(impellerpy.DisplayListBuilder_):
    pass


class PathBuilder(impellerpy.PathBuilder_):
    pass


class Surface(impellerpy.Surface_):
    pass


class Context(impellerpy.Context_):
    pass


class Window(impellerpy.Window_):
    pass
