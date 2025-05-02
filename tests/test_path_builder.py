from impellerpy.impeller import *
from impellerpy.impellerpy import *
import math


def test_path_builder_creation():
    """Test PathBuilder_ creation."""
    # Create a path builder
    path_builder = PathBuilder_()

    # We can't directly test the default properties, but we can verify it was created
    assert path_builder is not None


def test_path_builder_build():
    """Test PathBuilder_ build method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Build a path with non-zero fill type
    path = path_builder.build(FillType.NON_ZERO)

    # We can't directly test the properties of the path, but we can verify it was created
    assert path is not None

    # Create another path builder
    path_builder2 = PathBuilder_()

    # Build a path with odd fill type
    path2 = path_builder2.build(FillType.ODD)
    assert path2 is not None


def test_path_builder_build_copy():
    """Test PathBuilder_ build_copy method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Add some operations
    path_builder.move_to(Point(0, 0))
    path_builder.line_to(Point(100, 100))
    path_builder.line_to(Point(0, 100))
    path_builder.close()

    # Build a copy of the path with non-zero fill type
    path = path_builder.build_copy(FillType.NON_ZERO)

    # We can't directly test the properties of the path, but we can verify it was created
    assert path is not None

    # Verify the original path builder is still usable
    path2 = path_builder.build(FillType.ODD)
    assert path2 is not None


def test_path_builder_add_arc():
    """Test PathBuilder_ add_arc method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Add an arc
    result = path_builder.add_arc(Rect(100, 100, 100, 100), 0.0, 90.0)

    # Verify method chaining works
    assert result is path_builder

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_add_oval():
    """Test PathBuilder_ add_oval method."""
    # Create a path builder
    path_builder = PathBuilder_()

    # Add an oval
    oval_bounds = Rect(50, 50, 100, 100)
    result = path_builder.add_oval(oval_bounds)

    # Verify method chaining works
    assert result is path_builder

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_add_rect():
    """Test PathBuilder_ add_rect method."""
    # Create a path builder
    path_builder = PathBuilder_()

    # Add a rectangle
    rect = Rect(50, 50, 100, 100)
    result = path_builder.add_rect(rect)

    # Verify method chaining works
    assert result is path_builder

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_add_rounded_rect():
    """Test PathBuilder_ add_rounded_rect method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Create a rectangle and rounding radii
    rect = Rect(50, 50, 100, 100)
    radii = RoundingRadii_()
    radii.top_left.x = 10
    radii.top_left.y = 10
    radii.top_right.x = 10
    radii.top_right.y = 10
    radii.bottom_left.x = 10
    radii.bottom_left.y = 10
    radii.bottom_right.x = 10
    radii.bottom_right.y = 10

    # Add a rounded rectangle
    result = path_builder.add_rounded_rect(rect, radii)

    # Verify method chaining works
    assert result is path_builder

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_close():
    """Test PathBuilder_ close method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Add some operations
    path_builder.move_to(Point(0, 0))
    path_builder.line_to(Point(100, 100))
    path_builder.line_to(Point(0, 100))

    # Close the path
    result = path_builder.close()

    # Verify method chaining works
    assert result is path_builder

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_cubic_curve_to():
    """Test PathBuilder_ cubic_curve_to method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Add a move_to operation first
    path_builder.move_to(Point(0, 0))

    # Add a cubic curve
    cp1 = Point(33, 0)
    cp2 = Point(66, 100)
    end = Point(100, 100)
    result = path_builder.cubic_curve_to(cp1, cp2, end)

    # Verify method chaining works
    assert result is path_builder

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_line_to():
    """Test PathBuilder_ line_to method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Add a move_to operation first
    path_builder.move_to(Point(0, 0))

    # Add a line_to operation
    result = path_builder.line_to(Point(100, 100))

    # Verify method chaining works
    assert result is path_builder

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_move_to():
    """Test PathBuilder_ move_to method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Add a move_to operation
    result = path_builder.move_to(Point(50, 50))

    # Verify method chaining works
    assert result is path_builder

    # Add more operations
    path_builder.line_to(Point(150, 50))
    path_builder.line_to(Point(150, 150))
    path_builder.line_to(Point(50, 150))
    path_builder.close()

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_quadratic_curve_to():
    """Test PathBuilder_ quadratic_curve_to method."""
    # Create a path builder
    path_builder = PathBuilder()

    # Add a move_to operation first
    path_builder.move_to(Point(0, 0))

    # Add a quadratic curve
    cp = Point(50, 0)
    end = Point(100, 100)
    result = path_builder.quadratic_curve_to(cp, end)

    # Verify method chaining works
    assert result is path_builder

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None


def test_path_builder_complex_path():
    """Test creating a complex path with PathBuilder_."""
    # Create a path builder
    path_builder = PathBuilder_()

    # Create a star shape
    center_x = 100
    center_y = 100
    outer_radius = 50
    inner_radius = 20
    points = 5

    for i in range(points * 2):
        radius = outer_radius if i % 2 == 0 else inner_radius
        angle = i * 3.14159 / points
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        if i == 0:
            path_builder.move_to(Point(x, y))
        else:
            path_builder.line_to(Point(x, y))

    path_builder.close()

    # Build the path
    path = path_builder.build(FillType.NON_ZERO)
    assert path is not None
