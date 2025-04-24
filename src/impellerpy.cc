#include <nanobind/nanobind.h>
#include <impeller.hpp>

int version() {
  return ImpellerGetVersion();
}

NB_MODULE(impellerpy, module) {
  module.def("version", &version);
}
