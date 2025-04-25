#include <nanobind/nanobind.h>
#include <impeller.hpp>
#include <iostream>
#include <map>

namespace nb = nanobind;

namespace IMPELLER_HPP_NAMESPACE {
ProcTable gGlobalProcTable;
}  // namespace IMPELLER_HPP_NAMESPACE

class Demo {
 public:
  Demo() {
    static int count = 0;
    ++count;
    std::cout << "Creating " << count << std::endl;
  }

  ~Demo() {
    static int count = 0;
    ++count;
    std::cout << "Destroying " << count << std::endl;
  }

  Demo& Foo() {
    std::cout << "Foo" << std::endl;
    return *this;
  }

  int GetValue() const { return 42; }
};

static void SetupImpellerHPPProcTableOnce() {
  static std::once_flag sOnceFlag;
  std::call_once(sOnceFlag, []() {
    std::map<std::string, void*> proc_map;
#define IMPELLER_HPP_PROC(name) \
  proc_map[#name] = reinterpret_cast<void*>(&name);
    IMPELLER_HPP_EACH_PROC(IMPELLER_HPP_PROC)
#undef IMPELLER_HPP_PROC
    impeller::hpp::gGlobalProcTable.Initialize(
        [&](auto name) { return proc_map.at(name); });
  });
}

static void BindDisplayListBuilder(nb::module_& m) {
  nb::class_<impeller::hpp::DisplayListBuilder>(m, "DisplayListBuilder")
      .def(nb::init());

  nb::class_<Demo>(m, "Demo")
      .def(nb::init())
      .def("GetValue", &Demo::GetValue)
      .def("Foo", &Demo::Foo, nb::rv_policy::reference);
}

NB_MODULE(impellerpy, m) {
  SetupImpellerHPPProcTableOnce();

  // Version
  m.def("get_version", &ImpellerGetVersion, "Get the Impeller API version.");
  m.attr("VERSION") = IMPELLER_VERSION;
  m.attr("VERSION_VARIANT") = IMPELLER_VERSION_GET_VARIANT(IMPELLER_VERSION);
  m.attr("VERSION_MAJOR") = IMPELLER_VERSION_GET_MAJOR(IMPELLER_VERSION);
  m.attr("VERSION_MINOR") = IMPELLER_VERSION_GET_MINOR(IMPELLER_VERSION);
  m.attr("VERSION_PATCH") = IMPELLER_VERSION_GET_PATCH(IMPELLER_VERSION);

  // Enums
  nb::enum_<ImpellerFillType>(m, "FillType")
      .value("NON_ZERO", kImpellerFillTypeNonZero)
      .value("ODD", kImpellerFillTypeOdd);

  nb::enum_<ImpellerClipOperation>(m, "ClipOperation")
      .value("DIFFERENCE", kImpellerClipOperationDifference)
      .value("INTERSECT", kImpellerClipOperationIntersect);

  nb::enum_<ImpellerBlendMode>(m, "BlendMode")
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

  nb::enum_<ImpellerDrawStyle>(m, "DrawStyle")
      .value("FILL", kImpellerDrawStyleFill)
      .value("STROKE", kImpellerDrawStyleStroke)
      .value("STROKE_AND_FILL", kImpellerDrawStyleStrokeAndFill);

  nb::enum_<ImpellerStrokeCap>(m, "StrokeCap")
      .value("BUTT", kImpellerStrokeCapButt)
      .value("ROUND", kImpellerStrokeCapRound)
      .value("SQUARE", kImpellerStrokeCapSquare);

  nb::enum_<ImpellerStrokeJoin>(m, "StrokeJoin")
      .value("MITER", kImpellerStrokeJoinMiter)
      .value("ROUND", kImpellerStrokeJoinRound)
      .value("BEVEL", kImpellerStrokeJoinBevel);

  nb::enum_<ImpellerPixelFormat>(m, "PixelFormat")
      .value("RGBA8888", kImpellerPixelFormatRGBA8888);

  nb::enum_<ImpellerTextureSampling>(m, "TextureSampling")
      .value("NEAREST_NEIGHBOR", kImpellerTextureSamplingNearestNeighbor)
      .value("LINEAR", kImpellerTextureSamplingLinear);

  nb::enum_<ImpellerTileMode>(m, "TileMode")
      .value("CLAMP", kImpellerTileModeClamp)
      .value("REPEAT", kImpellerTileModeRepeat)
      .value("MIRROR", kImpellerTileModeMirror)
      .value("DECAL", kImpellerTileModeDecal);

  nb::enum_<ImpellerBlurStyle>(m, "BlurStyle")
      .value("NORMAL", kImpellerBlurStyleNormal)
      .value("SOLID", kImpellerBlurStyleSolid)
      .value("OUTER", kImpellerBlurStyleOuter)
      .value("INNER", kImpellerBlurStyleInner);

  nb::enum_<ImpellerColorSpace>(m, "ColorSpace")
      .value("SRGB", kImpellerColorSpaceSRGB)
      .value("EXTENDED_SRGB", kImpellerColorSpaceExtendedSRGB)
      .value("DISPLAY_P3", kImpellerColorSpaceDisplayP3);

  nb::enum_<ImpellerFontWeight>(m, "FontWeight")
      .value("W100", kImpellerFontWeight100)
      .value("W200", kImpellerFontWeight200)
      .value("W300", kImpellerFontWeight300)
      .value("W400", kImpellerFontWeight400)
      .value("W500", kImpellerFontWeight500)
      .value("W600", kImpellerFontWeight600)
      .value("W700", kImpellerFontWeight700)
      .value("W800", kImpellerFontWeight800)
      .value("W900", kImpellerFontWeight900);

  nb::enum_<ImpellerFontStyle>(m, "FontStyle")
      .value("NORMAL", kImpellerFontStyleNormal)
      .value("ITALIC", kImpellerFontStyleItalic);

  nb::enum_<ImpellerTextAlignment>(m, "TextAlignment")
      .value("LEFT", kImpellerTextAlignmentLeft)
      .value("RIGHT", kImpellerTextAlignmentRight)
      .value("CENTER", kImpellerTextAlignmentCenter)
      .value("JUSTIFY", kImpellerTextAlignmentJustify)
      .value("START", kImpellerTextAlignmentStart)
      .value("END", kImpellerTextAlignmentEnd);

  nb::enum_<ImpellerTextDirection>(m, "TextDirection")
      .value("RTL", kImpellerTextDirectionRTL)
      .value("LTR", kImpellerTextDirectionLTR);

  // Structs
  nb::class_<ImpellerRect>(m, "Rect")
      .def(nb::init<>())
      .def_rw("x", &ImpellerRect::x)
      .def_rw("y", &ImpellerRect::y)
      .def_rw("width", &ImpellerRect::width)
      .def_rw("height", &ImpellerRect::height);

  nb::class_<ImpellerPoint>(m, "Point")
      .def(nb::init<>())
      .def_rw("x", &ImpellerPoint::x)
      .def_rw("y", &ImpellerPoint::y);

  nb::class_<ImpellerSize>(m, "Size")
      .def(nb::init<>())
      .def_rw("width", &ImpellerSize::width)
      .def_rw("height", &ImpellerSize::height);

  nb::class_<ImpellerISize>(m, "ISize")
      .def(nb::init<>())
      .def_rw("width", &ImpellerISize::width)
      .def_rw("height", &ImpellerISize::height);

  nb::class_<ImpellerRange>(m, "Range")
      .def(nb::init<>())
      .def_rw("start", &ImpellerRange::start)
      .def_rw("end", &ImpellerRange::end);

  nb::class_<ImpellerMatrix>(m, "Matrix").def(nb::init<>())
      // .def_rw("m", &ImpellerMatrix::m)
      ;

  nb::class_<ImpellerColorMatrix>(m, "ColorMatrix").def(nb::init<>())
      // .def_rw("m", &ImpellerColorMatrix::m)
      ;

  nb::class_<ImpellerRoundingRadii>(m, "RoundingRadii")
      .def(nb::init<>())
      .def_rw("top_left", &ImpellerRoundingRadii::top_left)
      .def_rw("bottom_left", &ImpellerRoundingRadii::bottom_left)
      .def_rw("top_right", &ImpellerRoundingRadii::top_right)
      .def_rw("bottom_right", &ImpellerRoundingRadii::bottom_right);

  nb::class_<ImpellerColor>(m, "Color")
      .def(nb::init<>())
      .def_rw("red", &ImpellerColor::red)
      .def_rw("green", &ImpellerColor::green)
      .def_rw("blue", &ImpellerColor::blue)
      .def_rw("alpha", &ImpellerColor::alpha)
      .def_rw("color_space", &ImpellerColor::color_space);

  nb::class_<ImpellerTextureDescriptor>(m, "TextureDescriptor")
      .def(nb::init<>())
      .def_rw("pixel_format", &ImpellerTextureDescriptor::pixel_format)
      .def_rw("size", &ImpellerTextureDescriptor::size)
      .def_rw("mip_count", &ImpellerTextureDescriptor::mip_count);

  nb::class_<ImpellerMapping>(m, "Mapping")
      .def(nb::init<>())
      .def_rw("data", &ImpellerMapping::data)
      .def_rw("length", &ImpellerMapping::length)
      // .def_rw("on_release", &ImpellerMapping::on_release)
      ;

  nb::class_<ImpellerContextVulkanSettings>(m, "VulkanSettings")
      .def(nb::init<>())
      .def_rw("user_data", &ImpellerContextVulkanSettings::user_data)
      // .def_rw("proc_address_callback",
      //         &ImpellerContextVulkanSettings::proc_address_callback)
      .def_rw("enable_vulkan_validation",
              &ImpellerContextVulkanSettings::enable_vulkan_validation);

  nb::class_<ImpellerContextVulkanInfo>(m, "VulkanInfo")
      .def(nb::init<>())
      .def_rw("vk_instance", &ImpellerContextVulkanInfo::vk_instance)
      .def_rw("vk_physical_device",
              &ImpellerContextVulkanInfo::vk_physical_device)
      .def_rw("vk_logical_device",
              &ImpellerContextVulkanInfo::vk_logical_device)
      .def_rw("graphics_queue_family_index",
              &ImpellerContextVulkanInfo::graphics_queue_family_index)
      .def_rw("graphics_queue_index",
              &ImpellerContextVulkanInfo::graphics_queue_index);

  BindDisplayListBuilder(m);
}
