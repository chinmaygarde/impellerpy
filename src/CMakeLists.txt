
find_package(Python
  COMPONENTS Interpreter Development
  REQUIRED
)

find_package(nanobind
  REQUIRED
)

nanobind_add_module(impellerpy
  impellerpy.cc
)
