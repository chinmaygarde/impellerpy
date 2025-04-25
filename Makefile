# This project uses CMake and Git sub-modules. This Makefile is just in place
# to make common tasks easier.

.PHONY: clean build sync test

build: build/build.ninja
	cmake --build --preset default

test: build
	uvx pytest

build/build.ninja:
	cmake --preset default

clean:
	rm -rf build

sync:
	git submodule update --init --recursive -j 8
