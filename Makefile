# This project uses CMake and Git sub-modules. This Makefile is just in place
# to make common tasks easier.

.PHONY: clean build sync test format check serve_docs

build: build/build.ninja
	cmake --build --preset default

test: .venv build check
	uv run pytest -rP

.venv:
	uv sync

build/build.ninja:
	cmake --preset default

clean:
	rm -rf build

sync:
	git submodule update --init --recursive -j 8

format:
	uv run ruff format src tests
	uv run ruff format

check:
	uv run ruff check

serve_docs:
	uv run mkdocs serve
