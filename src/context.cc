#include "context.h"

#include <hedley.h>

namespace impeller::py {

static hpp::Context CreateContext(ContextBackend backend) {
  switch (backend) {
    case ContextBackend::kOpenGLES:
      break;
    case ContextBackend::kMetal:
      return hpp::Context(ImpellerContextCreateMetalNew(ImpellerGetVersion()),
                          hpp::AdoptTag::kAdopt);
    case ContextBackend::kVulkan:
      break;
  }
  HEDLEY_UNREACHABLE();
}

ContextWrapper::ContextWrapper(ContextBackend backend)
    : context_(CreateContext(backend)) {}

const hpp::Context& ContextWrapper::GetContext() const {
  return context_;
}

}  // namespace impeller::py
