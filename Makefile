# This project uses CMake and Git sub-modules. This Makefile is just in place
# to make common tasks easier.

.PHONY: clean build sync test format check serve_docs deploy_docs clean_package package docker

build: build/args.gn
	cmake --build --preset default

build/args.gn:
	cmake --preset default

test: build check
	uv run pytest -rP

clean: clean_package
	rm -rf build
	rm -rf .venv
	rm -rf cache

clean_package:
	rm -rf dist

sync:
	git submodule update --init --recursive -j 8

format:
	uv run ruff format src tests

check:
	uv run ruff check

serve_docs:
	uv run mkdocs serve

deploy_docs:
	rm -rf site
	uv run mkdocs gh-deploy --force

package: clean_package
	uv build --wheel -v

docker: clean
	docker build -t chinmaygarde/impellerpy .
	docker run --rm -it -v `pwd`:/impellerpy -w /impellerpy chinmaygarde/impellerpy /bin/bash

docker_manylinux: clean
	docker build -f manylinux.Dockerfile -t chinmaygarde/impellerpy_manylinux .
	docker run --rm -it -v `pwd`:/impellerpy -w /impellerpy chinmaygarde/impellerpy_manylinux /bin/bash
