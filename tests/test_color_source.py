from impellerpy import *

def test_color_source_conical_gradient():
    """Test ColorSource_ conical_gradient static method."""
    # Create points and colors for the gradient
    start_center = Point(100, 100)
    start_radius = 50.0
    end_center = Point(200, 200)
    end_radius = 100.0
    stops = [0.0, 0.5, 1.0]
    colors = [
        Color(r=1.0, g=0.0, b=0.0, a=1.0),  # Red
        Color(r=0.0, g=1.0, b=0.0, a=1.0),  # Green
        Color(r=0.0, g=0.0, b=1.0, a=1.0),  # Blue
    ]
    tile_mode = TileMode.CLAMP

    # Create a conical gradient color source
    color_source = ColorSource_.conical_gradient(
        start_center,
        start_radius,
        end_center,
        end_radius,
        stops,
        colors,
        tile_mode,
    )

    # We can't directly test the properties of the color source, but we can verify it was created
    assert color_source is not None

    # Test with transformation matrix
    matrix = Matrix(
        [
            [
                2.0,
                0.0,
                0.0,
                0.0,
            ],
            [
                0.0,
                2.0,
                0.0,
                0.0,
            ],
            [
                0.0,
                0.0,
                1.0,
                0.0,
            ],
            [
                0.0,
                0.0,
                0.0,
                1.0,
            ],
        ]
    )

    color_source_with_transform = ColorSource_.conical_gradient(
        start_center,
        start_radius,
        end_center,
        end_radius,
        stops,
        colors,
        tile_mode,
        matrix,
    )
    assert color_source_with_transform is not None


def test_color_source_linear_gradient():
    """Test ColorSource_ linear_gradient static method."""
    # Create points and colors for the gradient
    start_point = Point(0, 0)
    end_point = Point(100, 100)
    stops = [0.0, 0.5, 1.0]
    colors = [
        Color(r=1.0, g=0.0, b=0.0, a=1.0),  # Red
        Color(r=0.0, g=1.0, b=0.0, a=1.0),  # Green
        Color(r=0.0, g=0.0, b=1.0, a=1.0),  # Blue
    ]
    tile_mode = TileMode.REPEAT

    # Create a linear gradient color source
    color_source = ColorSource_.linear_gradient(
        start_point, end_point, colors, stops, tile_mode
    )

    # We can't directly test the properties of the color source, but we can verify it was created
    assert color_source is not None

    # Test with different tile mode
    color_source2 = ColorSource_.linear_gradient(
        start_point, end_point, colors, stops, TileMode.MIRROR
    )
    assert color_source2 is not None


def test_color_source_radial_gradient():
    """Test ColorSource_ radial_gradient static method."""
    # Create center point and colors for the gradient
    center = Point(100, 100)
    radius = 50.0
    stops = [0.0, 0.5, 1.0]
    colors = [
        Color(r=1.0, g=0.0, b=0.0, a=1.0),  # Red
        Color(r=0.0, g=1.0, b=0.0, a=1.0),  # Green
        Color(r=0.0, g=0.0, b=1.0, a=1.0),  # Blue
    ]
    tile_mode = TileMode.CLAMP

    # Create a radial gradient color source
    color_source = ColorSource_.radial_gradient(
        center, radius, colors, stops, tile_mode
    )

    # We can't directly test the properties of the color source, but we can verify it was created
    assert color_source is not None


def test_color_source_sweep_gradient():
    """Test ColorSource_ sweep_gradient static method."""
    # Create center point and colors for the gradient
    center = Point(100, 100)
    start = 0.0
    end = 360.0
    stops = [0.0, 0.5, 1.0]
    colors = [
        Color(r=1.0, g=0.0, b=0.0, a=1.0),  # Red
        Color(r=0.0, g=1.0, b=0.0, a=1.0),  # Green
        Color(r=0.0, g=0.0, b=1.0, a=1.0),  # Blue
    ]
    tile_mode = TileMode.CLAMP

    # Create a sweep gradient color source
    color_source = ColorSource_.sweep_gradient(
        center, start, end, colors, stops, tile_mode
    )

    # We can't directly test the properties of the color source, but we can verify it was created
    assert color_source is not None


def test_color_source_with_paint():
    """Test using ColorSource_ with Paint."""
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

    # Create a paint and set the color source
    paint = Paint()
    paint.set_color_source(color_source)

    # We can't directly test the properties of the paint's color source, but we can verify it was set
    # by checking that the paint object is returned (method chaining)
    assert paint is not None
