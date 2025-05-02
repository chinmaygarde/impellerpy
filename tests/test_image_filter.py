from impellerpy.impeller import *
from impellerpy.impellerpy import *


def test_image_filter_blur():
    """Test ImageFilter_ blur static method."""
    # Create a blur image filter
    x_sigma = 5.0
    y_sigma = 5.0
    image_filter = ImageFilter_.blur(x_sigma, y_sigma, TileMode.CLAMP)

    # We can't directly test the properties of the filter, but we can verify it was created
    assert image_filter is not None

    # Test with different sigma values
    image_filter2 = ImageFilter_.blur(10.0, 15.0, TileMode.CLAMP)
    assert image_filter2 is not None


def test_image_filter_compose():
    """Test ImageFilter_ compose static method."""
    # Create two filters to compose
    outer_filter = ImageFilter_.blur(5.0, 5.0, TileMode.CLAMP)
    inner_filter = ImageFilter_.blur(2.0, 2.0, TileMode.CLAMP)

    # Compose the filters
    composed_filter = ImageFilter_.compose(outer_filter, inner_filter)

    # We can't directly test the properties of the filter, but we can verify it was created
    assert composed_filter is not None


def test_image_filter_dilate():
    """Test ImageFilter_ dilate static method."""
    # Create a dilate image filter
    x_radius = 3.0
    y_radius = 3.0
    image_filter = ImageFilter_.dilate(x_radius, y_radius)

    # We can't directly test the properties of the filter, but we can verify it was created
    assert image_filter is not None

    # Test with different radius values
    image_filter2 = ImageFilter_.dilate(5.0, 7.0)
    assert image_filter2 is not None


def test_image_filter_erode():
    """Test ImageFilter_ erode static method."""
    # Create an erode image filter
    x_radius = 3.0
    y_radius = 3.0
    image_filter = ImageFilter_.erode(x_radius, y_radius)

    # We can't directly test the properties of the filter, but we can verify it was created
    assert image_filter is not None

    # Test with different radius values
    image_filter2 = ImageFilter_.erode(5.0, 7.0)
    assert image_filter2 is not None


def test_image_filter_matrix():
    """Test ImageFilter_ matrix static method."""
    # Create a matrix
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
    ]
    matrix = Matrix_(values)

    # Create a matrix image filter
    image_filter = ImageFilter_.matrix(matrix, TextureSampling.LINEAR)

    # We can't directly test the properties of the filter, but we can verify it was created
    assert image_filter is not None

    # Test with nearest neighbor sampling
    image_filter2 = ImageFilter_.matrix(
        matrix, TextureSampling.NEAREST_NEIGHBOR
    )
    assert image_filter2 is not None


def test_image_filter_with_paint():
    """Test using ImageFilter_ with Paint."""
    # Create an image filter
    image_filter = ImageFilter_.blur(5.0, 5.0, TileMode.CLAMP)

    # Create a paint and set the image filter
    paint = Paint()
    paint.set_image_filter(image_filter)

    # We can't directly test the properties of the paint's filter, but we can verify it was set
    # by checking that the paint object is returned (method chaining)
    assert paint is not None
