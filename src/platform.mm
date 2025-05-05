#include "platform.h"

#define GLFW_EXPOSE_NATIVE_COCOA
#include <GLFW/glfw3native.h>
#include <Metal/Metal.h>
#include <QuartzCore/QuartzCore.h>

namespace impeller::py {

void ApplyGLFWWindowHints() {
  ::glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);
}

bool ConfigurePlatformWindow(GLFWwindow* window) {
  NSWindow* cocoa_window = ::glfwGetCocoaWindow(window);

  if (cocoa_window == nil) {
    return false;
  }

  auto layer = [CAMetalLayer layer];
  layer.device = MTLCreateSystemDefaultDevice();
  layer.pixelFormat = MTLPixelFormatBGRA8Unorm;
  layer.framebufferOnly = NO;
  cocoa_window.contentView.layer = layer;
  cocoa_window.contentView.wantsLayer = YES;

  return true;
}

impeller::hpp::Surface WrapSurface(const impeller::hpp::Context& context,
                                   GLFWwindow* window) {
  NSWindow* cocoa_window = ::glfwGetCocoaWindow(window);
  CAMetalLayer* layer =
      reinterpret_cast<CAMetalLayer*>(cocoa_window.contentView.layer);
  float xscale = 0.0f;
  float yscale = 0.0f;
  ::glfwGetWindowContentScale(window, &xscale, &yscale);
  layer.drawableSize = CGSizeMake(layer.bounds.size.width * xscale,
                                  layer.bounds.size.height * yscale);
  return impeller::hpp::Surface::WrapMetalDrawable(context, layer.nextDrawable);
}

}  // namespace impeller::py
