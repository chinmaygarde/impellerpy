from enum import Enum
from typing import Optional, Sequence, Callable, Any

def get_version() -> int: ...

class FillType_(Enum):
    NON_ZERO = 0
    ODD = 1

class ClipOperation_(Enum):
    DIFFERENCE = 0
    INTERSECT = 1

class BlendMode_(Enum):
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

class DrawStyle_(Enum):
    FILL = 0
    STROKE = 1
    STROKE_AND_FILL = 2

class StrokeCap_(Enum):
    BUTT = 0
    ROUND = 1
    SQUARE = 2

class StrokeJoin_(Enum):
    MITER = 0
    ROUND = 1
    BEVEL = 2

class PixelFormat_(Enum):
    RGBA8888 = 0

class TextureSampling_(Enum):
    NEAREST_NEIGHBOR = 0
    LINEAR = 1

class TileMode_(Enum):
    CLAMP = 0
    REPEAT = 1
    MIRROR = 2
    DECAL = 3

class BlurStyle_(Enum):
    NORMAL = 0
    SOLID = 1
    OUTER = 2
    INNER = 3

class ColorSpace_(Enum):
    SRGB = 0
    EXTENDED_SRGB = 1
    DISPLAY_P3 = 2

class FontWeight_(Enum):
    W100 = 0
    W200 = 1
    W300 = 2
    W400 = 3
    W500 = 4
    W600 = 5
    W700 = 6
    W800 = 7
    W900 = 8

class FontStyle_(Enum):
    NORMAL = 0
    ITALIC = 1

class TextAlignment_(Enum):
    LEFT = 0
    RIGHT = 1
    CENTER = 2
    JUSTIFY = 3
    START = 4
    END = 5

class TextDirection_(Enum):
    RTL = 0
    LTR = 1

class ContextBackend_(Enum):
    OPENGLES = 0
    METAL = 1
    VULKAN = 2

class Rect_:
    x: float
    y: float
    width: float
    height: float

    def __init__(self) -> None: ...

class Point_:
    x: float
    y: float

    def __init__(self) -> None: ...

class Size_:
    width: float
    height: float

    def __init__(self) -> None: ...

class ISize_:
    width: int
    height: int

    def __init__(self) -> None: ...

class Range_:
    start: int
    end: int

    def __init__(self) -> None: ...

class Matrix_:
    m: Sequence[float]  # Assuming a 1D sequence for the matrix

    def __init__(self) -> None: ...

class ColorMatrix_:
    m: Sequence[float]  # Assuming a 1D sequence for the matrix

    def __init__(self) -> None: ...

class RoundingRadii_:
    top_left: Point_
    bottom_left: Point_
    top_right: Point_
    bottom_right: Point_

    def __init__(self) -> None: ...

class Color_:
    red: float
    green: float
    blue: float
    alpha: float
    color_space: ColorSpace_

    def __init__(self) -> None: ...

class TextureDescriptor_:
    pixel_format: PixelFormat_
    size: ISize_
    mip_count: int

    def __init__(self) -> None: ...

class Mapping_:
    data: bytes  # Or a more specific buffer type if needed
    length: int
    # on_release: Optional[Callable[[Optional[Any]], None]]  # Callback type
    def __init__(self) -> None: ...

class ContextVulkanSettings_:
    user_data: Optional[Any]  # Void pointer, so use Any

    proc_address_callback: Optional[
        Callable[[str, Optional[Any]], Optional[Any]]
    ]  # Callback type

    enable_vulkan_validation: bool

    def __init__(self) -> None: ...

class ContextVulkanInfo_:
    vk_instance: Optional[Any]  # Void pointer

    vk_physical_device: Optional[Any]  # Void pointer

    vk_logical_device: Optional[Any]  # Void pointer

    graphics_queue_family_index: int

    graphics_queue_index: int

    def __init__(self) -> None: ...

class ColorFilter_:
    pass

class ColorSource_:
    pass

class ImageFilter_:
    pass

class MaskFilter_:
    pass

class Paint_:
    def __init__(self) -> None: ...
    def set_color(self, color: Color_) -> Paint_: ...
    def set_blend_mode(self, blend_mode: BlendMode_) -> Paint_: ...
    def set_draw_style(self, style: DrawStyle_) -> Paint_: ...
    def set_stroke_cap(self, cap: StrokeCap_) -> Paint_: ...
    def set_stroke_join(self, join: StrokeJoin_) -> Paint_: ...
    def set_stroke_width(self, width: float) -> Paint_: ...
    def set_stroke_miter(self, miter: float) -> Paint_: ...
    def set_color_filter(self, filter: ColorFilter_) -> Paint_: ...
    def set_color_source(self, source: ColorSource_) -> Paint_: ...
    def set_image_filter(self, filter: ImageFilter_) -> Paint_: ...
    def set_mask_filter(self, filter: MaskFilter_) -> Paint_: ...

class DisplayList_:
    # Done
    pass

class Path_:
    # Done
    pass

class LineMetrics_:
    pass

class GlyphInfo_:
    pass

class Paragraph_:
    def alphabetic_baseline(self) -> float: ...
    def height(self) -> float: ...
    def ideographic_baseline(self) -> float: ...
    def line_count(self) -> int: ...
    def longest_line_width(self) -> float: ...
    def max_intrinsic_width(self) -> float: ...
    def max_width(self) -> float: ...
    def min_intrinsic_width(self) -> float: ...
    def line_metrics(self) -> LineMetrics_: ...
    def glyph_info_at_code_unit_index(
        self, code_unit_index: int
    ) -> GlyphInfo_: ...
    def glyph_info_at_paragraph_coordinate(
        self, x: float, y: float
    ) -> GlyphInfo_: ...
    def word_boundary(self, code_unit_index: int) -> Range_: ...

class Texture_:
    @staticmethod
    def with_contents(
        context: Context_, desc: TextureDescriptor_, data: Mapping_
    ) -> Texture_: ...

class DisplayListBuilder_:
    def __init__(self) -> None: ...
    def build(self) -> DisplayList_: ...
    def clip_oval(
        self, rect: Rect_, op: ClipOperation_
    ) -> DisplayListBuilder_: ...
    def clip_path(
        self, path: Path_, op: ClipOperation_
    ) -> DisplayListBuilder_: ...
    def clip_rect(
        self, rect: Rect_, op: ClipOperation_
    ) -> DisplayListBuilder_: ...
    def clip_rounded_rect(
        self, rect: Rect_, radii: RoundingRadii_, op: ClipOperation_
    ) -> DisplayListBuilder_: ...
    def draw_dashed_line(
        self,
        from_point: Point_,
        to_point: Point_,
        on_length: float,
        off_length: float,
        paint: Paint_,
    ) -> DisplayListBuilder_: ...
    def draw_display_list(
        self, dl: DisplayList_, opacity: float
    ) -> DisplayListBuilder_: ...
    def draw_line(
        self, from_point: Point_, to_point: Point_, paint: Paint_
    ) -> DisplayListBuilder_: ...
    def draw_oval(
        self, oval_bounds: Rect_, paint: Paint_
    ) -> DisplayListBuilder_: ...
    def draw_paint(self, paint: Paint_) -> DisplayListBuilder_: ...
    def draw_paragraph(
        self, paragraph: Paragraph_, paint: Paint_
    ) -> DisplayListBuilder_: ...
    def draw_shadow(
        self,
        path: Path_,
        shadow_color: Color_,
        elevation: float,
        occuluder_is_transparent: bool,
        device_pixel_ratio: float,
    ) -> DisplayListBuilder_: ...
    def draw_path(self, path: Path_, paint: Paint_) -> DisplayListBuilder_: ...
    def draw_rect(self, rect: Rect_, paint: Paint_) -> DisplayListBuilder_: ...
    def draw_rounded_rect(
        self, rect: Rect_, radii: RoundingRadii_, paint: Paint_
    ) -> DisplayListBuilder_: ...
    def draw_rounded_rect_difference(
        self,
        outer_rect: Rect_,
        outer_radii: RoundingRadii_,
        inner_rect: Rect_,
        inner_radii: RoundingRadii_,
        paint: Paint_,
    ) -> DisplayListBuilder_: ...
    def draw_texture(
        self,
        texture: Texture_,
        point: Point_,
        sampling: TextureSampling_,
        paint: Paint_,
    ) -> DisplayListBuilder_: ...
    def draw_texture_rect(
        self,
        texture: Texture_,
        src_rect: Rect_,
        dst_rect: Rect_,
        sampling: TextureSampling_,
        paint: Paint_,
    ) -> DisplayListBuilder_: ...
    def save_count(self) -> int: ...
    def reset_transform(self) -> DisplayListBuilder_: ...
    def restore(self) -> DisplayListBuilder_: ...
    def restore_to_count(self, count: int) -> DisplayListBuilder_: ...
    def rotate(self, angle_in_degrees: float) -> DisplayListBuilder_: ...
    def save(self) -> DisplayListBuilder_: ...
    def save_layer(
        self, paint: Optional[Paint_], backdrop: Optional[ImageFilter_]
    ) -> DisplayListBuilder_: ...
    def scale(self, x: float, y: float) -> DisplayListBuilder_: ...
    def get_transform(self) -> Matrix_: ...
    def set_transform(self, xform: Matrix_) -> DisplayListBuilder_: ...
    def push_transform(self, xform: Matrix_) -> DisplayListBuilder_: ...
    def translate(self, x: float, y: float) -> DisplayListBuilder_: ...

class PathBuilder_:
    def __init__(self) -> None: ...
    def build_copy(self, fill: FillType_) -> Path_: ...
    def build(self, fill: FillType_) -> Path_: ...
    def add_arc(
        self, start_degrees: float, end_degrees: float
    ) -> PathBuilder_: ...
    def add_oval(self, oval_bounds: Rect_) -> PathBuilder_: ...
    def add_rect(self, rect: Rect_) -> PathBuilder_: ...
    def add_rounded_rect(
        self, rect: Rect_, radii: RoundingRadii_
    ) -> PathBuilder_: ...
    def close(self) -> PathBuilder_: ...
    def cubic_curve_to(
        self, cp1: Point_, cp2: Point_, end: Point_
    ) -> PathBuilder_: ...
    def line_to(self, location: Point_) -> PathBuilder_: ...
    def move_to(self, location: Point_) -> PathBuilder_: ...
    def quadratic_curve_to(self, cp: Point_, end: Point_) -> PathBuilder_: ...

class Surface_:
    def draw(self, dl: DisplayList_) -> bool: ...
    def present(self) -> bool: ...

class Context_:
    def __init__(self, backend: ContextBackend_) -> None: ...

class Window_:
    def create_render_surface(self, context: Context_) -> Surface_: ...
    def should_close(self) -> bool: ...
    def poll_events(self) -> None: ...

def get_main_window() -> Window_: ...
