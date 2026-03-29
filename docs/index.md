# ImpellerPy

Python bindings to [Impeller](https://github.com/flutter/flutter/blob/main/engine/src/flutter/impeller/README.md), [Flutter's](https://flutter.dev/) GPU-accelerated 2D rendering engine. ImpellerPy lets Python developers create high-performance graphics applications — with windows, vector paths, gradients, image filters, and rich typography — without requiring Flutter or Dart.

## Installation

=== "uv"
    ```sh
    uv add impellerpy
    ```
=== "pip"
    ```sh
    pip install impellerpy
    ```

## Quick Start

```python
from impellerpy import (
    Context, Window, DisplayListBuilder,
    Paint, Color, Rect, BlendMode
)

ctx = Context()
window = Window()

paint = (
    Paint()
    .set_color(Color(r=0.2, g=0.6, b=1.0, a=1.0))
    .set_blend_mode(BlendMode.SOURCE_OVER)
    .set_stroke_width(3.0)
)

dl = (
    DisplayListBuilder()
    .draw_rect(Rect(100, 100, 300, 200), paint)
    .build()
)

surface = window.create_render_surface(ctx)
surface.draw(dl)
surface.present()
```

See [Usage](usage.md) for installation details and [API Reference](reference.md) for the full API.
