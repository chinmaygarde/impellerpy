#include "window.h"

#include "cocoa.h"

#include <iostream>
#include <mutex>

namespace impeller::py {

static void SetupGLFW() {
  ::glfwSetErrorCallback([](int error, const char* description) {
    std::cout << "GLFW Error: (" << error << ") " << description;
  });
  ::glfwInit();
}

static void SetupGLFWOnce() {
  static std::once_flag sOnce;
  std::call_once(sOnce, []() { SetupGLFW(); });
}

Window::Window() {
  SetupGLFWOnce();

  ::glfwDefaultWindowHints();
  ::glfwWindowHint(GLFW_VISIBLE, GLFW_TRUE);
  ::glfwWindowHint(GLFW_CLIENT_API, GLFW_NO_API);

  window_ = ::glfwCreateWindow(800, 600, "Window", nullptr, nullptr);
  ::glfwSetWindowUserPointer(window_, this);

  ConfigureCocoaWindow(window_);
}

Window::~Window() {
  if (window_) {
    ::glfwHideWindow(window_);
    ::glfwSetWindowUserPointer(window_, nullptr);
    ::glfwDestroyWindow(window_);
  }
}

impeller::hpp::Surface Window::CreateRenderSurface(
    const impeller::hpp::Context& context) {
  return WrapSurface(context, window_);
}

bool Window::ShouldClose() const {
  return ::glfwWindowShouldClose(window_) == GLFW_TRUE;
}

void Window::PollEvents() const {
  ::glfwPollEvents();
}

}  // namespace impeller::py
