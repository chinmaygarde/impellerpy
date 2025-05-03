from typing import List
from .impellerpy import *

class Rect(Rect_):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
        width: float = 0,
        height: float = 0,
    ):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Point(Point_):
    def __init__(
        self,
        x: float = 0,
        y: float = 0,
    ):
        super().__init__()
        self.x = x
        self.y = y


class Size(Size_):
    def __init__(self, width: float = 0, height: float = 0):
        super().__init__()
        self.width = width
        self.height = height


class ISize(ISize_):
    def __init__(self, width: int = 0, height: int = 0):
        super().__init__()
        self.width = width
        self.height = height


class Range(Range_):
    def __init__(self, start: int = 0, end: int = 0):
        super().__init__()
        self.start = start
        self.end = end


class Matrix(Matrix_):
    def __init__(self, row_col_list: List[List[float]]):
        values = []
        for col in range(4):
            for row in range(4):
                values.append(row_col_list[col][row])
        super().__init__(values)


class ColorMatrix(ColorMatrix_):
    pass


class RoundingRadii(RoundingRadii_):
    pass


class Color(Color_):
    def __init__(
        self,
        r: float = 0.0,
        g: float = 0.0,
        b: float = 0.0,
        a: float = 0.0,
    ):
        super().__init__()
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a


class TextureDescriptor(TextureDescriptor_):
    def __init__(
        self,
        pixel_format: PixelFormat,
        texture_size: ISize,
        mip_count: int = 1,
    ):
        super().__init__()
        self.pixel_format = pixel_format
        self.size = texture_size
        self.mip_count = mip_count


class ColorFilter(ColorFilter_):
    pass


class ColorSource(ColorSource_):
    pass


class ImageFilter(ImageFilter_):
    pass


class MaskFilter(MaskFilter_):
    pass


class Paint(Paint_):
    pass


class DisplayList(DisplayList_):
    pass


class Path(Path_):
    pass


class LineMetrics(LineMetrics_):
    pass


class GlyphInfo(GlyphInfo_):
    pass


class Paragraph(Paragraph_):
    pass


class Texture(Texture_):
    pass


class DisplayListBuilder(DisplayListBuilder_):
    pass


class PathBuilder(PathBuilder_):
    pass


class Surface(Surface_):
    pass


class Context(Context_):
    pass


class Window(Window_):
    def __init__(self):
        super().__init__()


class TypographyContext(TypographyContext_):
    pass


class ParagraphStyle(ParagraphStyle_):
    pass


class ParagraphBuilder(ParagraphBuilder_):
    pass
