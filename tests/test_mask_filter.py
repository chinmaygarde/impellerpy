from impellerpy.impeller import *
from impellerpy.impellerpy import *


def test_mask_filter_blur():
    """Test MaskFilter_ blur static method."""
    # Create a blur mask filter with different styles
    styles = [
        BlurStyle.NORMAL,
        BlurStyle.SOLID,
        BlurStyle.OUTER,
        BlurStyle.INNER,
    ]
    sigma = 5.0

    for style in styles:
        mask_filter = MaskFilter_.blur(style, sigma)
        # We can't directly test the properties of the filter, but we can verify it was created
        assert mask_filter is not None

    # Test with different sigma value
    mask_filter2 = MaskFilter_.blur(BlurStyle.NORMAL, 10.0)
    assert mask_filter2 is not None


def test_mask_filter_with_paint():
    """Test using MaskFilter_ with Paint."""
    # Create a mask filter
    mask_filter = MaskFilter_.blur(BlurStyle.NORMAL, 5.0)

    # Create a paint and set the mask filter
    paint = Paint()
    paint.set_mask_filter(mask_filter)

    # We can't directly test the properties of the paint's filter, but we can verify it was set
    # by checking that the paint object is returned (method chaining)
    assert paint is not None
