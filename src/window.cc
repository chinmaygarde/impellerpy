#include "window.h"

#include "cocoa.h"

namespace impeller::py {

Window::Window() {
  glm::ivec2 size = {800, 600};
  ::glfwDefaultWindowHints();
  ::glfwWindowHint(GLFW_VISIBLE, GLFW_TRUE);
  ::glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);

  window_ = ::glfwCreateWindow(size.x, size.y, "Window", nullptr, nullptr);
  ::glfwSetWindowUserPointer(window_, this);

  ConfigureCocoaWindow(window_);
}

Window::~Window() {
  if (window_) {
    ::glfwSetWindowUserPointer(window_, nullptr);
    ::glfwDestroyWindow(window_);
  }
}

impeller::hpp::Surface Window::CreateRenderSurface(
    const impeller::hpp::Context& context) {
  return WrapSurface(context, window_);
}

void Window::RegisterPythonBindings(nanobind::module_& m) {
  nanobind::class_<Window>(m, "Window")
      .def(nanobind::init())
      .def("create_render_surface", &Window::CreateRenderSurface,
           nanobind::rv_policy::move);
}

}  // namespace impeller::py
