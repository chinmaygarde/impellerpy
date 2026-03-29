---
name: impellerpy build and CI conventions
description: Key facts about how impellerpy structures its build system and CI pipeline — important for auditing CI/build consistency
type: project
---

## Build system

- The project uses **CMake** as the real build backend, exposed through **`just`** (justfile) as a convenience wrapper for developers.
- The **Makefile was deleted** (commit 2ffe95b) and replaced with `justfile`. Target names changed slightly: underscores became hyphens (e.g., `deploy_docs` -> `deploy-docs`, `clean_package` -> `clean-package`, `serve_docs` -> `serve-docs`, `docker_manylinux` -> `docker-manylinux`).
- Python wheel builds use **`scikit-build-core`** + **`nanobind`** as the build backend (pyproject.toml), and packaging CI delegates entirely to **`cibuildwheel`** — it never calls `make` or `just` directly.
- Python tooling (pytest, ruff, mkdocs) is managed through **`uv`**.

## CI structure

- `.github/workflows/build.yml` — builds Python wheels on macos-13 and macos-15 via `cibuildwheel`, publishes to Test PyPI on releases. Does not call `make` or `just`.
- `.github/workflows/documentation.yml` — deploys MkDocs to GitHub Pages on push to main. Runs on `macos-latest`. Uses `uv` directly; **does not install `just`**, so justfile recipes must be inlined as shell commands.
- `.github/dependabot.yml` — monthly updates for github-actions and pip ecosystems.

## Established CI pattern

The documentation workflow inlines build commands directly (`uv run mkdocs gh-deploy --force`) rather than calling `just deploy-docs`, because `just` is not pre-installed on GitHub-hosted runners and the project has no setup-just step. This is the established pattern — follow it for any future CI steps rather than adding a `just` install step.

**Why:** `build.yml` never uses `just` either; it delegates to `cibuildwheel`. Keeping CI self-contained avoids an extra tool installation.

**How to apply:** When auditing or writing CI steps for this project, inline the underlying `uv`/`cmake` commands from the justfile rather than calling `just <recipe>`.
