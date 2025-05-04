from impellerpy import *

def test_window_creation():
    """Test Window_ creation."""
    # Create a window
    window = Window_()

    # We can't directly test the properties of the window, but we can verify it was created
    assert window is not None


def test_window_methods():
    """Test Window_ methods."""
    # Create a window
    window = Window_()

    # Test should_close method
    should_close = window.should_close()
    assert isinstance(should_close, bool)

    # Test poll_events method
    window.poll_events()  # Just verify it doesn't crash

    # Test create_render_surface method
    context = Context_()
    surface = window.create_render_surface(context)
    assert surface is not None
