# A New C++ Project

This is a project template Chinmay uses for his C++ projects.

## Prerequisites

* CMake (3.22 or above).
* Git.
* Ninja.
* Make.
* A C11 and C++20 compiler.
* [vcpkg](https://vcpkg.io/en/index.html) for package management.
  * Ensure that the `VCPKG_ROOT` environment variable is present and valid.

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
