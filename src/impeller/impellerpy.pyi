from enum import Enum

def get_version() -> int:
  ...

class FillType(Enum):
    NON_ZERO = 0
    ODD = 1

class ClipOperation(Enum):
    DIFFERENCE = 0
    INTERSECT = 1

class BlendMode(Enum):
    CLEAR = 0
    SOURCE = 1
    DESTINATION = 2
    SOURCE_OVER = 3
    DESTINATION_OVER = 4
    SOURCE_IN = 5
    DESTINATION_IN = 6
    SOURCE_OUT = 7
    DESTINATION_OUT = 8
    SOURCE_ATOP = 9
    DESTINATION_ATOP = 10
    XOR = 11
    PLUS = 12
    MODULATE = 13
    SCREEN = 14
    OVERLAY = 15
    DARKEN = 16
    LIGHTEN = 17
    COLOR_DODGE = 18
    COLOR_BURN = 19
    HARD_LIGHT = 20
    SOFT_LIGHT = 21
    DIFFERENCE = 22
    EXCLUSION = 23
    MULTIPLY = 24
    HUE = 25
    SATURATION = 26
    COLOR = 27
    LUMINOSITY = 28

class DrawStyle(Enum):
    FILL = 0
    STROKE = 1
    STROKE_AND_FILL = 2

class StrokeCap(Enum):
    BUTT = 0
    ROUND = 1
    SQUARE = 2

class StrokeJoin(Enum):
    MITER = 0
    ROUND = 1
    BEVEL = 2

class PixelFormat(Enum):
    RGBA8888 = 0

class TextureSampling(Enum):
    NEAREST_NEIGHBOR = 0
    LINEAR = 1

class TileMode(Enum):
    CLAMP = 0
    REPEAT = 1
    MIRROR = 2
    DECAL = 3

class BlurStyle(Enum):
    NORMAL = 0
    SOLID = 1
    OUTER = 2
    INNER = 3

class ColorSpace(Enum):
    SRGB = 0
    EXTENDED_SRGB = 1
    DISPLAY_P3 = 2

class FontWeight(Enum):
    W100 = 0
    W200 = 1
    W300 = 2
    W400 = 3
    W500 = 4
    W600 = 5
    W700 = 6
    W800 = 7
    W900 = 8

class FontStyle(Enum):
    NORMAL = 0
    ITALIC = 1

class TextAlignment(Enum):
    LEFT = 0
    RIGHT = 1
    CENTER = 2
    JUSTIFY = 3
    START = 4
    END = 5

class TextDirection(Enum):
    RTL = 0
    LTR = 1
