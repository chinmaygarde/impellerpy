#include "platform.h"

namespace impeller::py {

void ApplyGLFWWindowHints() {
  ::glfwWindowHint(GLFW_CLIENT_API, GLFW_OPENGL_ES_API);
  ::glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 2);
  ::glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 0);
  ::glfwWindowHint(GLFW_RED_BITS, 8);
  ::glfwWindowHint(GLFW_GREEN_BITS, 8);
  ::glfwWindowHint(GLFW_BLUE_BITS, 8);
  ::glfwWindowHint(GLFW_ALPHA_BITS, 8);
  ::glfwWindowHint(GLFW_DEPTH_BITS, 32);   // 32 bit depth buffer
  ::glfwWindowHint(GLFW_STENCIL_BITS, 8);  // 8 bit stencil buffer
  ::glfwWindowHint(GLFW_SAMPLES, 4);       // 4xMSAA
}

bool ConfigurePlatformWindow(GLFWwindow* window) {
  glfwMakeContextCurrent(window);
  return true;
}

impeller::hpp::Surface WrapSurface(const impeller::hpp::Context& context,
                                   GLFWwindow* window) {
  int width = 0;
  int height = 0;
  ::glfwGetFramebufferSize(window, &width, &height);
  return hpp::Surface::WrapFBO(context, 0u, kImpellerPixelFormatRGBA8888,
                               ImpellerISize{
                                   .width = width,
                                   .height = height,
                               });
}

}  // namespace impeller::py
