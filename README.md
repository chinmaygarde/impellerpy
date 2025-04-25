# ImpellerPy

Nothing to see here yet. This is a very early exploratory effort.

## Prerequisites

* CMake (3.22 or above).
* Git.
* Ninja.
* Make.
* A C11 and C++20 compiler.
* [vcpkg](https://vcpkg.io/en/index.html) for package management.
  * Ensure that the `VCPKG_ROOT` environment variable is present and valid.
* The vcpkg step compiles cpython3. To do that successfully on macOS, you need to invoke (look in the failure log for details on dependencies on other platforms):
  ```sh
  brew install autoconf automake autoconf-archive
  ```


## Building

> [!IMPORTANT]
> Make sure you have completed all [pre-requisites](#prerequisites).

This project uses the CMake build system but use Make for tasks. Using Make is optional but makes things easier.

* Fetch all submodules.
  ```sh
  make sync
  ```
* Build the default CMake preset.
  ```sh
  make
  ```
