# ------------------------------------------------------------------------------
# --- Setup Impeller -----------------------------------------------------------
# ------------------------------------------------------------------------------
cmake_policy(SET CMP0135 NEW)
include(FetchContent)

set(IMPELLER_SDK_SHA 7592aeaa90495784353fbbe5116f7e33cc8f9a4a)
if(CMAKE_HOST_APPLE)
  set(IMPELLER_PLATFORM darwin)
  set(IMPELLER_DYLIB libimpeller.dylib)
elseif(CMAKE_HOST_LINUX)
  set(IMPELLER_PLATFORM linux)
  set(IMPELLER_DYLIB libimpeller.so)
elseif(CMAKE_HOST_WIN32)
  set(IMPELLER_PLATFORM windows)
  set(IMPELLER_DYLIB libimpeller.dll)
else()
message(FATAL_ERROR "Unsupported platform.")
endif()

if (CMAKE_HOST_SYSTEM_PROCESSOR STREQUAL "aarch64")
  set(IMPELLER_ARCH arm64)
elseif (CMAKE_HOST_SYSTEM_PROCESSOR STREQUAL "arm64")
  set(IMPELLER_ARCH arm64)
elseif(CMAKE_HOST_SYSTEM_PROCESSOR STREQUAL "x86_64")
  set(IMPELLER_ARCH x64)
else()
message(FATAL_ERROR "Unsupported architecture ${CMAKE_HOST_SYSTEM_PROCESSOR} while downloading the Impeller dylib.")
endif()

message(NOTICE "Impeller SDK ${IMPELLER_SDK_SHA} for ${IMPELLER_PLATFORM}-${IMPELLER_ARCH} selected.")

FetchContent_Declare(
  impeller_sdk
  URL https://storage.googleapis.com/flutter_infra_release/flutter/${IMPELLER_SDK_SHA}/${IMPELLER_PLATFORM}-${IMPELLER_ARCH}/impeller_sdk.zip
)
FetchContent_MakeAvailable(impeller_sdk)
add_library(impeller SHARED IMPORTED)

set_target_properties(impeller
  PROPERTIES
  IMPORTED_LOCATION ${impeller_sdk_SOURCE_DIR}/lib/${IMPELLER_DYLIB}
)
target_include_directories(impeller INTERFACE ${impeller_sdk_SOURCE_DIR}/include)
list(APPEND CMAKE_INSTALL_RPATH ${impeller_sdk_SOURCE_DIR}/lib)
list(APPEND CMAKE_BUILD_RPATH ${impeller_sdk_SOURCE_DIR}/lib)

if(APPLE)
execute_process(COMMAND install_name_tool -id "@rpath/libimpeller.dylib" libimpeller.dylib
                WORKING_DIRECTORY ${impeller_sdk_SOURCE_DIR}/lib)
endif(APPLE)

# ------------------------------------------------------------------------------
# --- Build Python Module ------------------------------------------------------
# ------------------------------------------------------------------------------

find_package(
  Python 3.8 REQUIRED
  COMPONENTS Interpreter Development.Module
  OPTIONAL_COMPONENTS Development.SABIModule
)

find_package(nanobind
  CONFIG
  REQUIRED
)

nanobind_add_module(impellerpy
  LTO STABLE_ABI NB_STATIC
  bindings.cc
  bindings.h
  platform.h
  impellerpy.cc
  setup.cc
  setup.h
  window.cc
  window.h
)

if (APPLE)
target_sources(impellerpy
  PRIVATE
    platform.mm
)
else()
target_sources(impellerpy
  PRIVATE
    platform.cc
)
endif()

target_link_libraries(impellerpy
  PRIVATE
    impeller
    glfw
)

if(APPLE)
  target_link_libraries(impellerpy
    PRIVATE
        "-framework Metal"
        "-framework QuartzCore"
  )
endif()

install(TARGETS impellerpy
  LIBRARY
  DESTINATION impellerpy
)
install(IMPORTED_RUNTIME_ARTIFACTS impeller
  DESTINATION impellerpy
)
