#pragma once

#include <impeller.hpp>

namespace impeller::py {

enum class ContextBackend {
  kOpenGLES,
  kMetal,
  kVulkan,
};

class ContextWrapper {
 public:
  ContextWrapper(ContextBackend backend);

  ContextWrapper(const ContextWrapper&) = delete;

  ContextWrapper(ContextWrapper&&) = delete;

  ContextWrapper& operator=(const ContextWrapper&) = delete;

  ContextWrapper& operator=(ContextWrapper&&) = delete;

  const hpp::Context& GetContext() const;

 private:
  hpp::Context context_;
};

}  // namespace impeller::py
