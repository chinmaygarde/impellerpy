from impellerpy import *

def test_paint_creation():
    """Test Paint_ creation and basic properties."""
    # Create a paint
    paint = Paint_()

    # We can't directly test the default properties, but we can verify it was created
    assert paint is not None


def test_paint_set_color():
    """Test Paint_ set_color method."""
    # Create a paint
    paint = Paint_()

    # Create a color
    color = Color(r=0.5, g=0.6, b=0.7, a=0.8)

    # Set the color on the paint
    result = paint.set_color(color)

    # Verify method chaining works
    assert result is paint


def test_paint_set_blend_mode():
    """Test Paint_ set_blend_mode method."""
    # Create a paint
    paint = Paint_()

    # Set different blend modes
    blend_modes = [
        BlendMode.SOURCE_OVER,
        BlendMode.MULTIPLY,
        BlendMode.SCREEN,
        BlendMode.OVERLAY,
        BlendMode.DARKEN,
        BlendMode.LIGHTEN,
    ]

    for mode in blend_modes:
        result = paint.set_blend_mode(mode)
        # Verify method chaining works
        assert result is paint


def test_paint_set_draw_style():
    """Test Paint_ set_draw_style method."""
    # Create a paint
    paint = Paint_()

    # Set different draw styles
    draw_styles = [DrawStyle.FILL, DrawStyle.STROKE, DrawStyle.STROKE_AND_FILL]

    for style in draw_styles:
        result = paint.set_draw_style(style)
        # Verify method chaining works
        assert result is paint


def test_paint_set_stroke_properties():
    """Test Paint_ stroke-related methods."""
    # Create a paint
    paint = Paint_()

    # Test set_stroke_cap
    caps = [StrokeCap.BUTT, StrokeCap.ROUND, StrokeCap.SQUARE]
    for cap in caps:
        result = paint.set_stroke_cap(cap)
        assert result is paint

    # Test set_stroke_join
    joins = [StrokeJoin.MITER, StrokeJoin.ROUND, StrokeJoin.BEVEL]
    for join in joins:
        result = paint.set_stroke_join(join)
        assert result is paint

    # Test set_stroke_width
    result = paint.set_stroke_width(5.0)
    assert result is paint

    # Test set_stroke_miter
    result = paint.set_stroke_miter(4.0)
    assert result is paint


def test_paint_set_filters():
    """Test Paint_ filter-related methods."""
    # Create a paint
    paint = Paint_()

    # Test set_color_filter
    color = Color(r=0.5, g=0.6, b=0.7, a=0.8)
    color_filter = ColorFilter_.blend(color, BlendMode.SOURCE_OVER)
    result = paint.set_color_filter(color_filter)
    assert result is paint

    # Test set_image_filter
    image_filter = ImageFilter_.blur(5.0, 5.0, TileMode.CLAMP)
    result = paint.set_image_filter(image_filter)
    assert result is paint

    # Test set_mask_filter
    mask_filter = MaskFilter_.blur(BlurStyle.NORMAL, 5.0)
    result = paint.set_mask_filter(mask_filter)
    assert result is paint


def test_paint_set_color_source():
    """Test Paint_ set_color_source method."""
    # Create a paint
    paint = Paint_()

    # Create a linear gradient color source
    start_point = Point(0, 0)
    end_point = Point(100, 100)
    stops = [0.0, 1.0]
    colors = [
        Color(r=1.0, g=0.0, b=0.0, a=1.0),  # Red
        Color(r=0.0, g=0.0, b=1.0, a=1.0),  # Blue
    ]
    tile_mode = TileMode.CLAMP

    color_source = ColorSource_.linear_gradient(
        start_point, end_point, colors, stops, tile_mode
    )

    # Set the color source on the paint
    result = paint.set_color_source(color_source)

    # Verify method chaining works
    assert result is paint
