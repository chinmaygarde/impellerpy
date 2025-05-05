from impellerpy import *


def test_display_list_builder_creation():
    """Test DisplayListBuilder_ creation."""
    # Create a display list builder
    dl_builder = DisplayListBuilder()

    # We can't directly test the default properties, but we can verify it was created
    assert dl_builder is not None


def test_display_list_builder_build():
    """Test DisplayListBuilder_ build method."""
    # Create a display list builder
    dl_builder = DisplayListBuilder()

    # Build a display list
    dl = dl_builder.build()

    # We can't directly test the properties of the display list, but we can verify it was created
    assert dl is not None


def test_display_list_builder_clip_methods():
    """Test DisplayListBuilder_ clip methods."""
    # Create a display list builder
    dl_builder = DisplayListBuilder()

    # Test clip_rect
    rect = Rect(50, 50, 100, 100)
    result = dl_builder.clip_rect(rect, ClipOperation.INTERSECT)
    assert result is dl_builder

    # Test clip_oval
    oval_rect = Rect(50, 50, 100, 100)
    result = dl_builder.clip_oval(oval_rect, ClipOperation.DIFFERENCE)
    assert result is dl_builder

    # Test clip_rounded_rect
    rounded_rect = Rect(50, 50, 100, 100)
    radii = RoundingRadii()
    radii.top_left.x = 10
    radii.top_left.y = 10
    radii.top_right.x = 10
    radii.top_right.y = 10
    radii.bottom_left.x = 10
    radii.bottom_left.y = 10
    radii.bottom_right.x = 10
    radii.bottom_right.y = 10
    result = dl_builder.clip_rounded_rect(
        rounded_rect, radii, ClipOperation.INTERSECT
    )
    assert result is dl_builder

    # Test clip_path
    path_builder = PathBuilder()
    path_builder.add_rect(Rect(50, 50, 100, 100))
    path = path_builder.build(FillType.NON_ZERO)
    result = dl_builder.clip_path(path, ClipOperation.INTERSECT)
    assert result is dl_builder

    # Build the display list
    dl = dl_builder.build()
    assert dl is not None


def test_display_list_builder_draw_methods():
    """Test DisplayListBuilder_ draw methods."""
    # Create a display list builder
    dl_builder = DisplayListBuilder()

    # Create a paint
    paint = Paint()
    paint.set_color(Color(r=1.0, g=0.0, b=0.0, a=1.0))

    # Test draw_rect
    rect = Rect(50, 50, 100, 100)
    result = dl_builder.draw_rect(rect, paint)
    assert result is dl_builder

    # Test draw_oval
    oval_rect = Rect(200, 50, 100, 100)
    result = dl_builder.draw_oval(oval_rect, paint)
    assert result is dl_builder

    # Test draw_rounded_rect
    rounded_rect = Rect(350, 50, 100, 100)
    radii = RoundingRadii()
    radii.top_left.x = 10
    radii.top_left.y = 10
    radii.top_right.x = 10
    radii.top_right.y = 10
    radii.bottom_left.x = 10
    radii.bottom_left.y = 10
    radii.bottom_right.x = 10
    radii.bottom_right.y = 10
    result = dl_builder.draw_rounded_rect(rounded_rect, radii, paint)
    assert result is dl_builder

    # Test draw_line
    from_point = Point(50, 200)
    to_point = Point(150, 300)
    result = dl_builder.draw_line(from_point, to_point, paint)
    assert result is dl_builder

    # Test draw_dashed_line
    from_point2 = Point(200, 200)
    to_point2 = Point(300, 300)
    result = dl_builder.draw_dashed_line(
        from_point2, to_point2, 5.0, 5.0, paint
    )
    assert result is dl_builder

    # Test draw_path
    path_builder = PathBuilder()
    path_builder.move_to(Point(350, 200))
    path_builder.line_to(Point(450, 200))
    path_builder.line_to(Point(400, 300))
    path_builder.close()
    path = path_builder.build(FillType.NON_ZERO)
    result = dl_builder.draw_path(path, paint)
    assert result is dl_builder

    # Test draw_paint
    result = dl_builder.draw_paint(paint)
    assert result is dl_builder

    # Build the display list
    dl = dl_builder.build()
    assert dl is not None


def test_display_list_builder_transform_methods():
    """Test DisplayListBuilder_ transform methods."""
    # Create a display list builder
    dl_builder = DisplayListBuilder()

    # Test save and restore
    save_count = dl_builder.save_count()
    result = dl_builder.save()
    assert result is dl_builder
    assert dl_builder.save_count() == save_count + 1

    # Test translate
    result = dl_builder.translate(100.0, 100.0)
    assert result is dl_builder

    # Test scale
    result = dl_builder.scale(2.0, 2.0)
    assert result is dl_builder

    # Test rotate
    result = dl_builder.rotate(45.0)
    assert result is dl_builder

    # Test get_transform
    transform = dl_builder.get_transform()
    assert transform is not None

    # Test set_transform
    identity_matrix = Matrix.identity()
    result = dl_builder.set_transform(identity_matrix)
    assert result is dl_builder

    # Test push_transform
    scale_matrix = Matrix(
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
    result = dl_builder.push_transform(scale_matrix)
    assert result is dl_builder

    # Test restore
    result = dl_builder.restore()
    assert result is dl_builder
    assert dl_builder.save_count() == save_count

    # Test save_layer
    paint = Paint()
    paint.set_color(Color(r=1.0, g=0.0, b=0.0, a=0.5))
    result = dl_builder.save_layer(Rect(10, 10, 100, 100), paint)
    assert result is dl_builder

    # Test restore_to_count
    dl_builder.save()
    dl_builder.save()
    assert dl_builder.save_count() == save_count + 3
    result = dl_builder.restore_to_count(save_count)
    assert result is dl_builder
    assert dl_builder.save_count() == save_count

    # Test reset_transform
    result = dl_builder.reset_transform()
    assert result is dl_builder

    # Build the display list
    dl = dl_builder.build()
    assert dl is not None


def test_display_list_builder_draw_complex():
    """Test DisplayListBuilder_ with complex drawing operations."""
    # Create a display list builder
    dl_builder = DisplayListBuilder()

    # Create paints
    red_paint = Paint()
    red_paint.set_color(Color(r=1.0, g=0.0, b=0.0, a=1.0))

    blue_paint = Paint()
    blue_paint.set_color(Color(r=0.0, g=0.0, b=1.0, a=1.0))
    blue_paint.set_draw_style(DrawStyle.STROKE)
    blue_paint.set_stroke_width(5.0)

    # Draw a complex scene
    dl_builder.save()

    # Draw a red rectangle
    dl_builder.draw_rect(Rect(50, 50, 100, 100), red_paint)

    # Apply transformations
    dl_builder.save()
    dl_builder.translate(200, 50)
    dl_builder.rotate(45.0)

    # Draw a blue stroked rectangle
    dl_builder.draw_rect(Rect(0, 0, 100, 100), blue_paint)

    # Restore transformation
    dl_builder.restore()

    # Draw a path
    path_builder = PathBuilder()
    path_builder.move_to(Point(350, 50))
    path_builder.line_to(Point(450, 50))
    path_builder.line_to(Point(400, 150))
    path_builder.close()
    path = path_builder.build(FillType.NON_ZERO)

    green_paint = Paint()
    green_paint.set_color(Color(r=0.0, g=1.0, b=0.0, a=1.0))

    dl_builder.draw_path(path, green_paint)

    # Restore the original state
    dl_builder.restore()

    # Build the display list
    dl = dl_builder.build()
    assert dl is not None
