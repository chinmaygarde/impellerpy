from impellerpy import *

def test_texture_with_contents():
    """Test Texture_ with_contents static method."""
    # Create a context
    context = Context_()

    # Create a texture descriptor
    desc = TextureDescriptor_()
    desc.pixel_format = PixelFormat.RGBA8888
    desc.size.width = 100
    desc.size.height = 100
    desc.mip_count = 1

    # Create texture data (RGBA, 100x100)
    data = bytes([255, 0, 0, 255] * (100 * 100))  # Red pixels

    # Create a texture
    texture = Texture_.with_contents(context, desc, data)

    # We can't directly test the properties of the texture, but we can verify it was created
    assert texture is not None


def test_texture_with_display_list_builder():
    """Test using Texture_ with DisplayListBuilder_."""
    # Create a context
    context = Context_()

    # Create a texture descriptor
    desc = TextureDescriptor_()
    desc.pixel_format = PixelFormat.RGBA8888
    desc.size.width = 100
    desc.size.height = 100
    desc.mip_count = 1

    # Create texture data (RGBA, 100x100)
    data = bytes([0, 0, 255, 255] * (100 * 100))  # Blue pixels

    # Create a texture
    texture = Texture_.with_contents(context, desc, data)

    # Create a display list builder
    dl_builder = DisplayListBuilder_()

    # Draw the texture
    point = Point(50, 50)
    paint = Paint_()
    result = dl_builder.draw_texture(
        texture, point, TextureSampling.LINEAR, paint
    )

    # Verify method chaining works
    assert result is dl_builder

    # Draw the texture with rect
    src_rect = Rect(0, 0, 100, 100)
    dst_rect = Rect(200, 50, 100, 100)
    result = dl_builder.draw_texture_rect(
        texture, src_rect, dst_rect, TextureSampling.LINEAR, paint
    )

    # Verify method chaining works
    assert result is dl_builder

    # Build the display list
    dl = dl_builder.build()
    assert dl is not None


def test_texture_with_color_source():
    """Test using Texture_ with ColorSource_."""
    # Create a context
    context = Context_()

    # Create a texture descriptor
    desc = TextureDescriptor_()
    desc.pixel_format = PixelFormat.RGBA8888
    desc.size.width = 100
    desc.size.height = 100
    desc.mip_count = 1

    # Create texture data (RGBA, 100x100)
    data = bytes([0, 255, 0, 255] * (100 * 100))  # Green pixels

    # Create a texture
    texture = Texture_.with_contents(context, desc, data)

    # Create a color source from the texture
    color_source = ColorSource_.image(
        texture, TileMode.REPEAT, TileMode.REPEAT, TextureSampling.LINEAR
    )

    # We can't directly test the properties of the color source, but we can verify it was created
    assert color_source is not None

    # Create a paint and set the color source
    paint = Paint_()
    paint.set_color_source(color_source)

    # Create a display list builder and draw a rect with the paint
    dl_builder = DisplayListBuilder_()
    dl_builder.draw_rect(Rect(0, 0, 300, 300), paint)

    # Build the display list
    dl = dl_builder.build()
    assert dl is not None
