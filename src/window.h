#pragma once

#include <GLFW/glfw3.h>
#include <nanobind/nanobind.h>
#include <glm/glm.hpp>
#include <impeller.hpp>
#include "context.h"

namespace impeller::py {

class Window {
 public:
  static Window& GetMainWindow();

  Window();

  ~Window();

  Window(const Window&) = delete;

  Window(Window&&) = delete;

  Window& operator=(const Window&) = delete;

  Window& operator=(Window&&) = delete;

  impeller::hpp::Surface CreateRenderSurface(const ContextWrapper& context);

  bool ShouldClose() const;

  void PollEvents() const;

 private:
  ::GLFWwindow* window_ = nullptr;
};

}  // namespace impeller::py
