# ImpellerPy

Python Bindings to [Impeller](https://github.com/flutter/flutter/blob/main/engine/src/flutter/impeller/README.md). [Flutters](https://flutter.dev/) rendering engine.

## Prerequisites

* A C11 and C++20 compiler.
* CMake (3.22 or above).
* Git.
* Ninja.
* [vcpkg](https://vcpkg.io/en/index.html) for package management.
  * Ensure that the `VCPKG_ROOT` environment variable is present and valid.
* vcpkg compiles cpython3. To do that successfully on macOS, you need to invoke the following on macOS:
  ```sh
  brew install autoconf automake autoconf-archive
  ```
  * Look in the failure log for details on dependencies on other platforms.


## Building

> [!IMPORTANT]
> Make sure you have completed all [pre-requisites](#prerequisites). The first time you build, vcpkg will attempt to pull and build all dependencies. This will take a while. But the results will be cached.

This project uses the CMake build system but use Make for tasks. Using Make is optional but makes things easier.

* Fetch all submodules.
  ```sh
  make sync
  ```
* Build the default CMake preset.
  ```sh
  make
  ```
