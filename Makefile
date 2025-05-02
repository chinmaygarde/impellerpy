# This project uses CMake and Git sub-modules. This Makefile is just in place
# to make common tasks easier.

.PHONY: clean build sync test format check serve_docs deploy_docs package

build: package

test: .venv build check
	uv run pytest -rP

.venv:
	uv sync

clean:
	rm -rf build
	rm -rf .venv
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

package:
	uv build
