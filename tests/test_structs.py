from impellerpy import *

def test_rect():
    """Test Rect_ class functionality."""
    rect = Rect(10, 20, 30, 40)
    assert rect.x == 10
    assert rect.y == 20
    assert rect.width == 30
    assert rect.height == 40

    # Test default constructor
    rect2 = Rect_()
    assert rect2.x == 0
    assert rect2.y == 0
    assert rect2.width == 0
    assert rect2.height == 0

    # Test property assignment
    rect2.x = 15
    rect2.y = 25
    rect2.width = 35
    rect2.height = 45
    assert rect2.x == 15
    assert rect2.y == 25
    assert rect2.width == 35
    assert rect2.height == 45


def test_point():
    """Test Point_ class functionality."""
    point = Point(10, 20)
    assert point.x == 10
    assert point.y == 20

    # Test default constructor
    point2 = Point_()
    assert point2.x == 0
    assert point2.y == 0

    # Test property assignment
    point2.x = 15
    point2.y = 25
    assert point2.x == 15
    assert point2.y == 25


def test_size():
    """Test Size_ class functionality."""
    size = Size(100, 200)
    assert size.width == 100
    assert size.height == 200

    # Test default constructor
    size2 = Size()
    assert size2.width == 0
    assert size2.height == 0

    # Test property assignment
    size2.width = 150
    size2.height = 250
    assert size2.width == 150
    assert size2.height == 250


def test_isize():
    """Test ISize_ class functionality."""
    isize = ISize(100, 200)
    assert isize.width == 100
    assert isize.height == 200

    # Test default constructor
    isize2 = ISize()
    assert isize2.width == 0
    assert isize2.height == 0

    # Test property assignment
    isize2.width = 150
    isize2.height = 250
    assert isize2.width == 150
    assert isize2.height == 250


def test_range():
    """Test Range_ class functionality."""
    range_obj = Range(5, 10)
    assert range_obj.start == 5
    assert range_obj.end == 10

    # Test default constructor
    range2 = Range()
    assert range2.start == 0
    assert range2.end == 0

    # Test property assignment
    range2.start = 15
    range2.end = 25
    assert range2.start == 15
    assert range2.end == 25


def test_matrix():
    """Test Matrix_ class functionality."""
    # Create a matrix with identity values
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

    # Test getitem
    assert matrix[0] == 1.0
    assert matrix[5] == 1.0
    assert matrix[10] == 1.0
    assert matrix[15] == 1.0

    # Test setitem
    matrix[0] = 2.0
    assert matrix[0] == 2.0

    # Test to_list
    matrix_list = matrix.to_list()
    assert len(matrix_list) == 16
    assert matrix_list[0] == 2.0  # The value we changed
    assert matrix_list[5] == 1.0
    assert matrix_list[10] == 1.0
    assert matrix_list[15] == 1.0


def test_color_matrix():
    """Test ColorMatrix_ class functionality."""
    # Create a color matrix with identity values plus color vector
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
        1.0,
        0.2,
        0.3,
        1.0,  # Color vector
    ]
    color_matrix = ColorMatrix_(values)

    # Test getitem
    assert color_matrix[0] == 1.0
    assert color_matrix[5] == 1.0
    assert color_matrix[10] == 1.0
    assert color_matrix[15] == 1.0
    assert color_matrix[16] == 1
    assert color_matrix[19] == 1

    # Test setitem
    color_matrix[0] = 2.0
    color_matrix[16] = 0.5
    assert color_matrix[0] == 2.0
    assert color_matrix[16] == 0.5

    # Test to_list
    matrix_list = color_matrix.to_list()
    assert len(matrix_list) == 20
    assert matrix_list[0] == 2.0  # The value we changed
    assert matrix_list[16] == 0.5  # The value we changed


def test_rounding_radii():
    """Test RoundingRadii_ class functionality."""
    radii = RoundingRadii_()

    # Test default values
    assert radii.top_left.x == 0
    assert radii.top_left.y == 0
    assert radii.bottom_left.x == 0
    assert radii.bottom_left.y == 0
    assert radii.top_right.x == 0
    assert radii.top_right.y == 0
    assert radii.bottom_right.x == 0
    assert radii.bottom_right.y == 0

    # Test property assignment
    radii.top_left.x = 5
    radii.top_left.y = 5
    radii.bottom_left.x = 10
    radii.bottom_left.y = 10
    radii.top_right.x = 15
    radii.top_right.y = 15
    radii.bottom_right.x = 20
    radii.bottom_right.y = 20

    assert radii.top_left.x == 5
    assert radii.top_left.y == 5
    assert radii.bottom_left.x == 10
    assert radii.bottom_left.y == 10
    assert radii.top_right.x == 15
    assert radii.top_right.y == 15
    assert radii.bottom_right.x == 20
    assert radii.bottom_right.y == 20


def test_color():
    """Test Color_ class functionality."""
    color = Color_()

    # Test default values
    assert color.red == 0
    assert color.green == 0
    assert color.blue == 0
    assert color.alpha == 0
    assert color.color_space == ColorSpace.SRGB

    # Test property assignment
    color.red = 1
    color.green = 1
    color.blue = 1
    color.alpha = 1
    color.color_space = ColorSpace.DISPLAY_P3

    assert color.red == 1
    assert color.green == 1
    assert color.blue == 1
    assert color.alpha == 1
    assert color.color_space == ColorSpace.DISPLAY_P3


def test_texture_descriptor():
    """Test TextureDescriptor_ class functionality."""
    desc = TextureDescriptor_()

    # Test default values
    assert desc.pixel_format == PixelFormat.RGBA8888
    assert desc.size.width == 0
    assert desc.size.height == 0
    assert desc.mip_count == 0

    # Test property assignment
    desc.pixel_format = PixelFormat.RGBA8888
    desc.size.width = 100
    desc.size.height = 200
    desc.mip_count = 1

    assert desc.pixel_format == PixelFormat.RGBA8888
    assert desc.size.width == 100
    assert desc.size.height == 200
    assert desc.mip_count == 1
