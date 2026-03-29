---
name: impellerpy documentation structure
description: Where documentation lives, build tooling, and key doc-to-code mappings for impellerpy
type: project
---

Documentation lives in three places:
- `README.md` — comprehensive GitHub README with Mermaid diagrams, API overview, usage examples, build instructions, platform support
- `README_PYPI.md` — minimal PyPI page description; used as the `readme` field in `pyproject.toml`
- `docs/` — MkDocs source (index.md, usage.md, reference.md); deployed to GitHub Pages via `just deploy-docs`

**Why:** The README was comprehensively rewritten (2026-03-28) with full API examples. The docs/ site is thin by design — it delegates detail to the README and uses mkdocstrings to auto-generate the API reference from `impellerpy.pyi`.

**How to apply:** When auditing, check README.md first for accuracy; docs/index.md should mirror a condensed version of the README's intro and quick-start. docs/reference.md is auto-generated and does not need manual updates. docs/usage.md covers install only.
