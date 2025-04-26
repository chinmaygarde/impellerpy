#pragma once

#include <GLFW/glfw3.h>
#include <nanobind/nanobind.h>
#include <glm/glm.hpp>
#include <impeller.hpp>

namespace impeller::py {

class Window {
 public:
  static void RegisterPythonBindings(nanobind::module_& m);

  Window();

  ~Window();

  Window(const Window&) = delete;

  Window(Window&&) = delete;

  Window& operator=(const Window&) = delete;

  Window& operator=(Window&&) = delete;

  impeller::hpp::Surface CreateRenderSurface(
      const impeller::hpp::Context& context);

 private:
  ::GLFWwindow* window_ = nullptr;
};

}  // namespace impeller::py
