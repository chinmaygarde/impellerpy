from impellerpy import *


def test_context_creation():
    """Test Context_ creation."""
    # Create a context
    context = Context()

    # We can't directly test the properties of the context, but we can verify it was created
    assert context is not None


def test_context_with_texture():
    """Test Context_ with texture creation."""
    # Create a context
    context = Context()

    # Create a texture descriptor
    desc = TextureDescriptor(PixelFormat.RGBA8888, ISize(100, 100))

    # Create texture data (RGBA, 100x100)
    data = bytes([255, 0, 0, 255] * (100 * 100))  # Red pixels

    # Create a texture
    texture = Texture.with_contents(context, desc, data)

    # We can't directly test the properties of the texture, but we can verify it was created
    assert texture is not None
