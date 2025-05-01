from impeller.impeller import *
from impeller.impellerpy import *


def test_paragraph_builder_comprehensive():
    """Test all features of the ParagraphBuilder class."""
    # Create typography context
    typography_ctx = TypographyContext()
    
    # Create a paragraph builder
    builder = ParagraphBuilder(typography_ctx)
    
    # Test push_style with various font settings
    style1 = ParagraphStyle()
    style1.set_font_family("Arial")
    style1.set_font_size(24.0)
    style1.set_font_weight(FontWeight.W700)  # Bold
    style1.set_font_style(FontStyle.NORMAL)
    style1.set_text_alignment(TextAlignment.LEFT)
    style1.set_text_direction(TextDirection.LTR)
    style1.set_height(1.5)  # Line height multiplier
    style1.set_max_lines(10)
    style1.set_locale("en_US")
    
    # Set foreground color
    fg_paint = Paint()
    fg_paint.set_color(Color(r=0.8, g=0.2, b=0.2, a=1.0))
    style1.set_font_foreground(fg_paint)
    
    # Set background color
    bg_paint = Paint()
    bg_paint.set_color(Color(r=0.9, g=0.9, b=0.9, a=0.3))
    style1.set_background(bg_paint)
    
    # Push the style and add text
    builder.push_style(style1)
    builder.add_text("This is a test paragraph with bold text.\n")
    
    # Test another style
    style2 = ParagraphStyle()
    style2.set_font_family("Times New Roman")
    style2.set_font_size(18.0)
    style2.set_font_weight(FontWeight.W400)  # Normal
    style2.set_font_style(FontStyle.ITALIC)
    style2.set_text_alignment(TextAlignment.CENTER)
    
    # Set a different foreground color
    fg_paint2 = Paint()
    fg_paint2.set_color(Color(r=0.2, g=0.2, b=0.8, a=1.0))
    style2.set_font_foreground(fg_paint2)
    
    # Push the new style and add more text
    builder.push_style(style2)
    builder.add_text("This is italic text with a different style.\n")
    
    # Test pop_style to return to previous style
    builder.pop_style()
    builder.add_text("Back to the original style.\n")
    
    # Test style with right alignment
    style3 = ParagraphStyle()
    style3.set_font_family("Courier New")
    style3.set_font_size(16.0)
    style3.set_text_alignment(TextAlignment.RIGHT)
    
    # Set another foreground color
    fg_paint3 = Paint()
    fg_paint3.set_color(Color(r=0.2, g=0.8, b=0.2, a=1.0))
    style3.set_font_foreground(fg_paint3)
    
    builder.push_style(style3)
    builder.add_text("Right-aligned text with a monospace font.\n")
    
    # Build the paragraph with a specific width
    paragraph = builder.build(400.0)
    
    # Test paragraph properties
    assert paragraph.line_count() > 0
    assert paragraph.height() > 0
    assert paragraph.max_width() == 400.0
    
    # Test line metrics
    line_metrics = paragraph.line_metrics()
    for i in range(paragraph.line_count()):
        # Just verify these methods don't crash
        line_metrics.ascent(i)
        line_metrics.descent(i)
        line_metrics.width(i)
        line_metrics.height(i)
        line_metrics.baseline(i)
        line_metrics.left(i)
        line_metrics.is_hardbreak(i)
        line_metrics.code_unit_start_index(i)
        line_metrics.code_unit_end_index(i)
    
    # Test glyph info
    if paragraph.line_count() > 0:
        first_line_end = line_metrics.code_unit_end_index(0)
        if first_line_end > 0:
            glyph_info = paragraph.glyph_info_at_code_unit_index(1)
            # Verify glyph info methods
            glyph_info.grapheme_cluster_code_unit_range_begin()
            glyph_info.grapheme_cluster_code_unit_range_end()
            glyph_info.grapheme_cluster_bounds()
            glyph_info.is_ellipsis()
            glyph_info.text_direction()
            
            # Test word boundary
            word_boundary = paragraph.word_boundary(1)
            assert isinstance(word_boundary, Range_)
    
    # Test rendering the paragraph in a display list
    dl_builder = DisplayListBuilder()
    dl_builder.draw_paragraph(paragraph, Point(50, 50))
    display_list = dl_builder.build()
    
    # The test passes if we get here without exceptions
    assert display_list is not None


def test_paragraph_builder_with_multiple_languages():
    """Test paragraph builder with text in multiple languages."""
    typography_ctx = TypographyContext()
    builder = ParagraphBuilder(typography_ctx)
    
    # English style
    en_style = ParagraphStyle()
    en_style.set_font_family("Arial")
    en_style.set_font_size(24.0)
    en_style.set_locale("en_US")
    en_style.set_font_foreground(Paint().set_color(Color(r=0.0, g=0.0, b=0.0, a=1.0)))
    
    # Japanese style
    jp_style = ParagraphStyle()
    jp_style.set_font_family("Hiragino Sans")
    jp_style.set_font_size(24.0)
    jp_style.set_locale("ja_JP")
    jp_style.set_font_foreground(Paint().set_color(Color(r=0.8, g=0.0, b=0.0, a=1.0)))
    
    # Arabic style with RTL
    ar_style = ParagraphStyle()
    ar_style.set_font_family("Arial")
    ar_style.set_font_size(24.0)
    ar_style.set_locale("ar_SA")
    ar_style.set_text_direction(TextDirection.RTL)
    ar_style.set_font_foreground(Paint().set_color(Color(r=0.0, g=0.0, b=0.8, a=1.0)))
    
    # Add English text
    builder.push_style(en_style)
    builder.add_text("Hello, world!\n")
    
    # Add Japanese text
    builder.push_style(jp_style)
    builder.add_text("こんにちは世界！\n")
    
    # Add Arabic text
    builder.push_style(ar_style)
    builder.add_text("مرحبا بالعالم!\n")
    
    # Build the paragraph
    paragraph = builder.build(500.0)
    
    # Verify paragraph was created
    assert paragraph is not None
    assert paragraph.line_count() >= 3  # At least 3 lines (one for each language)
