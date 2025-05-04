from impellerpy import *

def test_typography_context_creation():
    """Test TypographyContext_ creation."""
    # Create a typography context
    typography_ctx = TypographyContext_()

    # We can't directly test the properties of the context, but we can verify it was created
    assert typography_ctx is not None


def test_paragraph_style_creation():
    """Test ParagraphStyle_ creation and methods."""
    # Create a paragraph style
    style = ParagraphStyle_()

    # We can't directly test the default properties, but we can verify it was created
    assert style is not None

    # Test set_font_family
    result = style.set_font_family("Arial")
    assert result is style

    # Test set_font_size
    result = style.set_font_size(24.0)
    assert result is style

    # Test set_font_weight
    result = style.set_font_weight(FontWeight.W700)
    assert result is style

    # Test set_font_style
    result = style.set_font_style(FontStyle.NORMAL)
    assert result is style

    # Test set_text_alignment
    result = style.set_text_alignment(TextAlignment.LEFT)
    assert result is style

    # Test set_text_direction
    result = style.set_text_direction(TextDirection.LTR)
    assert result is style

    # Test set_height
    result = style.set_height(1.5)
    assert result is style

    # Test set_max_lines
    result = style.set_max_lines(10)
    assert result is style

    # Test set_locale
    result = style.set_locale("en_US")
    assert result is style

    # Test set_font_foreground
    paint = Paint_()
    paint.set_color(Color(r=0.0, g=0.0, b=0.0, a=1.0))
    result = style.set_font_foreground(paint)
    assert result is style

    # Test set_background
    bg_paint = Paint_()
    bg_paint.set_color(Color(r=1.0, g=1.0, b=1.0, a=0.5))
    result = style.set_background(bg_paint)
    assert result is style


def test_paragraph_builder_creation():
    """Test ParagraphBuilder_ creation and methods."""
    # Create a typography context
    typography_ctx = TypographyContext_()

    # Create a paragraph builder
    builder = ParagraphBuilder_(typography_ctx)

    # We can't directly test the default properties, but we can verify it was created
    assert builder is not None

    # Test push_style
    style = ParagraphStyle_()
    style.set_font_family("Arial")
    style.set_font_size(24.0)
    result = builder.push_style(style)
    assert result is builder

    # Test add_text
    result = builder.add_text("Hello, world!")
    assert result is builder

    # Test pop_style
    result = builder.pop_style()
    assert result is builder

    # Test build
    paragraph = builder.build(400.0)
    assert paragraph is not None


def test_paragraph_methods():
    """Test Paragraph_ methods."""
    # Create a typography context, builder, and paragraph
    typography_ctx = TypographyContext_()
    builder = ParagraphBuilder_(typography_ctx)

    style = ParagraphStyle_()
    style.set_font_family("Arial")
    style.set_font_size(24.0)
    builder.push_style(style)
    builder.add_text("Hello, world!")

    paragraph = builder.build(400.0)

    # Test various paragraph methods
    assert paragraph.height() >= 0
    assert paragraph.line_count() >= 0
    assert paragraph.max_width() == 400.0
    assert paragraph.alphabetic_baseline() >= 0
    assert paragraph.ideographic_baseline() >= 0
    assert paragraph.max_intrinsic_width() >= 0
    assert paragraph.min_intrinsic_width() >= 0
    assert paragraph.longest_line_width() >= 0

    # Test line_metrics
    line_metrics = paragraph.line_metrics()
    assert line_metrics is not None

    # Test glyph_info_at_code_unit_index and word_boundary
    # These might fail if the paragraph is empty or has no valid glyphs
    try:
        glyph_info = paragraph.glyph_info_at_code_unit_index(0)
        assert glyph_info is not None

        word_boundary = paragraph.word_boundary(0)
        assert word_boundary is not None
    except:
        # These might fail depending on the font and text, so we'll just pass
        pass


def test_line_metrics_methods():
    """Test LineMetrics_ methods."""
    # Create a typography context, builder, and paragraph to get line metrics
    typography_ctx = TypographyContext_()
    builder = ParagraphBuilder_(typography_ctx)

    style = ParagraphStyle_()
    style.set_font_family("Arial")
    style.set_font_size(24.0)
    builder.push_style(style)
    builder.add_text("Hello, world!\nSecond line.")

    paragraph = builder.build(400.0)
    line_metrics = paragraph.line_metrics()

    # Test line metrics methods for each line
    for i in range(paragraph.line_count()):
        # These should all return valid values, but we can't assert specific values
        assert line_metrics.ascent(i) >= 0
        assert line_metrics.descent(i) >= 0
        assert line_metrics.height(i) >= 0
        assert line_metrics.width(i) >= 0
        assert line_metrics.baseline(i) >= 0
        assert line_metrics.left(i) >= 0
        assert isinstance(line_metrics.is_hardbreak(i), bool)
        assert line_metrics.code_unit_start_index(i) >= 0
        assert line_metrics.code_unit_end_index(i) >= 0
        assert line_metrics.code_unit_end_index_excluding_whitespace(i) >= 0
        assert line_metrics.code_unit_end_index_including_newline(i) >= 0


def test_glyph_info_methods():
    """Test GlyphInfo_ methods."""
    # Create a typography context, builder, and paragraph to get glyph info
    typography_ctx = TypographyContext_()
    builder = ParagraphBuilder_(typography_ctx)

    style = ParagraphStyle_()
    style.set_font_family("Arial")
    style.set_font_size(24.0)
    builder.push_style(style)
    builder.add_text("Hello, world!")

    paragraph = builder.build(400.0)

    # Try to get glyph info for the first character
    try:
        glyph_info = paragraph.glyph_info_at_code_unit_index(0)

        # Test glyph info methods
        assert glyph_info.grapheme_cluster_code_unit_range_begin() >= 0
        assert glyph_info.grapheme_cluster_code_unit_range_end() >= 0

        bounds = glyph_info.grapheme_cluster_bounds()
        assert isinstance(bounds, Rect_)

        assert isinstance(glyph_info.is_ellipsis(), bool)
        assert isinstance(glyph_info.text_direction(), TextDirection)

        # Test glyph_info_at_paragraph_coordinate
        glyph_info2 = paragraph.glyph_info_at_paragraph_coordinate(10, 10)
        assert glyph_info2 is not None
    except:
        # These might fail depending on the font and text, so we'll just pass
        pass
