#include <nanobind/nanobind.h>
#include <impeller.hpp>

PY_INT32_T version() {
  return ImpellerGetVersion();
}

NB_MODULE(impellerpy, module) {
  module.def("version", &version);
}
