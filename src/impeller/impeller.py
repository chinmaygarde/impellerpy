from . import impellerpy


class Rect(impellerpy.Rect_):
    pass


class Point(impellerpy.Point_):
    pass


class Size(impellerpy.Size_):
    pass


class ISize(impellerpy.ISize_):
    pass


class Range(impellerpy.Range_):
    pass


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
    pass


class Mapping(impellerpy.Mapping_):
    pass


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
