---
name: impellerpy API patterns and naming conventions
description: Key API facts needed to verify code examples in documentation are correct
type: project
---

**Build tool:** `just` (justfile). The Makefile was deleted (commit 2ffe95b). All build commands use `just`, not `make`.

**Enum naming:** Python enums use SCREAMING_SNAKE_CASE (e.g., `BlendMode.SOURCE_OVER`, `TileMode.CLAMP`, `FontWeight.W700`). NOT Flutter/Dart-style `kSourceOver` / `kBold`.

**Window:** `Window()` takes no arguments. Default size is 800x600 (hardcoded in C++). There are no `width`, `height`, or `title` parameters.

**Surface:** Not directly instantiated. Obtained via `window.create_render_surface(context)`. Draw with `surface.draw(dl)` and present with `surface.present()`. There is no `acquire_render_surface`, `present_render_surface`, or `draw_display_list` method.

**ParagraphBuilder:** Constructor signature is `ParagraphBuilder(typo_ctx)` — one argument only. Styles are set via `.push_style(style)`. `.build()` takes a positional `width: float` (not a `max_width` keyword argument).

**ColorSource:** Static factory methods are `ColorSource.linear_gradient(...)`, `ColorSource.conical_gradient(...)`, `ColorSource.radial_gradient(...)`, `ColorSource.sweep_gradient(...)`, `ColorSource.image(...)`. NOT `make_linear_gradient`.
`linear_gradient` parameter order: `start_point`, `end_point`, `colors`, `stops`, `tile_mode`.

**Export count:** `__all__` in `src/impellerpy/__init__.py` has 44 symbols (not 49).

**Why:** Discovered during doc audit 2026-03-28. The README examples were written with incorrect Flutter/Dart-style names and incorrect API signatures.
