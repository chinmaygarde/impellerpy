from impellerpy.impeller import *
from impellerpy.impellerpy import *

def test_surface_methods():
    """Test Surface_ methods."""
    # This test is more of a mock test since we can't create a Surface directly
    # We'll just verify the methods exist and have the right signatures

    # Create a context and window to get a surface
    context = Context_()
    window = Window_()

    # Get a surface from the window
    surface = window.create_render_surface(context)

    # We can't directly test the properties of the surface, but we can verify it was created
    assert surface is not None

    # Create a simple display list to draw
    dl_builder = DisplayListBuilder_()
    paint = Paint_()
    paint.set_color(Color(r=1.0, g=0.0, b=0.0, a=1.0))
    dl_builder.draw_rect(Rect(50, 50, 100, 100), paint)
    dl = dl_builder.build()

    # Test draw method
    draw_result = surface.draw(dl)
    # The result depends on the actual rendering, so we can't assert a specific value
    assert draw_result is True

    # Test present method
    present_result = surface.present()
    # The result depends on the actual rendering, so we can't assert a specific value
    assert present_result is True
