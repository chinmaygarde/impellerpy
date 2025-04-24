# Library
add_library(new_cpp_project
  project.h
  project.cc
)

# Configure Fixtures Location
get_filename_component(TEST_ASSETS_LOCATION ../assets ABSOLUTE)
configure_file(fixtures_location.h.in fixtures_location.h @ONLY)

# Unittests
add_executable(new_cpp_project_tests
  unittests.cc
  ${CMAKE_CURRENT_BINARY_DIR}/fixtures_location.h
)
target_link_libraries(new_cpp_project_tests
  new_cpp_project
  GTest::gtest_main
)
target_include_directories(new_cpp_project_tests
  PUBLIC
    ${CMAKE_CURRENT_BINARY_DIR}
)
gtest_discover_tests(new_cpp_project_tests)
