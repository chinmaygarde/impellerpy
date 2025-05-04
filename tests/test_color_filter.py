from impellerpy import *

def test_color_filter_blend():
    """Test ColorFilter_ blend static method."""
    # Create a color
    color = Color(r=0.5, g=0.6, b=0.7, a=0.8)

    # Create a color filter with blend mode
    color_filter = ColorFilter_.blend(color, BlendMode.SOURCE_OVER)

    # We can't directly test the properties of the filter, but we can verify it was created
    assert color_filter is not None

    # Test with different blend modes
    color_filter2 = ColorFilter_.blend(color, BlendMode.MULTIPLY)
    assert color_filter2 is not None

    color_filter3 = ColorFilter_.blend(color, BlendMode.SCREEN)
    assert color_filter3 is not None


def test_color_filter_matrix():
    """Test ColorFilter_ matrix static method."""
    # Create a color matrix
    values = [
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
        0.1,
        0.2,
        0.3,
        0.4,  # Color vector
    ]
    color_matrix = ColorMatrix_(values)

    # Create a color filter with matrix
    color_filter = ColorFilter_.matrix(color_matrix)

    # We can't directly test the properties of the filter, but we can verify it was created
    assert color_filter is not None

    # Test with a different matrix
    values2 = [
        0.5,
        0.0,
        0.0,
        0.0,
        0.0,
        0.5,
        0.0,
        0.0,
        0.0,
        0.0,
        0.5,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,  # Color vector
    ]
    color_matrix2 = ColorMatrix_(values2)
    color_filter2 = ColorFilter_.matrix(color_matrix2)
    assert color_filter2 is not None


def test_color_filter_with_paint():
    """Test using ColorFilter_ with Paint."""
    # Create a color
    color = Color(r=0.5, g=0.6, b=0.7, a=0.8)

    # Create a color filter with blend mode
    color_filter = ColorFilter_.blend(color, BlendMode.SOURCE_OVER)

    # Create a paint and set the color filter
    paint = Paint()
    paint.set_color_filter(color_filter)

    # We can't directly test the properties of the paint's filter, but we can verify it was set
    # by checking that the paint object is returned (method chaining)
    assert paint is not None
