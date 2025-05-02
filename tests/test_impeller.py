from impellerpy.impeller import *
from impellerpy.impellerpy import *
from PIL import Image
from pyglm import glm
import os


def test_version():
    assert get_version() != 0


def test_structs():
    r = Rect(width=13, height=14)
    assert r.x == 0
    assert r.y == 0
    assert r.width == 13
    assert r.height == 14
    r2 = Rect()
    assert r2.width == 0


def test_display_list_builder():
    dl_builder = DisplayListBuilder()
    dl_builder.clip_oval(
        Rect(),
        ClipOperation.DIFFERENCE,
    ).build()


def test_can_create_window():
    context = Context()
    window = Window()
    while not window.should_close():
        window.poll_events()
        surface = window.create_render_surface(context)
        paint = Paint()

        color = Color(a=1, b=1)
        paint.set_color(color)

        paint = Paint()
        paint.set_color(color)

        rect = Rect(100, 200, 200, 300)

        dl_builder = DisplayListBuilder()
        dl_builder.draw_rect(rect, paint)
        dl = dl_builder.build()

        surface.draw(dl)

        surface.present()
        break


def test_can_draw_image(pytestconfig):
    image = Image.open(
        os.path.join(pytestconfig.rootpath, "assets/airplane.jpg")
    )
    assert image.size[0] != 0
    assert image.size[1] != 0
    desc = TextureDescriptor(
        PixelFormat.RGBA8888,
        ISize(image.size[0], image.size[1]),
    )
    context = Context()
    texture = Texture.with_contents(
        context,
        desc,
        image.convert("RGBA").tobytes(),
    )

    dl = (
        DisplayListBuilder()
        .push_transform(Matrix(glm.scale(glm.vec3(2)).to_list()))
        .draw_texture(
            texture,
            Point(100, 100),
            TextureSampling.LINEAR,
            Paint(),
        )
        .build()
    )
    window = Window()
    while not window.should_close():
        window.poll_events()
        surface = window.create_render_surface(context)
        surface.draw(dl)
        surface.present()
        break


def test_can_draw_text():
    ctx = TypographyContext()
    para = (
        ParagraphBuilder(ctx)
        .push_style(
            ParagraphStyle()
            .set_background(Paint().set_color(Color(g=1, a=1)))
            .set_font_foreground(Paint().set_color(Color(r=1, a=1)))
            .set_font_weight(FontWeight.W900)
        )
        .add_text("Hello")
        .build(900)
    )
    dl = (
        DisplayListBuilder()
        .scale(5.0, 5.0)
        .draw_paragraph(para, Point(100, 100))
        .build()
    )
    context = Context()
    window = Window()
    while not window.should_close():
        window.poll_events()
        surface = window.create_render_surface(context)
        surface.draw(dl)
        surface.present()
        break


def test_can_draw_conical_gradient():
    dl = (
        DisplayListBuilder()
        .draw_rect(
            Rect(0, 0, 500, 500),
            Paint().set_color_source(
                ColorSource.conical_gradient(
                    Point(500, 500),
                    100.0,
                    Point(0, 0),
                    200.0,
                    [0, 1],
                    [
                        Color(r=1, a=1),
                        Color(b=1, a=1),
                    ],
                    TileMode.REPEAT,
                )
            ),
        )
        .build()
    )
    context = Context()
    window = Window()
    while not window.should_close():
        window.poll_events()
        surface = window.create_render_surface(context)
        surface.draw(dl)
        surface.present()
        break
