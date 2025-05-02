# This project uses CMake and Git sub-modules. This Makefile is just in place
# to make common tasks easier.

.PHONY: clean build sync test format check serve_docs deploy_docs clean_package package

build: build/build.ninja
	cmake --build --preset default

test: .venv build check
	uv run pytest -rP

.venv:
	uv sync

build/build.ninja:
	cmake --preset default

clean: clean_package
	@echo "Cleaning directories used for local development."
	rm -rf build
	rm -rf .venv

clean_package:
	@echo "Cleaning directories used to build the package."
	rm -rf dist
	rm -rf skbuild

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
	uv build --wheel
