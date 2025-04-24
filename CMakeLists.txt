cmake_minimum_required(VERSION 3.22)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/tools/cmake")

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/third_party/cmake_toolbox")
include(CMakeToolboxInitialize)

CMakeToolboxInitialize()

SetCAndCXXStandard(11 20)

EnableCCache()

project(new_cpp_project)

enable_testing()

include(GoogleTest)
include(CTest)

find_package(GTest CONFIG REQUIRED)

# Project
add_subdirectory(src)
