#include "bindings.h"

#include <nanobind/stl/unique_ptr.h>
#include <impeller.hpp>
#include <memory>

#include "window.h"

namespace impeller::py {

namespace nb = nanobind;

using namespace impeller::hpp;

static void BindAttributes(nb::module_& m) {
  // Version
  m.def("get_version", &ImpellerGetVersion, "Get the Impeller API version.");
  m.attr("VERSION") = IMPELLER_VERSION;
  m.attr("VERSION_VARIANT") = IMPELLER_VERSION_GET_VARIANT(IMPELLER_VERSION);
  m.attr("VERSION_MAJOR") = IMPELLER_VERSION_GET_MAJOR(IMPELLER_VERSION);
  m.attr("VERSION_MINOR") = IMPELLER_VERSION_GET_MINOR(IMPELLER_VERSION);
  m.attr("VERSION_PATCH") = IMPELLER_VERSION_GET_PATCH(IMPELLER_VERSION);
}

static void BindEnums(nb::module_& m) {
  // Enums
  nb::enum_<ImpellerFillType>(m, "FillType_")
      .value("NON_ZERO", kImpellerFillTypeNonZero)
      .value("ODD", kImpellerFillTypeOdd);

  nb::enum_<ImpellerClipOperation>(m, "ClipOperation_")
      .value("DIFFERENCE", kImpellerClipOperationDifference)
      .value("INTERSECT", kImpellerClipOperationIntersect);

  nb::enum_<ImpellerBlendMode>(m, "BlendMode_")
      .value("CLEAR", kImpellerBlendModeClear)
      .value("SOURCE", kImpellerBlendModeSource)
      .value("DESTINATION", kImpellerBlendModeDestination)
      .value("SOURCE_OVER", kImpellerBlendModeSourceOver)
      .value("DESTINATION_OVER", kImpellerBlendModeDestinationOver)
      .value("SOURCE_IN", kImpellerBlendModeSourceIn)
      .value("DESTINATION_IN", kImpellerBlendModeDestinationIn)
      .value("SOURCE_OUT", kImpellerBlendModeSourceOut)
      .value("DESTINATION_OUT", kImpellerBlendModeDestinationOut)
      .value("SOURCE_ATOP", kImpellerBlendModeSourceATop)
      .value("DESTINATION_ATOP", kImpellerBlendModeDestinationATop)
      .value("XOR", kImpellerBlendModeXor)
      .value("PLUS", kImpellerBlendModePlus)
      .value("MODULATE", kImpellerBlendModeModulate)
      .value("SCREEN", kImpellerBlendModeScreen)
      .value("OVERLAY", kImpellerBlendModeOverlay)
      .value("DARKEN", kImpellerBlendModeDarken)
      .value("LIGHTEN", kImpellerBlendModeLighten)
      .value("COLOR_DODGE", kImpellerBlendModeColorDodge)
      .value("COLOR_BURN", kImpellerBlendModeColorBurn)
      .value("HARD_LIGHT", kImpellerBlendModeHardLight)
      .value("SOFT_LIGHT", kImpellerBlendModeSoftLight)
      .value("DIFFERENCE", kImpellerBlendModeDifference)
      .value("EXCLUSION", kImpellerBlendModeExclusion)
      .value("MULTIPLY", kImpellerBlendModeMultiply)
      .value("HUE", kImpellerBlendModeHue)
      .value("SATURATION", kImpellerBlendModeSaturation)
      .value("COLOR", kImpellerBlendModeColor)
      .value("LUMINOSITY", kImpellerBlendModeLuminosity);

  nb::enum_<ImpellerDrawStyle>(m, "DrawStyle_")
      .value("FILL", kImpellerDrawStyleFill)
      .value("STROKE", kImpellerDrawStyleStroke)
      .value("STROKE_AND_FILL", kImpellerDrawStyleStrokeAndFill);

  nb::enum_<ImpellerStrokeCap>(m, "StrokeCap_")
      .value("BUTT", kImpellerStrokeCapButt)
      .value("ROUND", kImpellerStrokeCapRound)
      .value("SQUARE", kImpellerStrokeCapSquare);

  nb::enum_<ImpellerStrokeJoin>(m, "StrokeJoin_")
      .value("MITER", kImpellerStrokeJoinMiter)
      .value("ROUND", kImpellerStrokeJoinRound)
      .value("BEVEL", kImpellerStrokeJoinBevel);

  nb::enum_<ImpellerPixelFormat>(m, "PixelFormat_")
      .value("RGBA8888", kImpellerPixelFormatRGBA8888);

  nb::enum_<ImpellerTextureSampling>(m, "TextureSampling_")
      .value("NEAREST_NEIGHBOR", kImpellerTextureSamplingNearestNeighbor)
      .value("LINEAR", kImpellerTextureSamplingLinear);

  nb::enum_<ImpellerTileMode>(m, "TileMode_")
      .value("CLAMP", kImpellerTileModeClamp)
      .value("REPEAT", kImpellerTileModeRepeat)
      .value("MIRROR", kImpellerTileModeMirror)
      .value("DECAL", kImpellerTileModeDecal);

  nb::enum_<ImpellerBlurStyle>(m, "BlurStyle_")
      .value("NORMAL", kImpellerBlurStyleNormal)
      .value("SOLID", kImpellerBlurStyleSolid)
      .value("OUTER", kImpellerBlurStyleOuter)
      .value("INNER", kImpellerBlurStyleInner);

  nb::enum_<ImpellerColorSpace>(m, "ColorSpace_")
      .value("SRGB", kImpellerColorSpaceSRGB)
      .value("EXTENDED_SRGB", kImpellerColorSpaceExtendedSRGB)
      .value("DISPLAY_P3", kImpellerColorSpaceDisplayP3);

  nb::enum_<ImpellerFontWeight>(m, "FontWeight_")
      .value("W100", kImpellerFontWeight100)
      .value("W200", kImpellerFontWeight200)
      .value("W300", kImpellerFontWeight300)
      .value("W400", kImpellerFontWeight400)
      .value("W500", kImpellerFontWeight500)
      .value("W600", kImpellerFontWeight600)
      .value("W700", kImpellerFontWeight700)
      .value("W800", kImpellerFontWeight800)
      .value("W900", kImpellerFontWeight900);

  nb::enum_<ImpellerFontStyle>(m, "FontStyle_")
      .value("NORMAL", kImpellerFontStyleNormal)
      .value("ITALIC", kImpellerFontStyleItalic);

  nb::enum_<ImpellerTextAlignment>(m, "TextAlignment_")
      .value("LEFT", kImpellerTextAlignmentLeft)
      .value("RIGHT", kImpellerTextAlignmentRight)
      .value("CENTER", kImpellerTextAlignmentCenter)
      .value("JUSTIFY", kImpellerTextAlignmentJustify)
      .value("START", kImpellerTextAlignmentStart)
      .value("END", kImpellerTextAlignmentEnd);

  nb::enum_<ImpellerTextDirection>(m, "TextDirection_")
      .value("RTL", kImpellerTextDirectionRTL)
      .value("LTR", kImpellerTextDirectionLTR);
}

static void BindStructs(nb::module_& m) {
  // Structs
  nb::class_<ImpellerRect>(m, "Rect_")
      .def(nb::init<>())
      .def_rw("x", &ImpellerRect::x)
      .def_rw("y", &ImpellerRect::y)
      .def_rw("width", &ImpellerRect::width)
      .def_rw("height", &ImpellerRect::height);

  nb::class_<ImpellerPoint>(m, "Point_")
      .def(nb::init<>())
      .def_rw("x", &ImpellerPoint::x)
      .def_rw("y", &ImpellerPoint::y);

  nb::class_<ImpellerSize>(m, "Size_")
      .def(nb::init<>())
      .def_rw("width", &ImpellerSize::width)
      .def_rw("height", &ImpellerSize::height);

  nb::class_<ImpellerISize>(m, "ISize_")
      .def(nb::init<>())
      .def_rw("width", &ImpellerISize::width)
      .def_rw("height", &ImpellerISize::height);

  nb::class_<ImpellerRange>(m, "Range_")
      .def(nb::init<>())
      .def_rw("start", &ImpellerRange::start)
      .def_rw("end", &ImpellerRange::end);

  nb::class_<ImpellerMatrix>(m, "Matrix_")
      .def("__init__",
           [](ImpellerMatrix* t, nb::list list) {
             new (t) ImpellerMatrix();
             const auto size = std::min<size_t>(16, list.size());
             for (size_t i = 0; i < size; i++) {
               t->m[i] = nb::cast<float>(list[i]);
             }
           })
      .def("__getitem__",
           [](const ImpellerMatrix& mat, int i) -> float { return mat.m[i]; })
      .def("__setitem__",
           [](ImpellerMatrix& mat, int i, float value) { mat.m[i] = value; })
      .def("to_list", [](const ImpellerMatrix& m) {
        nb::list result;
        for (size_t i = 0; i < 16; i++) {
          result.append(m.m[i]);
        }
        return result;
      });

  nb::class_<ImpellerColorMatrix>(m, "ColorMatrix_")
      .def(nb::init<>())
      .def("__init__",
           [](ImpellerColorMatrix* t, nb::list list) {
             new (t) ImpellerColorMatrix();
             const auto size = std::min<size_t>(20, list.size());
             for (size_t i = 0; i < size; i++) {
               t->m[i] = nb::cast<float>(list[i]);
             }
           })
      .def("__getitem__",
           [](const ImpellerColorMatrix& mat, int i) -> float {
             return mat.m[i];
           })
      .def("__setitem__", [](ImpellerColorMatrix& mat, int i,
                             float value) { mat.m[i] = value; })
      .def("to_list", [](const ImpellerColorMatrix& m) {
        nb::list result;
        for (size_t i = 0; i < 20; i++) {
          result.append(m.m[i]);
        }
        return result;
      });

  nb::class_<ImpellerRoundingRadii>(m, "RoundingRadii_")
      .def(nb::init<>())
      .def_rw("top_left", &ImpellerRoundingRadii::top_left)
      .def_rw("bottom_left", &ImpellerRoundingRadii::bottom_left)
      .def_rw("top_right", &ImpellerRoundingRadii::top_right)
      .def_rw("bottom_right", &ImpellerRoundingRadii::bottom_right);

  nb::class_<ImpellerColor>(m, "Color_")
      .def(nb::init<>())
      .def_rw("red", &ImpellerColor::red)
      .def_rw("green", &ImpellerColor::green)
      .def_rw("blue", &ImpellerColor::blue)
      .def_rw("alpha", &ImpellerColor::alpha)
      .def_rw("color_space", &ImpellerColor::color_space);

  nb::class_<ImpellerTextureDescriptor>(m, "TextureDescriptor_")
      .def(nb::init<>())
      .def_rw("pixel_format", &ImpellerTextureDescriptor::pixel_format)
      .def_rw("size", &ImpellerTextureDescriptor::size)
      .def_rw("mip_count", &ImpellerTextureDescriptor::mip_count);
}

static void BindColorFilter(nb::module_& m) {
  nb::class_<ColorFilter>(m, "ColorFilter_")
      .def_static(
          "blend",
          [](const ImpellerColor& color, const ImpellerBlendMode& blend_mode) {
            return ColorFilter::Blend(color, blend_mode);
          })
      .def_static("matrix", [](const ImpellerColorMatrix& matrix) {
        return ColorFilter::Matrix(matrix);
      });
}

static void BindColorSource(nb::module_& m) {
  nb::class_<ColorSource>(m, "ColorSource_");
}

static void BindImageFilter(nb::module_& m) {
  nb::class_<ImageFilter>(m, "ImageFilter_");
}

static void BindLineMetrics(nb::module_& m) {
  nb::class_<LineMetrics>(m, "LineMetrics_");
}

static void BindPath(nb::module_& m) {
  nb::class_<Path>(m, "Path_");
}

static void BindGlyphInfo(nb::module_& m) {
  nb::class_<GlyphInfo>(m, "GlyphInfo_");
}

static void BindParagraph(nb::module_& m) {
  nb::class_<Paragraph>(m, "Paragraph_")
      .def("alphabetic_baseline", &Paragraph::GetAlphabeticBaseline)
      .def("height", &Paragraph::GetHeight)
      .def("ideographic_baseline", &Paragraph::GetIdeographicBaseline)
      .def("line_count", &Paragraph::GetLineCount)
      .def("longest_line_width", &Paragraph::GetLongestLineWidth)
      .def("max_intrinsic_width", &Paragraph::GetMaxIntrinsicWidth)
      .def("max_width", &Paragraph::GetMaxWidth)
      .def("min_intrinsic_width", &Paragraph::GetMinIntrinsicWidth)
      .def("line_metrics", &Paragraph::GetLineMetrics)
      .def("glyph_info_at_code_unit_index",
           &Paragraph::GlyphInfoAtCodeUnitIndex)
      .def("glyph_info_at_paragraph_coordinate",
           &Paragraph::GlyphInfoAtParagraphCoordinates)
      .def("word_boundary", &Paragraph::GetWordBoundary);
}

static void BindTexture(nb::module_& m) {
  nb::class_<Texture>(m, "Texture_")
      .def_static("with_contents",
                  [](const Context& context,                 //
                     const ImpellerTextureDescriptor& desc,  //
                     nb::bytes data                          //
                     ) -> Texture {
                    auto mapping = std::make_unique<Mapping>(
                        reinterpret_cast<const uint8_t*>(data.data()),  //
                        data.size(),                                    //
                        nullptr                                         //
                    );
                    return Texture::WithContents(context, desc,
                                                 std::move(mapping));
                  });
}

static void BindPathBuilder(nb::module_& m) {
  nb::class_<PathBuilder>(m, "PathBuilder_")
      .def("build_copy", &PathBuilder::BuildCopy, nb::rv_policy::move)
      .def("build", &PathBuilder::Build, nb::rv_policy::move)
      .def("add_arc", &PathBuilder::AddArc, nb::rv_policy::reference)
      .def("add_oval", &PathBuilder::AddOval, nb::rv_policy::reference)
      .def("add_rect", &PathBuilder::AddRect, nb::rv_policy::reference)
      .def("add_rounded_rect", &PathBuilder::AddRoundedRect,
           nb::rv_policy::reference)
      .def("close", &PathBuilder::Close, nb::rv_policy::reference)
      .def("cubic_curve_to", &PathBuilder::CubicCurveTo,
           nb::rv_policy::reference)
      .def("line_to", &PathBuilder::LineTo, nb::rv_policy::reference)
      .def("move_to", &PathBuilder::MoveTo, nb::rv_policy::reference)
      .def("quadratic_curve_to", &PathBuilder::QuadraticCurveTo,
           nb::rv_policy::reference);
}

static void BindMaskFilter(nb::module_& m) {
  nb::class_<MaskFilter>(m, "MaskFilter_");
}

static void BindPaint(nb::module_& m) {
  nb::class_<Paint>(m, "Paint_")
      .def(nb::init())
      .def("set_color", &Paint::SetColor, nb::rv_policy::reference)
      .def("set_blend_mode", &Paint::SetBlendMode, nb::rv_policy::reference)
      .def("set_draw_style", &Paint::SetDrawStyle, nb::rv_policy::reference)
      .def("set_stroke_cap", &Paint::SetStrokeCap, nb::rv_policy::reference)
      .def("set_stroke_join", &Paint::SetStrokeJoin, nb::rv_policy::reference)
      .def("set_stroke_width", &Paint::SetStrokeWidth, nb::rv_policy::reference)
      .def("set_stroke_miter", &Paint::SetStrokeMiter, nb::rv_policy::reference)
      .def("set_color_filter", &Paint::SetColorFilter, nb::rv_policy::reference)
      .def("set_color_source", &Paint::SetColorSource, nb::rv_policy::reference)
      .def("set_image_filter", &Paint::SetImageFilter, nb::rv_policy::reference)
      .def("set_mask_filter", &Paint::SetMaskFilter, nb::rv_policy::reference);
}

static void BindDisplayList(nb::module_& m) {
  nb::class_<DisplayList> _(m, "DisplayList_");
}

static void BindDisplayListBuilder(nb::module_& m) {
  nb::class_<DisplayListBuilder>(m, "DisplayListBuilder_")
      .def(nb::init())
      .def("build", &DisplayListBuilder::Build, nb::rv_policy::reference)
      .def("clip_oval", &DisplayListBuilder::ClipOval, nb::rv_policy::reference)
      .def("clip_path", &DisplayListBuilder::ClipPath, nb::rv_policy::reference)
      .def("clip_rect", &DisplayListBuilder::ClipRect, nb::rv_policy::reference)
      .def("clip_rounded_rect", &DisplayListBuilder::ClipRoundedRect,
           nb::rv_policy::reference)
      .def("draw_dashed_line", &DisplayListBuilder::DrawDashedLine,
           nb::rv_policy::reference)
      .def("draw_display_list", &DisplayListBuilder::DrawDisplayList,
           nb::rv_policy::reference)
      .def("draw_line", &DisplayListBuilder::DrawLine, nb::rv_policy::reference)
      .def("draw_oval", &DisplayListBuilder::DrawOval, nb::rv_policy::reference)
      .def("draw_paint", &DisplayListBuilder::DrawPaint,
           nb::rv_policy::reference)
      .def("draw_paragraph", &DisplayListBuilder::DrawParagraph,
           nb::rv_policy::reference)
      .def("draw_shadow", &DisplayListBuilder::DrawShadow,
           nb::rv_policy::reference)
      .def("draw_path", &DisplayListBuilder::DrawPath, nb::rv_policy::reference)
      .def("draw_rect", &DisplayListBuilder::DrawRect, nb::rv_policy::reference)
      .def("draw_rounded_rect", &DisplayListBuilder::DrawRoundedRect,
           nb::rv_policy::reference)
      .def("draw_rounded_rect_difference",
           &DisplayListBuilder::DrawRoundedRectDifference,
           nb::rv_policy::reference)
      .def("draw_texture", &DisplayListBuilder::DrawTexture,
           nb::rv_policy::reference)
      .def("draw_texture_rect", &DisplayListBuilder::DrawTextureRect,
           nb::rv_policy::reference)
      .def("save_count", &DisplayListBuilder::GetSaveCount)
      .def("reset_transform", &DisplayListBuilder::ResetTransform,
           nb::rv_policy::reference)
      .def("restore", &DisplayListBuilder::Restore, nb::rv_policy::reference)
      .def("restore_to_count", &DisplayListBuilder::RestoreToCount,
           nb::rv_policy::reference)
      .def("rotate", &DisplayListBuilder::Rotate, nb::rv_policy::reference)
      .def("save", &DisplayListBuilder::Save, nb::rv_policy::reference)
      .def("save_layer", &DisplayListBuilder::SaveLayer,
           nb::rv_policy::reference)
      .def("scale", &DisplayListBuilder::Scale, nb::rv_policy::reference)
      .def("get_transform", &DisplayListBuilder::GetTransform)
      .def("set_transform", &DisplayListBuilder::SetTransform,
           nb::rv_policy::reference)
      .def("push_transform", &DisplayListBuilder::Transform,
           nb::rv_policy::reference)
      .def("translate", &DisplayListBuilder::Translate,
           nb::rv_policy::reference);
}

static void BindWindow(nb::module_& m) {
  nb::class_<Window>(m, "Window_")
      .def(nb::init())
      .def("create_render_surface", &Window::CreateRenderSurface,
           nb::rv_policy::move)
      .def("should_close", &Window::ShouldClose)
      .def("poll_events", &Window::PollEvents);
}

static ImpellerContext CreateContextNew() {
  return ImpellerContextCreateMetalNew(IMPELLER_VERSION);
}

static void BindContext(nb::module_& m) {
  nb::class_<Context>(m, "Context_").def("__init__", [](Context* t) {
    new (t) Context(CreateContextNew(), AdoptTag::kAdopt);
  });
}

static void BindTypographyContext(nb::module_& m) {
  nb::class_<TypographyContext>(m, "TypographyContext_").def(nb::init());
}

static void BindParagraphStyle(nb::module_& m) {
  nb::class_<ParagraphStyle>(m, "ParagraphStyle_")
      .def(nb::init())
      .def("set_background", &ParagraphStyle::SetBackground,
           nb::rv_policy::reference)
      .def("set_font_family", &ParagraphStyle::SetFontFamily,
           nb::rv_policy::reference)
      .def("set_font_size", &ParagraphStyle::SetFontSize,
           nb::rv_policy::reference)
      .def("set_font_style", &ParagraphStyle::SetFontStyle,
           nb::rv_policy::reference)
      .def("set_font_weight", &ParagraphStyle::SetFontWeight,
           nb::rv_policy::reference)
      .def("set_font_foreground", &ParagraphStyle::SetForeground,
           nb::rv_policy::reference)
      .def("set_height", &ParagraphStyle::SetHeight, nb::rv_policy::reference)
      .def("set_locale", &ParagraphStyle::SetLocale, nb::rv_policy::reference)
      .def("set_max_lines", &ParagraphStyle::SetMaxLines,
           nb::rv_policy::reference)
      .def("set_text_alignment", &ParagraphStyle::SetTextAlignment,
           nb::rv_policy::reference)
      .def("set_text_direction", &ParagraphStyle::SetTextDirection,
           nb::rv_policy::reference);
}

static void BindParagraphBuilder(nb::module_& m) {
  nb::class_<ParagraphBuilder>(m, "ParagraphBuilder_")
      .def(nb::init<TypographyContext>())
      .def("build", &ParagraphBuilder::Build, nb::rv_policy::move)
      .def("push_style", &ParagraphBuilder::PushStyle, nb::rv_policy::reference)
      .def("pop_style", &ParagraphBuilder::PopStyle, nb::rv_policy::reference)
      .def(
          "add_text",
          [](ParagraphBuilder& self, nb::str text) -> ParagraphBuilder& {
            const auto str = text.c_str();
            const auto len = strlen(str);
            return self.AddText(reinterpret_cast<const uint8_t*>(str), len);
          },
          nb::rv_policy::reference);
}

void BindSurface(nb::module_& m) {
  nb::class_<Surface>(m, "Surface_")
      .def("draw", &Surface::Draw)
      .def("present", &Surface::Present);
}

void BindImpeller(nb::module_& m) {
  BindAttributes(m);
  BindColorFilter(m);
  BindColorSource(m);
  BindContext(m);
  BindDisplayList(m);
  BindDisplayListBuilder(m);
  BindEnums(m);
  BindGlyphInfo(m);
  BindImageFilter(m);
  BindLineMetrics(m);
  BindMaskFilter(m);
  BindPaint(m);
  BindParagraph(m);
  BindPath(m);
  BindPathBuilder(m);
  BindStructs(m);
  BindSurface(m);
  BindTexture(m);
  BindWindow(m);
  BindParagraphBuilder(m);
  BindParagraphStyle(m);
  BindTypographyContext(m);
}

}  // namespace impeller::py
