#include <nanobind/nanobind.h>

#include "bindings.h"
#include "setup.h"
#include "window.h"

NB_MODULE(impellerpy, m) {
  impeller::py::SetupOnce();

  impeller::py::BindImpeller(m);
}
