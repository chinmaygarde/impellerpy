from enum import Enum
from typing import List, Optional, Tuple, Union

def get_version() -> int:
    """
    Get the version of Impeller standalone API.
    
    This is the API version that will be accepted for validity checks when provided to the
    context creation methods. The current version of the API is denoted by the
    `IMPELLER_VERSION` macro.
    
    Returns:
        The version of the standalone API.
    """
    ...

class FillType(Enum):
    """
    Determines how overlapping contours in a path are filled.
    
    NON_ZERO: Uses the non-zero winding rule for filling paths.
    ODD: Uses the even-odd rule for filling paths.
    """
    NON_ZERO = 0
    ODD = 1

class ClipOperation(Enum):
    """
    Determines how clip regions are combined.
    
    DIFFERENCE: Subtracts the new clip region from the current clip.
    INTERSECT: Intersects the new clip region with the current clip.
    """
    DIFFERENCE = 0
    INTERSECT = 1

class BlendMode(Enum):
    """
    Determines how source and destination colors are combined during drawing.
    
    These blend modes follow the standard Porter-Duff compositing operations
    and additional blend modes from PDF and SVG specifications.
    """
    CLEAR = 0            # Clear destination (0)
    SOURCE = 1           # Copy source (S)
    DESTINATION = 2      # Preserve destination (D)
    SOURCE_OVER = 3      # Source over destination (S + (1-Sa)*D)
    DESTINATION_OVER = 4 # Destination over source (D + (1-Da)*S)
    SOURCE_IN = 5        # Source where destination is non-zero (Da*S)
    DESTINATION_IN = 6   # Destination where source is non-zero (Sa*D)
    SOURCE_OUT = 7       # Source where destination is zero ((1-Da)*S)
    DESTINATION_OUT = 8  # Destination where source is zero ((1-Sa)*D)
    SOURCE_ATOP = 9      # Source atop destination (Da*S + (1-Sa)*D)
    DESTINATION_ATOP = 10 # Destination atop source (Sa*D + (1-Da)*S)
    XOR = 11             # Exclusive OR ((1-Sa)*D + (1-Da)*S)
    PLUS = 12            # Sum of source and destination (S + D)
    MODULATE = 13        # Product of source and destination (S*D)
    SCREEN = 14          # Screen blend mode
    OVERLAY = 15         # Overlay blend mode
    DARKEN = 16          # Darker of source and destination
    LIGHTEN = 17         # Lighter of source and destination
    COLOR_DODGE = 18     # Brightens destination based on source
    COLOR_BURN = 19      # Darkens destination based on source
    HARD_LIGHT = 20      # Hard light blend mode
    SOFT_LIGHT = 21      # Soft light blend mode
    DIFFERENCE = 22      # Absolute difference between source and destination
    EXCLUSION = 23       # Similar to DIFFERENCE but with lower contrast
    MULTIPLY = 24        # Multiply source and destination
    HUE = 25             # Hue from source, saturation and luminosity from destination
    SATURATION = 26      # Saturation from source, hue and luminosity from destination
    COLOR = 27           # Hue and saturation from source, luminosity from destination
    LUMINOSITY = 28      # Luminosity from source, hue and saturation from destination

class DrawStyle(Enum):
    """
    Determines how shapes are rendered.
    
    FILL: Fill the shape with the paint.
    STROKE: Stroke the outline of the shape with the paint.
    STROKE_AND_FILL: Both fill and stroke the shape with the paint.
    """
    FILL = 0
    STROKE = 1
    STROKE_AND_FILL = 2

class StrokeCap(Enum):
    """
    Determines how the ends of stroked lines are rendered.
    
    BUTT: End the stroke at the path's endpoint.
    ROUND: End the stroke with a semicircle at the path's endpoint.
    SQUARE: End the stroke with a square at the path's endpoint.
    """
    BUTT = 0
    ROUND = 1
    SQUARE = 2

class StrokeJoin(Enum):
    """
    Determines how corners in stroked paths are rendered.
    
    MITER: Join segments with a sharp corner.
    ROUND: Join segments with a rounded corner.
    BEVEL: Join segments with a flat corner.
    """
    MITER = 0
    ROUND = 1
    BEVEL = 2

class PixelFormat(Enum):
    """
    Specifies the format of pixels in textures and surfaces.
    
    RGBA8888: 8 bits per channel, red, green, blue, alpha.
    """
    RGBA8888 = 0

class TextureSampling(Enum):
    """
    Determines how textures are sampled when drawn.
    
    NEAREST_NEIGHBOR: Use the nearest pixel value.
    LINEAR: Interpolate between neighboring pixels.
    """
    NEAREST_NEIGHBOR = 0
    LINEAR = 1

class TileMode(Enum):
    """
    Determines how textures and gradients behave outside their bounds.
    
    CLAMP: Use the color at the nearest edge.
    REPEAT: Repeat the texture or gradient.
    MIRROR: Repeat the texture or gradient, mirroring on each repetition.
    DECAL: Use transparent black outside the bounds.
    """
    CLAMP = 0
    REPEAT = 1
    MIRROR = 2
    DECAL = 3

class BlurStyle(Enum):
    """
    Determines how blur mask filters are applied.
    
    NORMAL: Blur in all directions.
    SOLID: Blur and preserve the original shape.
    OUTER: Blur only outside the shape.
    INNER: Blur only inside the shape.
    """
    NORMAL = 0
    SOLID = 1
    OUTER = 2
    INNER = 3

class ColorSpace(Enum):
    """
    Specifies the color space for colors.
    
    SRGB: Standard RGB color space.
    EXTENDED_SRGB: Extended sRGB color space with values outside [0,1].
    DISPLAY_P3: Display P3 color space with wider gamut than sRGB.
    """
    SRGB = 0
    EXTENDED_SRGB = 1
    DISPLAY_P3 = 2

class FontWeight(Enum):
    """
    Specifies the weight (boldness) of a font.
    
    W100: Thin
    W200: Extra-Light
    W300: Light
    W400: Normal/Regular
    W500: Medium
    W600: Semi-bold
    W700: Bold
    W800: Extra-Bold
    W900: Black
    """
    W100 = 0  # Thin
    W200 = 1  # Extra-Light
    W300 = 2  # Light
    W400 = 3  # Normal/Regular
    W500 = 4  # Medium
    W600 = 5  # Semi-bold
    W700 = 6  # Bold
    W800 = 7  # Extra-Bold
    W900 = 8  # Black

class FontStyle(Enum):
    """
    Specifies the style of a font.
    
    NORMAL: Regular font style.
    ITALIC: Italic font style.
    """
    NORMAL = 0
    ITALIC = 1

class TextAlignment(Enum):
    """
    Specifies the horizontal alignment of text.
    
    LEFT: Align text to the left.
    RIGHT: Align text to the right.
    CENTER: Center text horizontally.
    JUSTIFY: Stretch text to fill the width.
    START: Align text to the start of the line (depends on text direction).
    END: Align text to the end of the line (depends on text direction).
    """
    LEFT = 0
    RIGHT = 1
    CENTER = 2
    JUSTIFY = 3
    START = 4
    END = 5

class TextDirection(Enum):
    """
    Specifies the direction of text flow.
    
    RTL: Right-to-left text direction.
    LTR: Left-to-right text direction.
    """
    RTL = 0
    LTR = 1

class Rect_:
    """
    Represents a rectangle with position and size.
    
    Attributes:
        x: The x-coordinate of the top-left corner.
        y: The y-coordinate of the top-left corner.
        width: The width of the rectangle.
        height: The height of the rectangle.
    """
    x: float
    y: float
    width: float
    height: float

    def __init__(self) -> None: 
        """Initialize a rectangle with default values (0,0,0,0)."""
        ...

class Point_:
    """
    Represents a 2D point with x and y coordinates.
    
    Attributes:
        x: The x-coordinate of the point.
        y: The y-coordinate of the point.
    """
    x: float
    y: float

    def __init__(self) -> None: 
        """Initialize a point with default values (0,0)."""
        ...

class Size_:
    """
    Represents a 2D size with width and height.
    
    Attributes:
        width: The width component of the size.
        height: The height component of the size.
    """
    width: float
    height: float

    def __init__(self) -> None: 
        """Initialize a size with default values (0,0)."""
        ...

class ISize_:
    """
    Represents a 2D size with integer width and height.
    
    Attributes:
        width: The width component of the size (integer).
        height: The height component of the size (integer).
    """
    width: int
    height: int

    def __init__(self) -> None: 
        """Initialize an integer size with default values (0,0)."""
        ...

class Range_:
    """
    Represents a range of values from start to end.
    
    Attributes:
        start: The start index of the range.
        end: The end index of the range.
    """
    start: int
    end: int

    def __init__(self) -> None: 
        """Initialize a range with default values (0,0)."""
        ...

class Matrix_:
    """
    A 4x4 transformation matrix using column-major storage.
    
    The matrix is stored as:
    | m[0] m[4] m[8]  m[12] |
    | m[1] m[5] m[9]  m[13] |
    | m[2] m[6] m[10] m[14] |
    | m[3] m[7] m[11] m[15] |
    """
    def __init__(
        self,
        values: List[float],
    ) -> None: 
        """
        Initialize a matrix with the provided values.
        
        Args:
            values: A list of 16 float values in column-major order.
        """
        ...
    
    def __getitem__(
        self,
        key: int,
    ) -> float: 
        """
        Get the value at the specified index.
        
        Args:
            key: The index (0-15) to retrieve.
            
        Returns:
            The float value at the specified index.
        """
        ...
    
    def __setitem__(
        self,
        key: int,
        value: float,
    ) -> None: 
        """
        Set the value at the specified index.
        
        Args:
            key: The index (0-15) to modify.
            value: The new float value to set.
        """
        ...
    
    def to_list(self) -> List[float]: 
        """
        Convert the matrix to a list of float values.
        
        Returns:
            A list of 16 float values representing the matrix in column-major order.
        """
        ...

class ColorMatrix_:
    """
    A 4x5 color transformation matrix used for transforming color values.
    
    The matrix is used to transform RGBA colors using the formula:
    | R' |   | m[0]  m[1]  m[2]  m[3]  m[4]  |   | R |
    | G' |   | m[5]  m[6]  m[7]  m[8]  m[9]  |   | G |
    | B' | = | m[10] m[11] m[12] m[13] m[14] | * | B |
    | A' |   | m[15] m[16] m[17] m[18] m[19] |   | A |
    | 1  |   | 0     0     0     0     1     |   | 1 |
    """
    def __init__(
        self,
        values: List[float],
    ) -> None: 
        """
        Initialize a color matrix with the provided values.
        
        Args:
            values: A list of 20 float values representing the 4x5 color matrix.
        """
        ...
    
    def __getitem__(
        self,
        key: int,
    ) -> float: 
        """
        Get the value at the specified index.
        
        Args:
            key: The index (0-19) to retrieve.
            
        Returns:
            The float value at the specified index.
        """
        ...
    
    def __setitem__(
        self,
        key: int,
        value: float,
    ) -> None: 
        """
        Set the value at the specified index.
        
        Args:
            key: The index (0-19) to modify.
            value: The new float value to set.
        """
        ...
    
    def to_list(self) -> List[float]: 
        """
        Convert the color matrix to a list of float values.
        
        Returns:
            A list of 20 float values representing the color matrix.
        """
        ...

class RoundingRadii_:
    """
    Specifies the radii for rounded corners of a rectangle.
    
    Attributes:
        top_left: The radius for the top-left corner.
        bottom_left: The radius for the bottom-left corner.
        top_right: The radius for the top-right corner.
        bottom_right: The radius for the bottom-right corner.
    """
    top_left: Point_
    bottom_left: Point_
    top_right: Point_
    bottom_right: Point_

    def __init__(self) -> None: 
        """Initialize rounding radii with default values (all corners set to 0,0)."""
        ...

class Color_:
    """
    Represents a color with red, green, blue, and alpha components.
    
    Attributes:
        red: The red component (0.0 to 1.0).
        green: The green component (0.0 to 1.0).
        blue: The blue component (0.0 to 1.0).
        alpha: The alpha component (0.0 to 1.0).
        color_space: The color space of the color.
    """
    red: float
    green: float
    blue: float
    alpha: float
    color_space: ColorSpace

    def __init__(self) -> None: 
        """Initialize a color with default values (0,0,0,0) in sRGB color space."""
        ...

class TextureDescriptor_:
    """
    Describes the properties of a texture.
    
    Attributes:
        pixel_format: The format of pixels in the texture.
        size: The dimensions of the texture in pixels.
        mip_count: The number of mipmap levels in the texture.
    """
    pixel_format: PixelFormat
    size: ISize_
    mip_count: int

    def __init__(self) -> None: 
        """Initialize a texture descriptor with default values."""
        ...

class ColorFilter_:
    """
    A filter that transforms colors before they are drawn.
    
    Color filters are functions that take two colors and mix them to produce a
    single color. This color is then merged with the destination during blending.
    """
    @staticmethod
    def blend(
        color: Color_,
        blend_mode: BlendMode,
    ) -> ColorFilter_: 
        """
        Create a color filter that performs blending of pixel values independently.
        
        Args:
            color: The color to blend with.
            blend_mode: The blend mode to use for combining colors.
            
        Returns:
            A new color filter that performs the specified blending.
        """
        ...
    
    @staticmethod
    def matrix(
        matrix: ColorMatrix_,
    ) -> ColorFilter_: 
        """
        Create a color filter that transforms pixel color values independently.
        
        Args:
            matrix: The color matrix to use for transforming colors.
            
        Returns:
            A new color filter that applies the specified color matrix transformation.
        """
        ...

class ColorSource_:
    """
    A source of colors for drawing operations.
    
    Color sources are functions that generate colors for each texture element
    covered by a draw call. The colors can be generated using a mathematical
    function (to produce gradients) or sampled from a texture.
    """
    @staticmethod
    def conical_gradient(
        start_center: Point_,
        start_radius: float,
        end_center: Point_,
        end_radius: float,
        stops: List[float],
        colors: List[Color_],
        tile_mode: TileMode,
        transformation: Optional[Matrix_] = None,
    ) -> ColorSource_: 
        """
        Create a color source that forms a conical gradient.
        
        Args:
            start_center: The center point of the starting circle.
            start_radius: The radius of the starting circle.
            end_center: The center point of the ending circle.
            end_radius: The radius of the ending circle.
            stops: The positions of color stops (0.0 to 1.0).
            colors: The colors at each stop position.
            tile_mode: How to handle coordinates outside the gradient.
            transformation: Optional transformation matrix to apply.
            
        Returns:
            A new color source that generates a conical gradient.
        """
        ...
    
    @staticmethod
    def image(
        texture: Texture_,
        horizontal_tile_mode: TileMode,
        vertical_tile_mode: TileMode,
        sampling: TextureSampling,
        transformation: Optional[Matrix_] = None,
    ) -> ColorSource_: 
        """
        Create a color source that samples from an image.
        
        Args:
            texture: The texture to sample from.
            horizontal_tile_mode: How to handle coordinates outside the texture horizontally.
            vertical_tile_mode: How to handle coordinates outside the texture vertically.
            sampling: The sampling method to use when reading the texture.
            transformation: Optional transformation matrix to apply.
            
        Returns:
            A new color source that samples from the specified texture.
        """
        ...
    
    @staticmethod
    def linear_gradient(
        start_point: Point_,
        end_point: Point_,
        colors: List[Color_],
        stops: List[float],
        tile_mode: TileMode,
        transformation: Optional[Matrix_] = None,
    ) -> ColorSource_: 
        """
        Create a color source that forms a linear gradient.
        
        Args:
            start_point: The starting point of the gradient.
            end_point: The ending point of the gradient.
            colors: The colors at each stop position.
            stops: The positions of color stops (0.0 to 1.0).
            tile_mode: How to handle coordinates outside the gradient.
            transformation: Optional transformation matrix to apply.
            
        Returns:
            A new color source that generates a linear gradient.
        """
        ...
    
    @staticmethod
    def radial_gradient(
        center: Point_,
        radius: float,
        colors: List[Color_],
        stops: List[float],
        tile_mode: TileMode,
        transformation: Optional[Matrix_] = None,
    ) -> ColorSource_: 
        """
        Create a color source that forms a radial gradient.
        
        Args:
            center: The center point of the gradient.
            radius: The radius of the gradient.
            colors: The colors at each stop position.
            stops: The positions of color stops (0.0 to 1.0).
            tile_mode: How to handle coordinates outside the gradient.
            transformation: Optional transformation matrix to apply.
            
        Returns:
            A new color source that generates a radial gradient.
        """
        ...
    
    @staticmethod
    def sweep_gradient(
        center: Point_,
        start: float,
        end: float,
        colors: List[Color_],
        stops: List[float],
        tile_mode: TileMode,
        transformation: Optional[Matrix_] = None,
    ) -> ColorSource_: 
        """
        Create a color source that forms a sweep gradient.
        
        Args:
            center: The center point of the gradient.
            start: The starting angle in degrees.
            end: The ending angle in degrees.
            colors: The colors at each stop position.
            stops: The positions of color stops (0.0 to 1.0).
            tile_mode: How to handle coordinates outside the gradient.
            transformation: Optional transformation matrix to apply.
            
        Returns:
            A new color source that generates a sweep gradient.
        """
        ...

class ImageFilter_:
    """
    A filter that transforms images before they are drawn.
    
    Image filters are functions that are applied to regions of a texture to produce
    a single color. Contrast this with color filters that operate independently
    on a per-pixel basis.
    """
    @staticmethod
    def blur(
        x_sigma: float, y_sigma: float, tile_mode: TileMode
    ) -> ImageFilter_: 
        """
        Create an image filter that applies a Gaussian blur.
        
        The Gaussian blur applied may be an approximation for performance.
        
        Args:
            x_sigma: The standard deviation of the blur in the x direction.
            y_sigma: The standard deviation of the blur in the y direction.
            tile_mode: How to handle coordinates outside the source image.
            
        Returns:
            A new image filter that applies a Gaussian blur.
        """
        ...
    
    @staticmethod
    def compose(
        outer: ImageFilter_,
        inner: ImageFilter_,
    ) -> ImageFilter_: 
        """
        Create a composed filter that applies inner then outer filters.
        
        The resulting filter is equivalent to: destination = outer_filter(inner_filter(source))
        
        Args:
            outer: The outer image filter to apply second.
            inner: The inner image filter to apply first.
            
        Returns:
            A new image filter that applies both filters in sequence.
        """
        ...
    
    @staticmethod
    def dilate(
        x_radius: float,
        y_radius: float,
    ) -> ImageFilter_: 
        """
        Create an image filter that enhances pixel values to the maximum in a region.
        
        This filter enhances the per-channel pixel values to the maximum value
        in a circle around the pixel.
        
        Args:
            x_radius: The radius in the x direction.
            y_radius: The radius in the y direction.
            
        Returns:
            A new image filter that performs dilation.
        """
        ...
    
    @staticmethod
    def erode(
        x_radius: float,
        y_radius: float,
    ) -> ImageFilter_: 
        """
        Create an image filter that dampens pixel values to the minimum in a region.
        
        This filter dampens the per-channel pixel values to the minimum value
        in a circle around the pixel.
        
        Args:
            x_radius: The radius in the x direction.
            y_radius: The radius in the y direction.
            
        Returns:
            A new image filter that performs erosion.
        """
        ...
    
    @staticmethod
    def matrix(
        matrix: Matrix_,
        sampling: TextureSampling,
    ) -> ImageFilter_: 
        """
        Create an image filter that applies a transformation matrix to the image.
        
        Args:
            matrix: The transformation matrix to apply.
            sampling: The sampling method to use when reading the transformed image.
            
        Returns:
            A new image filter that applies the specified transformation.
        """
        ...

class MaskFilter_:
    """
    A filter applied to a shape's mask before drawing.
    
    Mask filters are functions that are applied over a shape after it has been
    drawn but before it has been blended into the final image.
    """
    @staticmethod
    def blur(
        style: BlurStyle,
        sigma: float,
    ) -> MaskFilter_: 
        """
        Create a mask filter that blurs contents in the masked shape.
        
        Args:
            style: The style of blur to apply.
            sigma: The standard deviation of the blur.
            
        Returns:
            A new mask filter that applies the specified blur.
        """
        ...

class Paint_:
    """
    Controls the visual properties of drawing operations.
    
    Paints define how shapes and text are rendered, including color, stroke style,
    blend mode, and various filters.
    """
    def __init__(self) -> None: 
        """Initialize a paint with default values."""
        ...
    
    def set_color(
        self,
        color: Color_,
    ) -> Paint_: 
        """
        Set the paint color.
        
        Args:
            color: The color to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_blend_mode(
        self,
        blend_mode: BlendMode,
    ) -> Paint_: 
        """
        Set the paint blend mode.
        
        The blend mode controls how the new paint contents are mixed with the values
        already drawn using previous draw calls.
        
        Args:
            blend_mode: The blend mode to use.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_draw_style(
        self,
        style: DrawStyle,
    ) -> Paint_: 
        """
        Set the paint draw style.
        
        The style controls if the closed shapes are filled and/or stroked.
        
        Args:
            style: The draw style to use.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_stroke_cap(
        self,
        cap: StrokeCap,
    ) -> Paint_: 
        """
        Set how strokes rendered using this paint are capped.
        
        Args:
            cap: The stroke cap style to use.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_stroke_join(
        self,
        join: StrokeJoin,
    ) -> Paint_: 
        """
        Set how strokes rendered using this paint are joined.
        
        Args:
            join: The stroke join style to use.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_stroke_width(
        self,
        width: float,
    ) -> Paint_: 
        """
        Set the width of the strokes rendered using this paint.
        
        Args:
            width: The stroke width in pixels.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_stroke_miter(
        self,
        miter: float,
    ) -> Paint_: 
        """
        Set the miter limit of the strokes rendered using this paint.
        
        The miter limit controls when a sharp corner is beveled.
        
        Args:
            miter: The miter limit value.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_color_filter(
        self,
        filter: ColorFilter_,
    ) -> Paint_: 
        """
        Set the color filter of the paint.
        
        Color filters are functions that take two colors and mix them to produce
        a single color. This color is then usually merged with the destination
        during blending.
        
        Args:
            filter: The color filter to use.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_color_source(
        self,
        source: ColorSource_,
    ) -> Paint_: 
        """
        Set the color source of the paint.
        
        Color sources are functions that generate colors for each texture element
        covered by a draw call.
        
        Args:
            source: The color source to use.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_image_filter(
        self,
        filter: ImageFilter_,
    ) -> Paint_: 
        """
        Set the image filter of the paint.
        
        Image filters are functions that are applied to regions of a texture to
        produce a single color.
        
        Args:
            filter: The image filter to use.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_mask_filter(
        self,
        filter: MaskFilter_,
    ) -> Paint_: 
        """
        Set the mask filter of the paint.
        
        Mask filters are functions that are applied over a shape after it has been
        drawn but before it has been blended into the final image.
        
        Args:
            filter: The mask filter to use.
            
        Returns:
            Self for method chaining.
        """
        ...

class DisplayList_:
    """
    Represents encoded rendering intent.
    
    Display lists are immutable, reusable, thread-safe, and context-agnostic.
    They encapsulate a series of drawing commands that can be executed on a surface.
    
    While it is perfectly fine to create new display lists per frame, there may
    be opportunities for optimization when display lists are reused multiple times.
    """
    pass

class Path_:
    """
    Represents a two-dimensional path that is immutable and graphics context agnostic.
    
    Paths in Impeller consist of linear, cubic Bézier curve, and quadratic
    Bézier curve segments. All other shapes are approximations using these
    building blocks.
    
    Paths are created using path builders that allow for the configuration of the
    path segments, how they are filled, and/or stroked.
    """
    pass

class LineMetrics_:
    """
    Describes the metrics of lines in a fully laid out paragraph.
    
    Regardless of how the string of text is specified to the paragraph builder,
    offsets into buffers that are returned by line metrics are always assumed to
    be into buffers of UTF-16 code units.
    """
    def unscaled_ascent(
        self,
        line: int,
    ) -> float: 
        """
        Get the rise from the baseline as calculated from the font and style for this line.
        
        This ignores the height from the text style.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The unscaled ascent value.
        """
        ...
    
    def ascent(
        self,
        line: int,
    ) -> float: 
        """
        Get the rise from the baseline as calculated from the font and style for this line.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The ascent value.
        """
        ...
    
    def descent(
        self,
        line: int,
    ) -> float: 
        """
        Get the drop from the baseline as calculated from the font and style for this line.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The descent value.
        """
        ...
    
    def baseline(
        self,
        line: int,
    ) -> float: 
        """
        Get the y coordinate of the baseline for this line from the top of the paragraph.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The baseline position.
        """
        ...
    
    def is_hardbreak(
        self,
        line: int,
    ) -> bool: 
        """
        Check if this line ends with an explicit line break or is the end of the paragraph.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            True if the line is a hard break, False otherwise.
        """
        ...
    
    def width(
        self,
        line: int,
    ) -> float: 
        """
        Get the width of the line from the left edge of the leftmost glyph to the right edge.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The width of the line.
        """
        ...
    
    def height(
        self,
        line: int,
    ) -> float: 
        """
        Get the total height of the line from the top edge to the bottom edge.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The height of the line.
        """
        ...
    
    def left(
        self,
        line: int,
    ) -> float: 
        """
        Get the x coordinate of left edge of the line.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The left edge coordinate.
        """
        ...
    
    def code_unit_start_index(
        self,
        line: int,
    ) -> int: 
        """
        Get the start index in the buffer of UTF-16 code units for this line.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The UTF-16 code units start index.
        """
        ...
    
    def code_unit_end_index(
        self,
        line: int,
    ) -> int: 
        """
        Get the end index in the buffer of UTF-16 code units for this line.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The UTF-16 code units end index.
        """
        ...
    
    def code_unit_end_index_excluding_whitespace(
        self,
        line: int,
    ) -> int: 
        """
        Get the end index (excluding whitespace) in the buffer of UTF-16 code units.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The UTF-16 code units end index excluding whitespace.
        """
        ...
    
    def code_unit_end_index_including_newline(
        self,
        line: int,
    ) -> int: 
        """
        Get the end index (including newlines) in the buffer of UTF-16 code units.
        
        Args:
            line: The line index (zero based).
            
        Returns:
            The UTF-16 code units end index including newlines.
        """
        ...

class GlyphInfo_:
    """
    Describes the metrics of glyphs in a paragraph line.
    
    Provides information about a specific glyph in a paragraph, including its
    position, bounds, and text properties.
    """
    def grapheme_cluster_code_unit_range_begin(self) -> int: 
        """
        Get the start index in the buffer of UTF-16 code units for the grapheme cluster.
        
        Returns:
            The UTF-16 code units start index.
        """
        ...
    
    def grapheme_cluster_code_unit_range_end(self) -> int: 
        """
        Get the end index in the buffer of UTF-16 code units for the grapheme cluster.
        
        Returns:
            The UTF-16 code units end index.
        """
        ...
    
    def grapheme_cluster_bounds(self) -> Rect_: 
        """
        Get the bounds of the grapheme cluster in the coordinate space of the paragraph.
        
        Returns:
            The grapheme cluster bounds.
        """
        ...
    
    def is_ellipsis(self) -> bool: 
        """
        Check if the glyph represents an ellipsis.
        
        Returns:
            True if the glyph is an ellipsis, False otherwise.
        """
        ...
    
    def text_direction(self) -> TextDirection: 
        """
        Get the direction of the run that contains the glyph.
        
        Returns:
            The text direction.
        """
        ...

class Paragraph_:
    """
    An immutable, fully laid out paragraph of text.
    
    Paragraphs are created by paragraph builders and contain the complete layout
    information for a block of text, including line breaks, font metrics, and
    glyph positioning.
    """
    def alphabetic_baseline(self) -> float: 
        """
        Get the distance from the top of the paragraph to the alphabetic baseline of the first line.
        
        This is used for alphabetic fonts (A-Z, a-z, Greek, etc.).
        
        Returns:
            The alphabetic baseline distance.
        """
        ...
    
    def height(self) -> float: 
        """
        Get the height of the laid out paragraph.
        
        This is not a tight bounding box and some glyphs may not reach the minimum
        location they are allowed to reach.
        
        Returns:
            The height of the paragraph.
        """
        ...
    
    def ideographic_baseline(self) -> float: 
        """
        Get the distance from the top of the paragraph to the ideographic baseline of the first line.
        
        This is used for ideographic fonts (Japanese, Korean, etc.).
        
        Returns:
            The ideographic baseline distance.
        """
        ...
    
    def line_count(self) -> int: 
        """
        Get the number of lines visible in the paragraph after line breaking.
        
        Returns:
            The number of lines.
        """
        ...
    
    def longest_line_width(self) -> float: 
        """
        Get the length of the longest line in the paragraph.
        
        This is the horizontal distance between the left edge of the leftmost glyph
        and the right edge of the rightmost glyph, in the longest line in the paragraph.
        
        Returns:
            The width of the longest line.
        """
        ...
    
    def max_intrinsic_width(self) -> float: 
        """
        Get the width of the paragraph without line breaking.
        
        Returns:
            The maximum intrinsic width.
        """
        ...
    
    def max_width(self) -> float: 
        """
        Get the width provided to the paragraph builder during layout.
        
        This is the maximum width any line in the laid out paragraph can occupy.
        But, it is not necessarily the actual width of the paragraph after layout.
        
        Returns:
            The maximum width.
        """
        ...
    
    def min_intrinsic_width(self) -> float: 
        """
        Get the actual width of the longest line in the paragraph after layout.
        
        This is expected to be less than or equal to max_width().
        
        Returns:
            The minimum intrinsic width.
        """
        ...
    
    def line_metrics(self) -> LineMetrics_: 
        """
        Get the line metrics of this laid out paragraph.
        
        Calculating the line metrics is expensive. The first time line metrics are
        requested, they will be cached along with the paragraph (which is immutable).
        
        Returns:
            The line metrics.
        """
        ...
    
    def glyph_info_at_code_unit_index(
        self,
        code_unit_index: int,
    ) -> GlyphInfo_: 
        """
        Get information about the glyph at the given UTF-16 code unit index.
        
        Args:
            code_unit_index: The UTF-16 code unit index.
            
        Returns:
            The glyph information.
        """
        ...
    
    def glyph_info_at_paragraph_coordinate(
        self,
        x: float,
        y: float,
    ) -> GlyphInfo_: 
        """
        Get information about the glyph closest to the specified coordinates.
        
        Args:
            x: The x coordinate relative to paragraph origin.
            y: The y coordinate relative to paragraph origin.
            
        Returns:
            The glyph information.
        """
        ...
    
    def word_boundary(
        self,
        code_unit_index: int,
    ) -> Range_: 
        """
        Get the range into the UTF-16 code unit buffer that represents the word.
        
        Word boundaries are defined more precisely in Unicode Standard Annex #29.
        
        Args:
            code_unit_index: The code unit index.
            
        Returns:
            The range representing the word boundary.
        """
        ...

class TypographyContext_:
    """
    A context for text layout and rendering.
    
    Typography contexts allow for the layout and rendering of text. These are
    typically expensive to create and applications will only ever need to create
    a single one during their lifetimes.
    
    Unlike graphics contexts, typography contexts are not thread-safe. These must
    be created, used, and collected on a single thread.
    """
    def __init__(self) -> None: 
        """Initialize a new typography context."""
        ...

class ParagraphStyle_:
    """
    Specifies the style properties for text in a paragraph.
    
    Paragraph styles are managed in a stack with specify text properties to apply
    to text that is added to the paragraph builder.
    """
    def __init__(self) -> None: 
        """Initialize a new paragraph style with default values."""
        ...
    
    def set_background(
        self,
        paint: Paint_,
    ) -> ParagraphStyle_: 
        """
        Set the paint used to render the background of the text glyphs.
        
        Args:
            paint: The paint to use for the background.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_font_family(
        self,
        family: str,
    ) -> ParagraphStyle_: 
        """
        Set the font family.
        
        Args:
            family: The font family name.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_font_size(
        self,
        size: float,
    ) -> ParagraphStyle_: 
        """
        Set the font size.
        
        Args:
            size: The font size in logical pixels.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_font_style(
        self,
        style: FontStyle,
    ) -> ParagraphStyle_: 
        """
        Set whether the glyphs should be bolded or italicized.
        
        Args:
            style: The font style.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_font_weight(
        self,
        weight: FontWeight,
    ) -> ParagraphStyle_: 
        """
        Set the weight of the font to select when rendering glyphs.
        
        Args:
            weight: The font weight.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_font_foreground(
        self,
        paint: Paint_,
    ) -> ParagraphStyle_: 
        """
        Set the paint used to render the text glyph contents.
        
        Args:
            paint: The paint to use for the text.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_height(
        self,
        height: float,
    ) -> ParagraphStyle_: 
        """
        Set the height of the text as a multiple of text size.
        
        When height is 0.0, the line height will be determined by the font's metrics
        directly, which may differ from the font size. Otherwise the line height of
        the text will be a multiple of font size, and be exactly fontSize * height
        logical pixels tall.
        
        Args:
            height: The height multiplier.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_locale(
        self,
        locale: str,
    ) -> ParagraphStyle_: 
        """
        Set the paragraph locale.
        
        Args:
            locale: The locale string (e.g., "en_US").
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_max_lines(
        self,
        count: int,
    ) -> ParagraphStyle_: 
        """
        Set the maximum line count within the paragraph.
        
        Args:
            count: The maximum number of lines.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_text_alignment(
        self,
        align: TextAlignment,
    ) -> ParagraphStyle_: 
        """
        Set the alignment of text within the paragraph.
        
        Args:
            align: The text alignment.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def set_text_direction(
        self,
        direction: TextDirection,
    ) -> ParagraphStyle_: 
        """
        Set the directionality of the text within the paragraph.
        
        Args:
            direction: The text direction.
            
        Returns:
            Self for method chaining.
        """
        ...

class ParagraphBuilder_:
    """
    Allows for the creation of fully laid out paragraphs.
    
    To build a paragraph, users push/pop paragraph styles onto a stack then add
    UTF-8 encoded text. The properties on the top of paragraph style stack when
    the text is added are used to layout and shape that subset of the paragraph.
    """
    def __init__(
        self,
        type_context: TypographyContext_,
    ): 
        """
        Initialize a new paragraph builder.
        
        Args:
            type_context: The typography context to use.
        """
        ...
    
    def build(
        self,
        width: float,
    ) -> Paragraph_: 
        """
        Layout and build a new paragraph using the specified width.
        
        The resulting paragraph is immutable. The paragraph builder must be
        discarded and a new one created to build more paragraphs.
        
        Args:
            width: The paragraph width in logical pixels.
            
        Returns:
            A new paragraph.
        """
        ...
    
    def push_style(
        self,
        style: ParagraphStyle_,
    ) -> ParagraphBuilder_: 
        """
        Push a new paragraph style onto the paragraph style stack.
        
        Not all paragraph styles can be combined. For instance, it does not make
        sense to mix text alignment for different text runs within a paragraph.
        In such cases, the preference of the first paragraph style on the style
        stack will take hold.
        
        Args:
            style: The paragraph style to push.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def pop_style(self) -> ParagraphBuilder_: 
        """
        Pop a previously pushed paragraph style from the paragraph style stack.
        
        Returns:
            Self for method chaining.
        """
        ...
    
    def add_text(
        self,
        text: str,
    ) -> ParagraphBuilder_: 
        """
        Add UTF-8 encoded text to the paragraph.
        
        The text will be styled according to the paragraph style already on top
        of the paragraph style stack.
        
        Args:
            text: The text to add.
            
        Returns:
            Self for method chaining.
        """
        ...

class Texture_:
    """
    A reference to a texture whose data is resident on the GPU.
    
    Textures can be referenced in draw calls and paints. Creating textures is
    extremely expensive and should be done on background threads when possible.
    """
    @staticmethod
    def with_contents(
        context: Context_,
        desc: TextureDescriptor_,
        data: bytes,
    ) -> Texture_: 
        """
        Create a texture with decompressed bytes.
        
        Note: Do not supply compressed image data directly (PNG, JPEG, etc.).
        This function only works with tightly packed decompressed data.
        
        Args:
            context: The graphics context.
            desc: The texture descriptor.
            data: The raw pixel data.
            
        Returns:
            A new texture.
        """
        ...

class DisplayListBuilder_:
    """
    Allows for the incremental creation of display lists.
    
    Display list builders are context-agnostic and can be used to create
    display lists that can be drawn on any surface.
    """
    def __init__(self) -> None: 
        """Initialize a new display list builder."""
        ...
    
    def build(self) -> DisplayList_: 
        """
        Create a new display list using the rendering intent already encoded in the builder.
        
        The builder is reset after this call.
        
        Returns:
            A new display list.
        """
        ...
    
    def clip_oval(
        self,
        rect: Rect_,
        op: ClipOperation,
    ) -> DisplayListBuilder_: 
        """
        Reduce the clip region to the intersection with the given oval.
        
        Args:
            rect: The rectangle defining the oval bounds.
            op: The clip operation to perform.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def clip_path(
        self,
        path: Path_,
        op: ClipOperation,
    ) -> DisplayListBuilder_: 
        """
        Reduce the clip region to the intersection with the given path.
        
        Args:
            path: The path to clip with.
            op: The clip operation to perform.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def clip_rect(
        self,
        rect: Rect_,
        op: ClipOperation,
    ) -> DisplayListBuilder_: 
        """
        Reduce the clip region to the intersection with the given rectangle.
        
        Args:
            rect: The rectangle to clip with.
            op: The clip operation to perform.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def clip_rounded_rect(
        self,
        rect: Rect_,
        radii: RoundingRadii_,
        op: ClipOperation,
    ) -> DisplayListBuilder_: 
        """
        Reduce the clip region to the intersection with the given rounded rectangle.
        
        Args:
            rect: The rectangle to clip with.
            radii: The corner radii of the rectangle.
            op: The clip operation to perform.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_dashed_line(
        self,
        from_point: Point_,
        to_point: Point_,
        on_length: float,
        off_length: float,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw a dashed line segment.
        
        Args:
            from_point: The starting point of the line.
            to_point: The ending point of the line.
            on_length: The length of the dash.
            off_length: The length of the gap between dashes.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_display_list(
        self,
        dl: DisplayList_,
        opacity: float,
    ) -> DisplayListBuilder_: 
        """
        Flatten the contents of another display list into this one.
        
        Args:
            dl: The display list to draw.
            opacity: The opacity to apply (0.0 to 1.0).
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_line(
        self,
        from_point: Point_,
        to_point: Point_,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw a line segment.
        
        Args:
            from_point: The starting point of the line.
            to_point: The ending point of the line.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_oval(
        self,
        oval_bounds: Rect_,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw an oval.
        
        Args:
            oval_bounds: The rectangle defining the oval bounds.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_paint(
        self,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Fill the current clip with the specified paint.
        
        Args:
            paint: The paint to use for filling.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_paragraph(
        self,
        paragraph: Paragraph_,
        point: Point_,
    ) -> DisplayListBuilder_: 
        """
        Draw a paragraph at the specified point.
        
        Args:
            paragraph: The paragraph to draw.
            point: The position to draw the paragraph at.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_shadow(
        self,
        path: Path_,
        shadow_color: Color_,
        elevation: float,
        occuluder_is_transparent: bool,
        device_pixel_ratio: float,
    ) -> DisplayListBuilder_: 
        """
        Draw a shadow for a path given a material elevation.
        
        Args:
            path: The shadow path.
            shadow_color: The shadow color.
            elevation: The material elevation.
            occuluder_is_transparent: If the object casting the shadow is transparent.
            device_pixel_ratio: The device pixel ratio.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_path(
        self,
        path: Path_,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw the specified shape.
        
        Args:
            path: The path to draw.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_rect(
        self,
        rect: Rect_,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw a rectangle.
        
        Args:
            rect: The rectangle to draw.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_rounded_rect(
        self,
        rect: Rect_,
        radii: RoundingRadii_,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw a rounded rectangle.
        
        Args:
            rect: The rectangle to draw.
            radii: The corner radii of the rectangle.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_rounded_rect_difference(
        self,
        outer_rect: Rect_,
        outer_radii: RoundingRadii_,
        inner_rect: Rect_,
        inner_radii: RoundingRadii_,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw a shape that is the difference between two rounded rectangles.
        
        Args:
            outer_rect: The outer rectangle.
            outer_radii: The corner radii of the outer rectangle.
            inner_rect: The inner rectangle.
            inner_radii: The corner radii of the inner rectangle.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_texture(
        self,
        texture: Texture_,
        point: Point_,
        sampling: TextureSampling,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw a texture at the specified point.
        
        Args:
            texture: The texture to draw.
            point: The position to draw the texture at.
            sampling: The sampling method to use.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def draw_texture_rect(
        self,
        texture: Texture_,
        src_rect: Rect_,
        dst_rect: Rect_,
        sampling: TextureSampling,
        paint: Paint_,
    ) -> DisplayListBuilder_: 
        """
        Draw a portion of texture at the specified location.
        
        Args:
            texture: The texture to draw.
            src_rect: The source rectangle within the texture.
            dst_rect: The destination rectangle to draw to.
            sampling: The sampling method to use.
            paint: The paint to use for drawing.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def save_count(self) -> int: 
        """
        Get the current size of the save stack.
        
        Returns:
            The save stack size.
        """
        ...
    
    def reset_transform(self) -> DisplayListBuilder_: 
        """
        Reset the transformation on top of the transformation stack to identity.
        
        Returns:
            Self for method chaining.
        """
        ...
    
    def restore(self) -> DisplayListBuilder_: 
        """
        Pop the last entry pushed onto the save stack.
        
        Returns:
            Self for method chaining.
        """
        ...
    
    def restore_to_count(
        self,
        count: int,
    ) -> DisplayListBuilder_: 
        """
        Restore the save stack to the specified count.
        
        Effectively calls restore() until the size of the save stack becomes the specified count.
        
        Args:
            count: The target save stack count.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def rotate(
        self,
        angle_in_degrees: float,
    ) -> DisplayListBuilder_: 
        """
        Apply a clockwise rotation to the transformation matrix.
        
        Args:
            angle_in_degrees: The angle in degrees.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def save(self) -> DisplayListBuilder_: 
        """
        Stash the current transformation and clip state onto a save stack.
        
        Returns:
            Self for method chaining.
        """
        ...
    
    def save_layer(
        self,
        bounds: Rect_,
        paint: Optional[Paint_] = None,
        backdrop: Optional[ImageFilter_] = None,
    ) -> DisplayListBuilder_: 
        """
        Save the current state and create an offscreen layer for rendering.
        
        On the balancing call to restore, the supplied paint's filters and blend modes
        will be used to composite the offscreen contents back onto the display list.
        
        Args:
            bounds: The bounds of the layer.
            paint: Optional paint to use when compositing the layer.
            backdrop: Optional backdrop filter to apply.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def scale(
        self,
        x: float,
        y: float,
    ) -> DisplayListBuilder_: 
        """
        Apply a scale to the transformation matrix.
        
        Args:
            x: The x scale factor.
            y: The y scale factor.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def get_transform(self) -> Matrix_: 
        """
        Get the transformation currently built up on the top of the transformation stack.
        
        Returns:
            The current transformation matrix.
        """
        ...
    
    def set_transform(
        self,
        xform: Matrix_,
    ) -> DisplayListBuilder_: 
        """
        Clear the transformation on top of the save stack and replace it with a new value.
        
        Args:
            xform: The new transformation matrix.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def push_transform(
        self,
        xform: Matrix_,
    ) -> DisplayListBuilder_: 
        """
        Append the provided transformation to the transformation already on the save stack.
        
        Args:
            xform: The transformation matrix to append.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def translate(
        self,
        x: float,
        y: float,
    ) -> DisplayListBuilder_: 
        """
        Apply a translation to the transformation matrix.
        
        Args:
            x: The x translation.
            y: The y translation.
            
        Returns:
            Self for method chaining.
        """
        ...

class PathBuilder_:
    """
    Allows for the incremental building of paths.
    
    Path builders create immutable Path objects that can be used for drawing
    and clipping operations.
    """
    def __init__(self) -> None: 
        """Initialize a new path builder."""
        ...
    
    def build_copy(
        self,
        fill: FillType,
    ) -> Path_: 
        """
        Create a new path by copying the existing built-up path.
        
        The existing path can continue being added to.
        
        Args:
            fill: The fill type to use for the path.
            
        Returns:
            A new path.
        """
        ...
    
    def build(
        self,
        fill: FillType,
    ) -> Path_: 
        """
        Create a new path using the existing built-up path.
        
        The existing path builder now contains an empty path.
        
        Args:
            fill: The fill type to use for the path.
            
        Returns:
            A new path.
        """
        ...
    
    def add_arc(
        self,
        rect: Rect_,
        start_degrees: float,
        end_degrees: float,
    ) -> PathBuilder_: 
        """
        Add an arc to the path.
        
        Args:
            rect: The rectangle defining the oval bounds of the arc.
            start_degrees: The starting angle in degrees.
            end_degrees: The ending angle in degrees.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def add_oval(
        self,
        oval_bounds: Rect_,
    ) -> PathBuilder_: 
        """
        Add an oval to the path.
        
        Args:
            oval_bounds: The rectangle defining the oval bounds.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def add_rect(
        self,
        rect: Rect_,
    ) -> PathBuilder_: 
        """
        Add a rectangle to the path.
        
        Args:
            rect: The rectangle to add.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def add_rounded_rect(
        self,
        rect: Rect_,
        radii: RoundingRadii_,
    ) -> PathBuilder_: 
        """
        Add a rounded rectangle to the path.
        
        Args:
            rect: The rectangle to add.
            radii: The corner radii of the rectangle.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def close(self) -> PathBuilder_: 
        """
        Close the current subpath.
        
        This adds a line segment from the current point to the first point of the subpath.
        
        Returns:
            Self for method chaining.
        """
        ...
    
    def cubic_curve_to(
        self,
        cp1: Point_,
        cp2: Point_,
        end: Point_,
    ) -> PathBuilder_: 
        """
        Add a cubic Bézier curve from the current point to the specified end point.
        
        Args:
            cp1: The first control point.
            cp2: The second control point.
            end: The end point.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def line_to(
        self,
        location: Point_,
    ) -> PathBuilder_: 
        """
        Add a line segment from the current point to the specified location.
        
        Args:
            location: The end point of the line.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def move_to(
        self,
        location: Point_,
    ) -> PathBuilder_: 
        """
        Move the cursor to the specified location without adding a line segment.
        
        Args:
            location: The new cursor location.
            
        Returns:
            Self for method chaining.
        """
        ...
    
    def quadratic_curve_to(
        self,
        cp: Point_,
        end: Point_,
    ) -> PathBuilder_: 
        """
        Add a quadratic Bézier curve from the current point to the specified end point.
        
        Args:
            cp: The control point.
            end: The end point.
            
        Returns:
            Self for method chaining.
        """
        ...

class Surface_:
    """
    A render target for Impeller to direct rendering to.
    
    Surfaces are how Impeller API users perform Window System Integration (WSI).
    Users wrap swapchain images as surfaces and draw display lists onto these
    surfaces to present content.
    """
    def draw(
        self,
        dl: DisplayList_,
    ) -> bool: 
        """
        Draw a display list onto the surface.
        
        The same display list can be drawn multiple times to different surfaces.
        
        Args:
            dl: The display list to draw.
            
        Returns:
            True if the display list was successfully drawn, False otherwise.
        """
        ...
    
    def present(self) -> bool: 
        """
        Present the surface to the underlying window system.
        
        Returns:
            True if the surface was successfully presented, False otherwise.
        """
        ...

class Context_:
    """
    An Impeller graphics context.
    
    Contexts are thread-safe objects that are expensive to create. Most
    applications will only ever create a single context during their lifetimes.
    Once setup, Impeller is ready to render frames as performantly as possible.
    
    During setup, contexts create the underlying graphics pipelines, allocators,
    worker threads, etc.
    
    The general guidance is to create as few contexts as possible (typically
    just one) and share them as much as possible.
    """
    def __init__(self) -> None: 
        """
        Initialize a new Metal context using the system default Metal device.
        """
        ...

class Window_:
    """
    A window for rendering content.
    
    Provides a platform-specific window and handles for creating render surfaces.
    """
    def __init__(self) -> None: 
        """Initialize a new window with default size (800x600)."""
        ...
    
    def create_render_surface(
        self,
        context: Context_,
    ) -> Surface_: 
        """
        Create a render surface for the window.
        
        Args:
            context: The graphics context to use.
            
        Returns:
            A new surface for rendering to the window.
        """
        ...
    
    def should_close(self) -> bool: 
        """
        Check if the window should close.
        
        Returns:
            True if the window should close, False otherwise.
        """
        ...
    
    def poll_events(self) -> None: 
        """Process all pending window events."""
        ...
