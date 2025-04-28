from enum import Enum
from typing import Optional, Sequence, Callable, Any

def get_version() -> int: ...

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

class ContextBackend(Enum):
    OPENGLES = 0
    METAL = 1
    VULKAN = 2

class Rect:
    x: float
    y: float
    width: float
    height: float

    def __init__(self) -> None: ...

class Point:
    x: float
    y: float

    def __init__(self) -> None: ...

class Size:
    width: float
    height: float

    def __init__(self) -> None: ...

class ISize:
    width: int
    height: int

    def __init__(self) -> None: ...

class Range:
    start: int
    end: int

    def __init__(self) -> None: ...

class Matrix:
    m: Sequence[float]  # Assuming a 1D sequence for the matrix

    def __init__(self) -> None: ...

class ColorMatrix:
    m: Sequence[float]  # Assuming a 1D sequence for the matrix

    def __init__(self) -> None: ...

class RoundingRadii:
    top_left: Point
    bottom_left: Point
    top_right: Point
    bottom_right: Point

    def __init__(self) -> None: ...

class Color:
    red: float
    green: float
    blue: float
    alpha: float
    color_space: ColorSpace

    def __init__(self) -> None: ...

class TextureDescriptor:
    pixel_format: PixelFormat
    size: ISize
    mip_count: int

    def __init__(self) -> None: ...

class Mapping:
    data: bytes  # Or a more specific buffer type if needed
    length: int
    on_release: Optional[Callable[[Optional[Any]], None]]  # Callback type

    def __init__(self) -> None: ...

class ContextVulkanSettings:
    user_data: Optional[Any]  # Void pointer, so use Any

    proc_address_callback: Optional[
        Callable[[str, Optional[Any]], Optional[Any]]
    ]  # Callback type

    enable_vulkan_validation: bool

    def __init__(self) -> None: ...

class ContextVulkanInfo:
    vk_instance: Optional[Any]  # Void pointer

    vk_physical_device: Optional[Any]  # Void pointer

    vk_logical_device: Optional[Any]  # Void pointer

    graphics_queue_family_index: int

    graphics_queue_index: int

    def __init__(self) -> None: ...

class ColorFilter:
    pass

class ColorSource:
    pass

class ImageFilter:
    pass

class MaskFilter:
    pass

class Paint:
    def __init__(self) -> None: ...
    def set_color(self, color: Color) -> Paint: ...
    def set_blend_mode(self, blend_mode: BlendMode) -> Paint: ...
    def set_draw_style(self, style: DrawStyle) -> Paint: ...
    def set_stroke_cap(self, cap: StrokeCap) -> Paint: ...
    def set_stroke_join(self, join: StrokeJoin) -> Paint: ...
    def set_stroke_width(self, width: float) -> Paint: ...
    def set_stroke_miter(self, miter: float) -> Paint: ...
    def set_color_filter(self, filter: ColorFilter) -> Paint: ...
    def set_color_source(self, source: ColorSource) -> Paint: ...
    def set_image_filter(self, filter: ImageFilter) -> Paint: ...
    def set_mask_filter(self, filter: MaskFilter) -> Paint: ...

class DisplayList:
    # Done
    pass

class Path:
    # Done
    pass

class LineMetrics:
    pass

class GlyphInfo:
    pass

class Paragraph:
    def alphabetic_baseline(self) -> float: ...
    def height(self) -> float: ...
    def ideographic_baseline(self) -> float: ...
    def line_count(self) -> int: ...
    def longest_line_width(self) -> float: ...
    def max_intrinsic_width(self) -> float: ...
    def max_width(self) -> float: ...
    def min_intrinsic_width(self) -> float: ...
    def line_metrics(self) -> LineMetrics: ...
    def glyph_info_at_code_unit_index(
        self, code_unit_index: int
    ) -> GlyphInfo: ...
    def glyph_info_at_paragraph_coordinate(
        self, x: float, y: float
    ) -> GlyphInfo: ...
    def word_boundary(self, code_unit_index: int) -> Range: ...

class Texture:
    # Done
    pass

class DisplayListBuilder:
    def __init__(self) -> None: ...
    def build(self) -> DisplayList: ...
    def clip_oval(
        self, rect: Rect, op: ClipOperation
    ) -> DisplayListBuilder: ...
    def clip_path(
        self, path: Path, op: ClipOperation
    ) -> DisplayListBuilder: ...
    def clip_rect(
        self, rect: Rect, op: ClipOperation
    ) -> DisplayListBuilder: ...
    def clip_rounded_rect(
        self, rect: Rect, radii: RoundingRadii, op: ClipOperation
    ) -> DisplayListBuilder: ...
    def draw_dashed_line(
        self,
        from_point: Point,
        to_point: Point,
        on_length: float,
        off_length: float,
        paint: Paint,
    ) -> DisplayListBuilder: ...
    def draw_display_list(
        self, dl: DisplayList, opacity: float
    ) -> DisplayListBuilder: ...
    def draw_line(
        self, from_point: Point, to_point: Point, paint: Paint
    ) -> DisplayListBuilder: ...
    def draw_oval(
        self, oval_bounds: Rect, paint: Paint
    ) -> DisplayListBuilder: ...
    def draw_paint(self, paint: Paint) -> DisplayListBuilder: ...
    def draw_paragraph(
        self, paragraph: Paragraph, paint: Paint
    ) -> DisplayListBuilder: ...
    def draw_shadow(
        self,
        path: Path,
        shadow_color: Color,
        elevation: float,
        occuluder_is_transparent: bool,
        device_pixel_ratio: float,
    ) -> DisplayListBuilder: ...
    def draw_path(self, path: Path, paint: Paint) -> DisplayListBuilder: ...
    def draw_rect(self, rect: Rect, paint: Paint) -> DisplayListBuilder: ...
    def draw_rounded_rect(
        self, rect: Rect, radii: RoundingRadii, paint: Paint
    ) -> DisplayListBuilder: ...
    def draw_rounded_rect_difference(
        self,
        outer_rect: Rect,
        outer_radii: RoundingRadii,
        inner_rect: Rect,
        inner_radii: RoundingRadii,
        paint: Paint,
    ) -> DisplayListBuilder: ...
    def draw_texture(
        self,
        texture: Texture,
        point: Point,
        sampling: TextureSampling,
        paint: Paint,
    ) -> DisplayListBuilder: ...
    def draw_texture_rect(
        self,
        texture: Texture,
        src_rect: Rect,
        dst_rect: Rect,
        sampling: TextureSampling,
        paint: Paint,
    ) -> DisplayListBuilder: ...
    def save_count(self) -> int: ...
    def reset_transform(self) -> DisplayListBuilder: ...
    def restore(self) -> DisplayListBuilder: ...
    def restore_to_count(self, count: int) -> DisplayListBuilder: ...
    def rotate(self, angle_in_degrees: float) -> DisplayListBuilder: ...
    def save(self) -> DisplayListBuilder: ...
    def save_layer(
        self, paint: Optional[Paint], backdrop: Optional[ImageFilter]
    ) -> DisplayListBuilder: ...
    def scale(self, x: float, y: float) -> DisplayListBuilder: ...
    def get_transform(self) -> Matrix: ...
    def set_transform(self, xform: Matrix) -> DisplayListBuilder: ...
    def push_transform(self, xform: Matrix) -> DisplayListBuilder: ...
    def translate(self, x: float, y: float) -> DisplayListBuilder: ...

class PathBuilder:
    def __init__(self) -> None: ...
    def build_copy(self, fill: FillType) -> Path: ...
    def build(self, fill: FillType) -> Path: ...
    def add_arc(
        self, start_degrees: float, end_degrees: float
    ) -> PathBuilder: ...
    def add_oval(self, oval_bounds: Rect) -> PathBuilder: ...
    def add_rect(self, rect: Rect) -> PathBuilder: ...
    def add_rounded_rect(
        self, rect: Rect, radii: RoundingRadii
    ) -> PathBuilder: ...
    def close(self) -> PathBuilder: ...
    def cubic_curve_to(
        self, cp1: Point, cp2: Point, end: Point
    ) -> PathBuilder: ...
    def line_to(self, location: Point) -> PathBuilder: ...
    def move_to(self, location: Point) -> PathBuilder: ...
    def quadratic_curve_to(self, cp: Point, end: Point) -> PathBuilder: ...

class Surface:
    def draw(self, dl: DisplayList) -> bool: ...
    def present(self) -> bool: ...

class Context:
    def __init__(self, backend: ContextBackend) -> None: ...

class Window:
    def create_render_surface(self, context: Context) -> Surface: ...
    def should_close(self) -> bool: ...
    def poll_events(self) -> None: ...

def get_main_window() -> Window: ...
