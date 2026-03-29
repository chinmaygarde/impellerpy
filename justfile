# This project uses CMake and Git sub-modules. This justfile is just in place
# to make common tasks easier.

build: build/args.gn
    cmake --build --preset default

[private]
build/args.gn:
    cmake --preset default

test: build check
    uv run pytest -rP

clean: clean-package
    rm -rf build
    rm -rf .venv
    rm -rf cache

clean-package:
    rm -rf dist

sync:
    git submodule update --init --recursive -j 8

format:
    uv run ruff format src tests

check:
    uv run ruff check

serve-docs:
    uv run mkdocs serve

deploy-docs:
    rm -rf site
    uv run mkdocs gh-deploy --force

package: clean-package
    uv build --wheel -v

docker: clean
    docker build -t chinmaygarde/impellerpy .
    docker run --rm -it -v `pwd`:/impellerpy -w /impellerpy chinmaygarde/impellerpy /bin/bash

docker-manylinux: clean
    docker build -f manylinux.Dockerfile -t chinmaygarde/impellerpy_manylinux .
    docker run --rm -it -v `pwd`:/impellerpy -w /impellerpy chinmaygarde/impellerpy_manylinux /bin/bash
