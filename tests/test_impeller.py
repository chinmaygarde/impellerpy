from impeller import impellerpy
from impeller import impeller
from PIL import Image
from pyglm import glm
import os


def test_version():
    assert impellerpy.get_version() != 0


def test_structs():
    r = impeller.Rect(width=13, height=14)
    assert r.x == 0
    assert r.y == 0
    assert r.width == 13
    assert r.height == 14
    r2 = impeller.Rect()
    assert r2.width == 0


def test_display_list_builder():
    dl_builder = impeller.DisplayListBuilder()
    dl_builder.clip_oval(
        impeller.Rect(), impellerpy.ClipOperation_.DIFFERENCE
    ).build()


def test_can_create_window():
    context = impellerpy.Context_(impellerpy.ContextBackend_.METAL)
    window = impeller.Window()
    while not window.should_close():
        window.poll_events()
        surface = window.create_render_surface(context)
        paint = impeller.Paint()

        color = impeller.Color(a=1, b=1)
        paint.set_color(color)

        paint = impeller.Paint()
        paint.set_color(color)

        rect = impeller.Rect(100, 200, 200, 300)

        dl_builder = impeller.DisplayListBuilder()
        dl_builder.draw_rect(rect, paint)
        dl = dl_builder.build()

        surface.draw(dl)

        surface.present()


def test_can_draw_image(pytestconfig):
    image = Image.open(
        os.path.join(pytestconfig.rootpath, "assets/airplane.jpg")
    )
    assert image.size[0] != 0
    assert image.size[1] != 0
    desc = impeller.TextureDescriptor(
        impellerpy.PixelFormat_.RGBA8888,
        impeller.ISize(image.size[0], image.size[1]),
    )
    context = impellerpy.Context_(impellerpy.ContextBackend_.METAL)
    texture = impeller.Texture.with_contents(
        context,
        desc,
        image.convert("RGBA").tobytes(),
    )

    dl = (
        impeller.DisplayListBuilder()
        .push_transform(impeller.Matrix(glm.scale(glm.vec3(2)).to_list()))
        .draw_texture(
            texture,
            impeller.Point(100, 100),
            impellerpy.TextureSampling_.LINEAR,
            impeller.Paint(),
        )
        .build()
    )
    window = impeller.Window()
    while not window.should_close():
        window.poll_events()
        surface = window.create_render_surface(context)
        surface.draw(dl)
        surface.present()


def test_can_draw_text(pytestconfig):
    ctx = impeller.TypographyContext()
    builder = impeller.ParagraphBuilder(ctx)
    builder.push_style(
        impeller.ParagraphStyle()
        .set_background(impeller.Paint().set_color(impeller.Color(g=1, a=1)))
        .set_font_foreground(
            impeller.Paint().set_color(impeller.Color(r=1, a=1))
        )
        .set_font_weight(impellerpy.FontWeight_.W900)
        .set_height(2)
    )
    builder.add_text("Hello")
    para = builder.build(900)
    dl = (
        impeller.DisplayListBuilder()
        .scale(5.0, 5.0)
        .draw_paragraph(para, impeller.Point(100, 100))
        .build()
    )
    context = impellerpy.Context_(impellerpy.ContextBackend_.METAL)
    window = impeller.Window()
    while not window.should_close():
        window.poll_events()
        surface = window.create_render_surface(context)
        paint = impeller.Paint()

        color = impeller.Color(a=1, b=1)
        paint.set_color(color)

        paint = impeller.Paint()
        paint.set_color(color)

        surface.draw(dl)

        surface.present()
