#pragma once

#include <GLFW/glfw3.h>
#include <impeller.hpp>

namespace impeller::py {

void ApplyGLFWWindowHints();

bool ConfigurePlatformWindow(GLFWwindow* window);

impeller::hpp::Surface WrapSurface(const impeller::hpp::Context& context,
                                   GLFWwindow* window);

}  // namespace impeller::py
